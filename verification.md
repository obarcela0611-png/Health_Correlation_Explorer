# Verification

## Test 1: Application Launch
- Ran the Streamlit application successfully.
- Confirmed that the application opens in the browser without errors.
- Result: PASS

## Test 2: Dataset Loading
- Loaded the nhanes_health.csv dataset.
- Confirmed that the first five rows display correctly.
- Result: PASS

## Test 3: Correlation Matrix
- Calculated Pearson correlations between numeric health variables.
- Confirmed that BMI and waist circumference have a correlation of approximately 0.903.
- Result: PASS

## Test 4: Correlation Heatmap
- Generated a heatmap showing correlations between numeric variables.
- Confirmed that the heatmap displays correctly.
- Result: PASS

## Test 5: Interactive Scatterplot
- Selected BMI as the X variable and waist circumference as the Y variable.
- Confirmed that the scatterplot updates when variables are changed.
- Result: PASS

## Test 6: Participant Filters
- Added filters for sex and age range.
- Selected Female participants between ages 42 and 80.
- Confirmed that the participant count changed to 1,482.
- Confirmed that the correlation matrix updated.
- Result: PASS

## Test 7: Scatterplot Trend Line
- Added a regression line to the scatterplot.
- Confirmed that the line displays correctly.
- Result: PASS

## Test 8: Correlation Methods
- Tested Pearson and Spearman correlations.
- Confirmed that both methods run without errors.
- Result: PASS

## Test 9: Heatmap Color Scale
- Set the heatmap color scale between -1 and 1.
- Confirmed that the color scale displays correctly.
- Result: PASS

### Test: Participant Filters

I tested the participant filters by selecting Female and
changing the age range to 42–80.

The number of participants decreased from 4,433 to 1,482.

The correlation heatmap updated automatically based on
the filtered data. The correlation between BMI and waist
circumference changed from approximately 0.90 to 0.91.

The heatmap continued displaying the correlation
coefficients (R) and sample sizes (N), with the color
scale fixed between -1 and 1.

Result: PASS

## Independent Pandas Verification

The correlation results from the Streamlit application were compared with calculations performed independently using pandas.

| Variable X | Variable Y | Method | App r | Pandas r | App N | Pandas N |
|---|---|---|---|---|---|---|
| age | bmi | Pearson | -0.012 | -0.012 | 4433 | 4433 |
| age | bmi | Spearman | 0.015 | 0.015 | 4433 | 4433 |

The results matched, confirming that the application correctly calculates the Pearson correlation coefficient and sample size for this variable pair.