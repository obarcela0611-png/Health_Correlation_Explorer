# Development Plan - Health Correlation Explorer

## Project Goal

I want to build an app that explores correlations between health measurements using the provided dataset. The application should include filters, a dataset preview, correlation calculations, a correlation heatmap, and scatterplots.  

## Step 1: Load and Preview the Dataset

- Import Streamlit, pandas, Seaborn, and Matplotlib.
- Load the nhanes_health.csv dataset using pandas.
- Display the first five rows of the dataset.
- Display the number of participants.

## Step 2: Create Interactive Filters

- Add a sidebar with a sex dropdown menu.
- Add an age range slider.
- Filter the dataset based on the selected sex and age range.
- Update the participant count, correlation calculations, heatmap, and scatterplot when filters change.

## Step 3: Calculate Correlations

- Select numeric variables from the dataset.
- Allow users to choose Pearson or Spearman correlation.
- Calculate the correlation matrix using pandas.
- Calculate the sample size for each variable pair.
- Display correlation coefficients and sample sizes in a table.

## Step 4: Create the Correlation Heatmap

- Allow users to select which numeric variables appear in the heatmap.
- Use Seaborn to generate the correlation heatmap.
- Display the correlation coefficient and sample size in each cell.
- Keep the heatmap color scale fixed between -1 and 1.

## Step 5: Create the Scatterplot

- Allow users to select X and Y variables.
- Generate a scatterplot using Seaborn.
- Color the points based on systolic blood pressure below 130 or 130 and higher.
- Add a regression trend line.
- Display the correlation coefficient and sample size for the selected variables.

## Step 6: Test and Verify the Application

- Confirm that the dataset loads correctly.
- Test the sex and age filters.
- Verify that the correlation matrix and heatmap update correctly.
- Confirm that the scatterplot displays the correct variables and blood pressure groups.
- Independently calculate correlations using pandas.
- Compare the pandas results with the Streamlit application.
- Document the results in verification.md.

## Step 7: Submit the Project

- Save the completed application in app.py.
- Document the AI prompts in prompts.md.
- Document code examples in small_script.md.
- Record testing results in verification.md.
- Upload the project files to GitHub.
- Deploy the Streamlit application and submit the required links.

