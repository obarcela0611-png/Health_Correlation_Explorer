import streamlit as st
import pandas as pd
import seaborn as sns

# Load the health data from the CSV file.
health_data = pd.read_csv("nhanes_health.csv")


# Add a title and a short description of the dataset.
st.title("Health Correlation Explorer")
st.write(
    "This dataset contains participant health measurements, including age, "
    "BMI, blood pressure, cholesterol, sleep, and sedentary time."
)


# Create filters
st.subheader("Filter Participants")

# Filter by sex
sex = st.selectbox("Select Sex", ["All", "Male", "Female"])

# Filter by age
age_range = st.slider(
    "Select Age Range",
    int(health_data["age"].min()),
    int(health_data["age"].max()),
    (int(health_data["age"].min()), int(health_data["age"].max())),
)

# Apply filters
filtered_data = health_data.copy()

if sex != "All":
    filtered_data = filtered_data[filtered_data["sex"] == sex]

filtered_data = filtered_data[
    (filtered_data["age"] >= age_range[0]) & (filtered_data["age"] <= age_range[1])
]

# Display participant count
st.write("Number of participants:", len(filtered_data))

# Display the first five rows so we can preview the data.
st.subheader("Dataset Preview")
st.dataframe(filtered_data.head())

# Select numeric columns for correlation analysis
numeric_data = filtered_data.select_dtypes(include="number")

# Select correlation method
st.subheader("Correlation Method")

method = st.selectbox("Select Method", ["pearson", "spearman"])

# Calculate correlations
correlation = numeric_data.corr(method=method)

# Calculate sample sizes for each pair of variables
sample_sizes = numeric_data.notna().astype(int).T.dot(numeric_data.notna().astype(int))

# Display correlation and sample size together
correlation_labels = correlation.copy().astype(str)

for row in correlation.index:
    for col in correlation.columns:
        correlation_labels.loc[row, col] = (
            f"{correlation.loc[row, col]:.2f}\n" f"N={sample_sizes.loc[row, col]}"
        )

# Display the correlation table
st.subheader("Correlation Matrix")
st.dataframe(correlation_labels)

import matplotlib.pyplot as plt

# Create a correlation heatmap
st.subheader("Correlation Heatmap")

fig, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(
    correlation,
    annot=correlation_labels,
    fmt="",
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    ax=ax,
)

st.pyplot(fig)

# Allow users to select two variables
st.subheader("Explore Health Variables")

variables = numeric_data.columns.tolist()

x_variable = st.selectbox("Select X variable", variables)
y_variable = st.selectbox("Select Y variable", variables, index=1)

# Create a scatterplot
st.subheader("Scatterplot")

fig, ax = plt.subplots()

sns.scatterplot(data=filtered_data, x=x_variable, y=y_variable, ax=ax)

# Add a trend line
sns.regplot(data=filtered_data, x=x_variable, y=y_variable, scatter=False, ax=ax)

st.pyplot(fig)

# Calculate the selected correlation
r = filtered_data[x_variable].corr(filtered_data[y_variable], method=method)

# Count participants with valid values for both variables
n = filtered_data[[x_variable, y_variable]].dropna().shape[0]

# Display correlation and sample size
st.write(method.capitalize(), "correlation: r =", round(r, 3), "| N =", n)
