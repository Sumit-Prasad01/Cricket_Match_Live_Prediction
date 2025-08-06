import streamlit as st
import numpy as np
import pandas as pd
import pickle
# from streamlit_option_menu import option_menu

# === (Optional) Load Trained Model ===
@st.cache_resource
def load_model():
    return pickle.load(open("models/random_forest_model", "rb"))

# model = load_model()  # Not used for rule-based classification

st.title("🏏 All-Rounder Type Classifier In ODI Cricket")

with st.sidebar:
    selected = option_menu('Classification of All Rounders',
                           ['ODI Classification', 'T20 Classification', 'Test Classification'],default_index=0)

st.markdown("Enter player stats below:")

# === User Input Fields ===
Mat = st.number_input("Matches Played (Mat)", min_value=0)
Runs = st.number_input("Total Runs", min_value=0)
HS = st.number_input("Highest Score (HS)", min_value=0)
Batting_Ave = st.number_input("Batting Average", min_value=0.0)
Hundreds = st.number_input("100s Scored", min_value=0)
Wkts = st.number_input("Total Wickets", min_value=0)
Bowling_Ave = st.number_input("Bowling Average", min_value=0.0)
Fifers = st.number_input("5 Wicket Hauls", min_value=0)
Ct = st.number_input("Catches Taken", min_value=0)

# === Feature Engineering ===
Runs_per_Match = Runs / (Mat + 1e-5)
Wkts_per_Match = Wkts / (Mat + 1e-5)
Batting_Impact = Batting_Ave * Hundreds
Bowling_Impact = Wkts / (Bowling_Ave + 1e-5)
Allrounder_Score = Batting_Impact + Bowling_Impact
HS_ratio = HS / (Runs + 1e-5)
Ct_per_Match = Ct / (Mat + 1e-5)

# === Rule-based All-Rounder Classification ===
def classify_allrounder(bat_avg, bowl_avg):
    if bat_avg >= 35 and bowl_avg >= 35:
        return "⚖️ Balanced All-Rounder"
    elif bat_avg >= 35 and bowl_avg < 35:
        return "🏏 Batting All-Rounder"
    elif bat_avg < 35 and bowl_avg < 35:
        return "🎯 Bowling All-Rounder"
    else:
        return "⚖️ Balanced All-Rounder"

# === Predict Button ===
if st.button("🔍 Classify All-Rounder Type"):
    category = classify_allrounder(Batting_Ave, Bowling_Ave)
    
    # Optional: Show features
    st.markdown("### 📊 Calculated Features:")
    st.write({
        "Runs_per_Match": round(Runs_per_Match, 2),
        "Wkts_per_Match": round(Wkts_per_Match, 2),
        "Batting_Impact": round(Batting_Impact, 2),
        "Bowling_Impact": round(Bowling_Impact, 2),
        "Allrounder_Score": round(Allrounder_Score, 2),
        "HS_ratio": round(HS_ratio, 2),
        "Ct_per_Match": round(Ct_per_Match, 2)
    })

    # Final classification
    st.success(f"🏆 Player is classified as: **{category}**")
