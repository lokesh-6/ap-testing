import streamlit as st
from statsmodels.stats.proportion import proportions_ztest
import numpy as np

# Define the ab_test function
def ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level):
    # Convert confidence level to alpha
    alpha = 1 - (confidence_level / 100)
    # Calculate the number of successes and the number of observations for each group
    successes = np.array([treatment_conversions, control_conversions])
    observations = np.array([treatment_visitors, control_visitors])
    # Perform the two-proportion Z-test
    stat, p_value = proportions_ztest(count=successes, nobs=observations, alternative='two-sided')
    # Determine the result based on the p-value and alpha
    if p_value < alpha:
        if stat > 0:
            result = "Experiment Group is Better"
        else:
            result = "Control Group is Better"
    else:
        result = "Indeterminate"
    return result

# Streamlit app UI
st.title('A/B Test Calculator')

# User inputs
st.sidebar.header('User Input Parameters')
control_visitors = st.sidebar.number_input('Control Group Visitors', min_value=0, value=1000)
control_conversions = st.sidebar.number_input('Control Group Conversions', min_value=0, value=50)
treatment_visitors = st.sidebar.number_input('Treatment Group Visitors', min_value=0, value=1000)
treatment_conversions = st.sidebar.number_input('Treatment Group Conversions', min_value=0, value=60)
confidence_level = st.sidebar.selectbox('Confidence Level', [90, 95, 99])

# Perform A/B test and display the result
result = ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level)
st.write(f"Result: {result}")
