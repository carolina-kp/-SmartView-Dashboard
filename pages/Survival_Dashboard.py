import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Survival Dashboard", layout="wide")
st.markdown("<style>" + open("style.css").read() + "</style>", unsafe_allow_html=True)

st.title("Survival Breakdown Dashboard")

df = sns.load_dataset("titanic").dropna()

# Plot 1 — Survival by Age Group
st.subheader("Survival Rate by Age Group")
df['age_group'] = pd.cut(df['age'], bins=[0, 12, 20, 40, 60, 100], labels=["Child", "Teen", "Adult", "Middle-aged", "Senior"])
fig1, ax1 = plt.subplots(figsize=(8, 4))
sns.barplot(data=df, x="age_group", y="survived", hue="sex", ax=ax1)
st.pyplot(fig1)

# Plot 2 — Survival by Embarkation Port
st.subheader("Survival by Embarkation Port")
fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.barplot(data=df, x="embarked", y="survived", hue="sex", ax=ax2)
st.pyplot(fig2)

# Plot 3 — Box Plot of Fare by Survival
st.subheader("Fare Distribution by Survival")
fig3, ax3 = plt.subplots(figsize=(8, 4))
sns.boxplot(data=df, x="survived", y="fare", hue="pclass", ax=ax3)
st.pyplot(fig3)

with st.expander(" Insights"):
    st.write("""
    - Children had higher survival, especially females.
    - Port 'C' had higher survival (likely wealthier passengers).
    - Survivors paid higher fares on average — socioeconomic impact is clear.
    """)

with st.expander("Bias Alert: Cognitive Reflection"):
    st.markdown("""
    This graph supports pattern recognition but may lead to **confirmation bias** if explored with fixed assumptions.
    
    Try changing filters or comparing unexpected groups to reduce bias and improve insight quality.
    """)
