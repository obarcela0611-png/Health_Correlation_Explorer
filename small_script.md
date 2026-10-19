# Small Scripts

## Script 1: Load the Dataset

This script loads the health dataset using pandas.

```python
import pandas as pd

health_data = pd.read_csv("nhanes_health.csv")
```

## Script 2: Filter Participants

This script filters participants based on their selected sex and age range.

```python
filtered_data = health_data[
    (health_data["sex"] == selected_sex) &
    (health_data["age"] >= age_range[0]) &
    (health_data["age"] <= age_range[1])
]
```

## Script 3: Calculate Correlations

This script calculates Pearson or Spearman correlations using numeric variables.

```python
numeric_data = filtered_data.select_dtypes(include="number")

correlation = numeric_data.corr(method=method)
```

## Script 4: Calculate Sample Sizes

This script calculates the number of valid observations for each pair of variables.

```python
sample_sizes = numeric_data.notna().astype(int).T.dot(
    numeric_data.notna().astype(int)
)
```

## Script 5: Create a Correlation Heatmap

This script creates a heatmap with a fixed color scale between -1 and 1.

```python
import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 8))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    ax=ax
)

st.pyplot(fig)
```

## Script 6: Create a Scatterplot

This script creates a scatterplot with a regression line.

```python
fig, ax = plt.subplots()

sns.regplot(
    data=filtered_data,
    x=x_variable,
    y=y_variable,
    ax=ax
)

st.pyplot(fig)
```
