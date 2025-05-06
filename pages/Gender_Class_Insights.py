import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Gender & Class Insights", layout="wide")
st.markdown("<style>" + open("style.css").read() + "</style>", unsafe_allow_html=True)

st.title("Gender & Class Insights")

df = sns.load_dataset("titanic").dropna()

# Plot 1 — Countplot of Gender by Class
st.subheader("Gender Distribution by Class")
fig1, ax1 = plt.subplots(figsize=(8, 4))
sns.countplot(data=df, x="pclass", hue="sex", ax=ax1)
st.pyplot(fig1)

# Plot 2 — Survival by Gender in Each Class
st.subheader(" Survival by Gender Within Class")
fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.barplot(data=df, x="pclass", y="survived", hue="sex", ax=ax2)
st.pyplot(fig2)

# Plot 3 — Violin Plot: Age vs. Class
st.subheader("Age Distribution Across Classes")
fig3, ax3 = plt.subplots(figsize=(8, 4))
sns.violinplot(data=df, x="pclass", y="age", hue="sex", split=True, ax=ax3)
st.pyplot(fig3)

with st.expander("Interpretation"):
    st.write("""
    - Most women were in 2nd class; men dominated 3rd class.
    - Women had significantly higher survival in every class.
    - Class 1 passengers were older, indicating higher wealth status.
    """)
