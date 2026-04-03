import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI Rail Controller", layout="wide")

st.title("🚂 AI-Powered Precise Train Traffic Control")

# 1. Sidebar
st.sidebar.header("Control Panel")
sim_speed = st.sidebar.slider("Simulation Speed", 1, 10, 1)
if st.sidebar.button("Simulate Signal Failure"):
    st.error("Signal Failure at Section B! Re-optimizing...")

# 2. KPI Section
col1, col2, col3 = st.columns(3)
col1.metric("Section Throughput", "+12%", "Optimal")
col2.metric("Total Delay Reduction", "45 mins", "-15%")
col3.metric("System Safety", "100%", "Secure")

# 3. The String Chart (Visualizing the 'Brain')
st.subheader("Live Section String Chart (Time vs. Distance)")
# Dummy data for the chart
chart_data = pd.DataFrame({
    'Time': [0, 10, 20, 30, 0, 15, 40],
    'Distance': [0, 5, 10, 15, 0, 5, 15],
    'Train': ['Rajdhani', 'Rajdhani', 'Rajdhani', 'Rajdhani', 'Freight', 'Freight', 'Freight']
})
fig = px.line(chart_data, x="Time", y="Distance", color="Train", markers=True)
st.plotly_chart(fig, use_container_width=True)

# 4. AI Recommendation Log
st.subheader("🤖 AI Decision Log")
st.write("👉 [14:02] Train 12301 cleared for Block A. High Priority.")
st.write("👉 [14:05] Train 88210 directed to Loop Line 1. Reason: Precedence.")
