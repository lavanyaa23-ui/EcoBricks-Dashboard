import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------
# SAMPLE DATA
# -----------------------
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Plastic_Collected_kg": [120, 150, 180, 220, 260, 300],
    "Eco_Bricks_Made": [240, 300, 360, 440, 520, 600],
    "Volunteers": [15, 20, 25, 28, 30, 35]
}

df = pd.DataFrame(data)
df["CO2_Saved_kg"] = df["Plastic_Collected_kg"] * 1.5

# -----------------------
# DASHBOARD LAYOUT
# -----------------------
st.set_page_config(page_title="Eco Bricks Dashboard", layout="wide")

st.title("♻️ Eco Bricks Creation - Plastic Waste Management")
st.markdown("This dashboard shows insights from the eco-bricks project.")

# KPIs (Key Metrics)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Plastic Collected", f"{df['Plastic_Collected_kg'].sum()} kg")
col2.metric("Total Eco Bricks", df['Eco_Bricks_Made'].sum())
col3.metric("Total Volunteers", df['Volunteers'].sum())
col4.metric("CO₂ Saved", f"{df['CO2_Saved_kg'].sum()} kg")

# -----------------------
# Charts
# -----------------------
# Plastic Collected Trend
fig1 = px.line(df, x="Month", y="Plastic_Collected_kg", markers=True, title="Plastic Collected Over Months")
st.plotly_chart(fig1, use_container_width=True)

# Eco Bricks Made
fig2 = px.bar(df, x="Month", y="Eco_Bricks_Made", color="Eco_Bricks_Made", title="Eco Bricks Made Each Month")
st.plotly_chart(fig2, use_container_width=True)

# Volunteers Pie Chart
fig3 = px.pie(df, values="Volunteers", names="Month", title="Volunteers Participation")
st.plotly_chart(fig3, use_container_width=True)

# CO2 Savings
fig4 = px.area(df, x="Month", y="CO2_Saved_kg", title="Estimated CO₂ Savings")
st.plotly_chart(fig4, use_container_width=True)
