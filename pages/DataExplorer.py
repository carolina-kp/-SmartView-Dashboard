import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(layout="wide")
st.title("📊 Data Explorer")

df = sns.load_dataset("titanic").dropna()

# Filters to compare subgroups
st.sidebar.header("🎯 Filter Data")
gender = st.sidebar.selectbox("Select Gender", ["all"] + sorted(df["sex"].unique()))
pclass = st.sidebar.selectbox("Select Passenger Class", ["all"] + sorted(df["pclass"].unique()))

filtered_df = df.copy()
if gender != "all":
    filtered_df = filtered_df[filtered_df["sex"] == gender]
if pclass != "all":
    filtered_df = filtered_df[filtered_df["pclass"] == pclass]

st.write(f"### Filtered Data Preview ({len(filtered_df)} rows)")
st.dataframe(filtered_df.head())

st.write("### 🔗 Correlation Heatmap (Numerical Features)")

numeric = filtered_df.select_dtypes(include='number')
corr = numeric.corr()

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🔍 Standard Heatmap")
    fig1, ax1 = plt.subplots(figsize=(7, 4))
    sns.heatmap(corr, annot=True, cmap="crest", ax=ax1)
    st.pyplot(fig1)

with col2:
    st.markdown("#### 🧮 Survival vs. Features")
    fig2, ax2 = plt.subplots(figsize=(7, 4))
    sns.barplot(data=filtered_df, x="sex", y="survived", hue="pclass", ax=ax2)
    st.pyplot(fig2)

# Explain biases & decisions
with st.expander("ℹ️ Why Use Heatmaps?"):
    st.write("""
    Heatmaps enhance pattern recognition using **preattentive color processing**.
    This supports users in instantly spotting anomalies or trends (e.g., age vs. survival).
    """)

with st.expander("🧠 Cognitive Bias Prevention"):
    st.write("""
    Filters help users test assumptions rather than rely on defaults (reduces **anchoring** and **confirmation bias**).
    Separate views encourage **comparative analysis** without mental overload.
    """)
