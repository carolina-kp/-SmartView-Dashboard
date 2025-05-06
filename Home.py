import streamlit as st

st.set_page_config(page_title="SmartView", layout="wide", page_icon="🚢")
st.markdown("<style>" + open("style.css").read() + "</style>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>🚢 SmartView Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #6f90af;'>A cognitive-optimized environment for business-like decision-making</h3>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("### Mission")
st.markdown("""
This dashboard uses **cognitive psychology**, **bias mitigation**, and **data visualization theory** to support high-stakes decision-making.
Users navigate through the **five stages of decision-making** using an interface based on *Decision Hierarchy* (PDF 13).
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("#### Explore Patterns")
    st.markdown("- Correlation heatmaps\n- Subgroup filters\n- Bar comparisons")
with col2:
    st.markdown("#### Cognitive Tools")
    st.markdown("- Bias reduction\n- Visual hierarchy\n- Expanders")
with col3:
    st.markdown("#### 🤖 Smart Assistant")
    st.markdown("- Ask about survival factors\n- Bias explanations\n- Reflection prompts")

st.success("Use the **left sidebar** to navigate between sections.")
