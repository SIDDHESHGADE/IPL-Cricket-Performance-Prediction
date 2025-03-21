import streamlit as st
import pandas as pd
import pickle 

# Load the trained model
with open("Batter.pkl", "rb") as model_file:
    model = pickle.load(model_file)


# Load dataset to extract unique dropdown values
df = pd.read_csv(r"C:\Personal project\IPL\final_data.csv")  

# Extract unique values for dropdowns
batter_options = sorted(df["batter"].dropna().unique())   # Sorting for better UI experience
bowler_options = sorted(df["bowler"].dropna().unique())
non_striker_options = sorted(df["non_striker"].dropna().unique())
venue_options = sorted(df["venue"].dropna().unique())
team1_options = sorted(df["team1"].dropna().unique())
team2_options = sorted(df["team2"].dropna().unique())
season_options = [2020, 2021, 2022, 2023, 2024]  

# Streamlit UI
st.title("🏏 Cricket Prediction Model")

batter = st.selectbox("🏏 Select Batter", batter_options)
bowler = st.selectbox("🎯 Select Bowler", bowler_options)
non_striker = st.selectbox("🏃‍♂️ Select Non-Striker", non_striker_options)
venue = st.selectbox("📍 Select Venue", venue_options)
team1 = st.selectbox("🏆 Select Team 1", team1_options)
team2 = st.selectbox("🏆 Select Team 2", team2_options)
season = st.selectbox("📅 Select Season", season_options)

balls_count = st.number_input("⚾ Enter Balls Count", min_value=1, step=1)
strike_rate = st.number_input("🚀 Enter Strike Rate", min_value=0.0, step=0.1)

if st.button("📊 Predict"):
    # Convert user input into a Pandas DataFrame
    user_input = pd.DataFrame([[batter, bowler, non_striker, venue, season, team1, team2, balls_count, strike_rate]],
                              columns=['batter', 'bowler', 'non_striker', 'venue', 'season', 'team1', 'team2', 'balls_count', 'strike_rate'])

    # Make prediction
    prediction = model.predict(user_input)

    # Display the predicted output
    st.success(f"🎯 Predicted Runs : {prediction[0]}")
