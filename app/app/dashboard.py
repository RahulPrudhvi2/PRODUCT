import streamlit as st
import sys
import os
import pandas as pd
import plotly.express as px

# ---------------- FIX IMPORT PATH ----------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

# Safe import (prevents crash if main not found)
try:
    from main import run_pipeline
except Exception as e:
    st.error(f"Error importing pipeline: {e}")
    st.stop()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="PLM Agentic AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM UI ----------------
# Custom CSS for a cleaner look (FIXED)

st.title("🚀 PLM Agentic AI Dashboard")
st.caption("Real-time Product Lifecycle Management & Predictive Maintenance")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("⚙️ System Controls")
    st.info("Adjust parameters to simulate asset conditions.")

    temp = st.slider("Temperature (°C)", 20, 120, 80)
    vib = st.slider("Vibration (mm/s)", 0.0, 10.0, 3.0)
    cycle = st.number_input("Current Cycle Count", 0, 10000, 850)

    st.divider()
    run_btn = st.button("⚡ Run Agentic Analysis", use_container_width=True, type="primary")

# ---------------- INPUT DATA ----------------
data = {
    "temperature": temp,
    "vibration": vib,
    "cycle_count": cycle
}

# ---------------- MAIN LOGIC ----------------
if run_btn:
    with st.spinner("Agent analyzing telemetry data..."):

        try:
            result = run_pipeline(data)
        except Exception as e:
            st.error(f"Pipeline Error: {e}")
            st.stop()

        # SAFE EXTRACTION
        monitor = result.get("monitoring", {})
        analytics = result.get("analytics", {})
        decision = result.get("decision", "No decision available")

        # DEFAULT SAFE VALUES
        rul = int(analytics.get("rul", 0))
        failure_prob = float(analytics.get("failure_prob_7d", 0))

    # ---------------- METRICS ----------------
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Temperature",
        f"{temp}°C",
        delta=f"{temp-70}°C" if temp > 70 else None,
        delta_color="inverse"
    )

    col2.metric(
        "Vibration",
        f"{vib} mm/s",
        delta="High" if vib > 7 else None,
        delta_color="inverse"
    )

    col3.metric("Predicted RUL", f"{rul} Cycles")

    health_score = max(0, 100 - (failure_prob * 100))
    col4.metric("System Health", f"{int(health_score)}%")

    # ---------------- STATUS + DECISION ----------------
    st.markdown("### 🧠 Agent Intelligence")
    status_col, decision_col = st.columns([1, 2])

    with status_col:
        if monitor.get("anomaly", False):
            st.error("### 🚨 Anomaly Detected\nUnusual patterns found.")
        else:
            st.success("### ✅ System Normal\nAll telemetry within safe bounds.")

    with decision_col:
        if "IMMEDIATE" in decision:
            st.error(f"**Action Required:** {decision}")
        elif "SCHEDULE" in decision:
            st.warning(f"**Advisory:** {decision}")
        else:
            st.info(f"**Recommendation:** {decision}")

    # ---------------- VISUALIZATION ----------------
    st.divider()
    graph_col, insight_col = st.columns([2, 1])

    with graph_col:
        st.subheader("📈 Predictive RUL Decay")

        try:
            if rul > 0:
                cycles_range = list(range(cycle, cycle + rul + 100, 50))

                df_plot = pd.DataFrame({
                    "Cycles": cycles_range,
                    "RUL Forecast": [max(0, rul - (i - cycle)) for i in cycles_range]
                })

                fig = px.line(
                    df_plot,
                    x="Cycles",
                    y="RUL Forecast",
                    template="plotly_white"
                )

                st.plotly_chart(fig, use_container_width=True)

            else:
                st.warning("No RUL data available for plotting.")

        except Exception as e:
            st.error(f"Plot Error: {e}")

    # ---------------- INSIGHTS ----------------
    with insight_col:
        st.subheader("📝 Executive Summary")

        criticality = "High" if temp > 90 or vib > 7 else "Low"

        st.markdown(f"""
        **Analysis Overview:**
        - **Risk Level:** {failure_prob * 100:.1f}% failure probability  
        - **Criticality:** {criticality}  

        **Agent Narrative:**
        The PLM Agent evaluated the asset at cycle **{cycle}**.
        Current behavior suggests normal degradation patterns,
        but vibration trends may require closer inspection.
        """)

# ---------------- DEFAULT STATE ----------------
else:
    st.write("---")
    st.info("👈 Adjust parameters in the sidebar and click 'Run Analysis'")