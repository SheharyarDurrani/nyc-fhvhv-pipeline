import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="NYC Rideshare Dashboard", layout="wide")
st.title("🚕 NYC FHVHV Rideshare Dashboard - January 2026")
st.write("**20.9 million trips analysed | Source: NYC TLC**")

base = "E:/nyc-fhvhv-pipeline/data/outputs/"
market = pd.read_csv(base + "market_share.csv")
hours = pd.read_csv(base + "busiest_hours.csv")
days = pd.read_csv(base + "trips_by_day.csv")
airport = pd.read_csv(base + "airport_vs_regular.csv")
distance = pd.read_csv(base + "trip_distance_breakdown.csv")

# KPI Row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Trips", "20.9M")
col2.metric("Uber Market Share", "72.7%")
col3.metric("Avg Driver Pay", "$20.18")
col4.metric("Peak Hour", "6 PM")

st.divider()

# Row 1
col1, col2 = st.columns(2)
with col1:
    st.subheader("Uber vs Lyft Market Share")
    fig = px.pie(market, values='total_trips', names='carrier',
                 color_discrete_sequence=['#1f77b4','#ff7f0e'])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Trips by Hour of Day")
    fig2 = px.bar(hours, x='hour', y='total_trips',
                  color='total_trips', color_continuous_scale='blues')
    st.plotly_chart(fig2, use_container_width=True)

# Row 2
col1, col2 = st.columns(2)
with col1:
    st.subheader("Trips by Day of Week")
    fig3 = px.bar(days, x='day_of_week', y='total_trips',
                  color='avg_driver_pay', color_continuous_scale='reds')
    st.plotly_chart(fig3, use_container_width=True)

with col2:
    st.subheader("Airport vs Regular - Avg Driver Pay")
    fig4 = px.bar(airport, x='trip_type', y='avg_driver_pay',
                  color='trip_type')
    st.plotly_chart(fig4, use_container_width=True)

# Row 3
st.subheader("Trip Distance Breakdown")
fig5 = px.pie(distance, values='total_trips', names='trip_category')
st.plotly_chart(fig5, use_container_width=True)

st.markdown("**Built with Python, DuckDB & Streamlit**")