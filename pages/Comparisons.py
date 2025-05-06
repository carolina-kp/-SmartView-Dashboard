import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Advanced Comparisons", layout="wide")
st.markdown("<style>" + open("style.css").read() + "</style>", unsafe_allow_html=True)
st.title("Advanced Comparisons")

df = sns.load_dataset("titanic").dropna()

st.subheader("Age vs. Fare (Scatter)")
fig1, ax1 = plt.subplots(figsize=(8, 4))
sns.scatterplot(data=df, x="age", y="fare", hue="sex", style="survived", ax=ax1)
st.pyplot(fig1)

st.subheader("Jointplot: Class vs. Age")
st.markdown("This plot blends histogram + scatter + KDE density to explore class-age clustering.")

fig2 = sns.jointplot(data=df, x="pclass", y="age", hue="sex", kind="kde", fill=True)
st.pyplot(fig2.fig)

with st.expander(" Interpretation"):
    st.write("""
    - Survivors cluster in low-fare, younger regions — but exceptions exist.
    - KDE patterns show Class 1 had older passengers, while Class 3 was younger.
    - Great for discussing outliers and real-world exceptions in data.
    """)
