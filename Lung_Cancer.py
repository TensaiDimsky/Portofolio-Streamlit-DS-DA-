import streamlit as st
import pandas as pd

"""
Lung Cancer Risk Calculator
=========================================
Dibuat berdasarkan analisis dari "Lung Cancer Prediction Using Machine Learning"
oleh Dimas Wibisono.

Skema bobot risiko diambil dari Top Feature Importance hasil model XGBoost
(tuned):
    CancerHistory   ~ 0.40
    GeneticRisk     ~ 0.16
    Smoking         ~ 0.10
    Gender          ~ 0.095
    BMI Category    ~ 0.07
    Age Group       ~ 0.055
    AlcoholIntake   ~ 0.05
    ActivityLevel   ~ 0.045
"""

# ----------------------------------------------------------------------
# Konfigurasi halaman
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Kalkulator Risiko Kanker Paru",
    page_icon="🫁",
    layout="centered",
)

# ----------------------------------------------------------------------
# Bobot fitur (hasil feature importance XGBoost - Tuned)
# ----------------------------------------------------------------------
WEIGHTS = {
    "cancer_history": 0.40,
    "genetic_risk": 0.16,
    "smoking": 0.10,
    "gender": 0.095,
    "bmi_category": 0.07,
    "age_group": 0.055,
    "alcohol_intake": 0.05,
    "activity_level": 0.045,
}


def bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def bmi_risk_score(category: str) -> float:
    # Underweight & Obese dianggap faktor risiko lebih tinggi
    # dibanding BMI normal (pola umum epidemiologi kanker).
    mapping = {
        "Underweight": 0.8,
        "Normal": 0.2,
        "Overweight": 0.5,
        "Obese": 0.9,
    }
    return mapping[category]


def age_group(age: int) -> str:
    if age < 40:
        return "< 40 tahun"
    elif age <= 60:
        return "40 - 60 tahun"
    else:
        return "> 60 tahun"


def age_risk_score(group: str) -> float:
    mapping = {
        "< 40 tahun": 0.2,
        "40 - 60 tahun": 0.55,
        "> 60 tahun": 0.9,
    }
    return mapping[group]


def activity_level(activity: float) -> str:
    if activity <= 3:
        return "Rendah"
    elif activity <= 6:
        return "Sedang"
    else:
        return "Tinggi"


def activity_risk_score(level: str) -> float:
    # Aktivitas fisik tinggi -> risiko lebih rendah
    mapping = {"Rendah": 0.8, "Sedang": 0.5, "Tinggi": 0.2}
    return mapping[level]


def compute_risk(
    age: int,
    gender: str,
    bmi: float,
    smoking: bool,
    genetic_risk: str,
    physical_activity: float,
    alcohol_intake: float,
    cancer_history: bool,
):
    # --- Feature engineering ---
    bmi_cat = bmi_category(bmi)
    age_grp = age_group(age)
    act_lvl = activity_level(physical_activity)

    # --- Skor tiap fitur, dinormalisasi ke rentang 0-1 ---
    scores = {
        "cancer_history": 1.0 if cancer_history else 0.0,
        "genetic_risk": {"Rendah": 0.15, "Sedang": 0.55, "Tinggi": 0.95}[genetic_risk],
        "smoking": 1.0 if smoking else 0.0,
        "gender": 0.55 if gender == "Laki-laki" else 0.45,
        "bmi_category": bmi_risk_score(bmi_cat),
        "age_group": age_risk_score(age_grp),
        "alcohol_intake": min(alcohol_intake / 5, 1.0),
        "activity_level": activity_risk_score(act_lvl),
    }

    # --- Skor akhir tertimbang (0-100) ---
    weighted_sum = sum(scores[k] * WEIGHTS[k] for k in WEIGHTS)
    risk_percent = round(weighted_sum * 100, 1)

    details = {
        "BMI Category": bmi_cat,
        "Age Group": age_grp,
        "Activity Level": act_lvl,
    }

    return risk_percent, scores, details


def risk_label(risk_percent: float):
    if risk_percent < 35:
        return "RISIKO RENDAH", "green"
    elif risk_percent < 65:
        return "RISIKO SEDANG", "orange"
    else:
        return "RISIKO TINGGI", "red"


# ----------------------------------------------------------------------
# UI
# ----------------------------------------------------------------------
st.title("🫁 Kalkulator Risiko Kanker Paru")
st.caption(
    "Berdasarkan analisis faktor risiko pada dataset *Lung Cancer Prediction*"
    "ML terlatih — hanya untuk simulasi & edukasi, bukan diagnosis medis."
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    age = st.slider("Usia (tahun)", min_value=20, max_value=80, value=45)
    gender = st.radio("Jenis Kelamin", ["Laki-laki", "Perempuan"], horizontal=True)
    bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=24.0, step=0.1)
    genetic_risk = st.selectbox("Risiko Genetik", ["Rendah", "Sedang", "Tinggi"])

with col2:
    smoking = st.checkbox("Merokok?")
    cancer_history = st.checkbox("Punya riwayat kanker sebelumnya?")
    physical_activity = st.slider("Aktivitas Fisik per Minggu (skala 0-10)", 0.0, 10.0, 5.0, 0.5)
    alcohol_intake = st.slider("Konsumsi Alkohol per Minggu (skala 0-5)", 0.0, 5.0, 1.0, 0.5)

st.divider()

if st.button("🔍 Hitung Risiko", type="primary", use_container_width=True):
    risk_percent, scores, details = compute_risk(
        age, gender, bmi, smoking, genetic_risk,
        physical_activity, alcohol_intake, cancer_history,
    )
    label, color = risk_label(risk_percent)

    st.markdown(f"### Hasil: **:{color}[{label}]**")
    st.progress(min(int(risk_percent), 100))
    st.metric("Skor Risiko", f"{risk_percent}%")

    st.markdown("**Hasil Feature Engineering:**")
    d1, d2, d3 = st.columns(3)
    d1.metric("Kategori BMI", details["BMI Category"])
    d2.metric("Kelompok Usia", details["Age Group"])
    d3.metric("Level Aktivitas", details["Activity Level"])

    with st.expander("Lihat rincian kontribusi tiap faktor"):
        for k, v in scores.items():
            contrib = v * WEIGHTS[k] * 100
            st.write(f"- **{k.replace('_', ' ').title()}**: skor {v:.2f} × bobot {WEIGHTS[k]:.3f} = {contrib:.1f} poin")

    if label == "RISIKO TINGGI":
        st.error("Disarankan segera berkonsultasi dengan dokter untuk pemeriksaan lebih lanjut.")
    elif label == "RISIKO SEDANG":
        st.warning("Pertimbangkan pemeriksaan kesehatan rutin dan perbaikan gaya hidup.")
    else:
        st.success("Tetap jaga gaya hidup sehat dan lakukan pemeriksaan berkala.")

st.divider()
st.caption(
    "⚠️ Disclaimer: Kalkulator ini adalah alat simulasi edukatif berbasis bobot "
    "feature importance dari analisis data, BUKAN alat diagnosis medis. "
    "Selalu konsultasikan kondisi kesehatan Anda dengan tenaga medis profesional."
)