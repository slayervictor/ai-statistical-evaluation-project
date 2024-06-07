import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency, shapiro, levene, bartlett


def chi2_independence_test(groups, crosstab=False):
    """
    Perform a Chi-Square test for independence on the given data.

    - Null-hypothesis: The two variables are independent, i.e. there is no association between them. 
    The alternative hypothesis is that the two variables are dependent.

    Parameters:
        data (DataFrame): The input DataFrame containing the data.
        group1 (str): The name of the first grouping variable.
        group2 (str): The name of the second grouping variable.

    Assumptions:
    - Independence: The observations in the data should be independent of each other.
    - Random Sampling: The data should be obtained through a random sampling process.
    - Expected Cell Frequencies: The expected cell frequencies in the contingency table should be at least 5.

    Returns:
        None
    """

    if not crosstab:
        # Create a contingency table from the DataFrame
        table = pd.crosstab(*groups)
    else:
        table = groups

    # Perform the Chi-Square test for independence
    chi2, p_value, dof, expected = chi2_contingency(table)

    # Print the results
    print("Chi-Square test results:")
    print("Chi-Square test statistic:", chi2)
    print("p-value:", p_value)
    print("Degrees of freedom:", dof)
    print("Expected frequencies:\n", expected)


def shapiro_normality_test(groups):
    """
    The Shapiro-Wilk test is a statistical test used to assess the normality assumption for a given dataset. 

    - Null-hypothesis: The population from which the data is sampled follows a normal distribution.

    Assumptions:
    - Independence: The observations in the dataset should be independent of each other. 
    This means that the value of one observation should not be influenced by or dependent on the value of another observation.

    - Random Sampling: The dataset should be obtained through a random sampling process, 
    where each observation has an equal chance of being included in the sample.

    - Normal Distribution: The Shapiro-Wilk test assumes that the population from which the data is sampled follows a 
    normal distribution.

    - Moderate to large sample sizes (typically n > 5). 


    Parameters:
        data (DataFrame): The data containing the groups for the normality test.
        group1 (str): The column name of group 1.
        group2 (str): The column name of group 2.

    Returns:
        None
    """

    # Perform normality test using Shapiro-Wilk test
    p_values = []
    for index, group in enumerate(groups):
        shapiro_stat_group, shapiro_p_value_group = shapiro(group)
        p_values.append(shapiro_p_value_group)

    return p_values


def levene_variance_test(groups):
    """
    The Levene's test is a statistical test used to assess the equality of variance between two or more groups in a dataset. 
    - Null-hypothesis: The population variances of the groups are equal.

    Assumptions:
    - Independence: The observations in the dataset should be independent of each other. 
    This means that the value of one observation should not be influenced by or dependent on the value of another observation.

    - Random Sampling: The dataset should be obtained through a random sampling process, 
    where each observation has an equal chance of being included in the sample.
    """

    # Perform variance test using Levene's test
    levene_stat, levene_p_value = levene(*groups)
    '''
    print("Levene's test:")
    print("Test statistic:", levene_stat)
    print("p-value:", levene_p_value)
    print()
    '''

    return levene_stat, levene_p_value


def bartlett_variance_test(groups):
    """
    The Bartlett's test is a statistical test used to assess the equality of variance between two or more groups in a dataset. 
    - Null hypothesis: The population variances of the groups are equal.

    Assumptions:
    - Independence: The observations in the dataset should be independent of each other. 
      This means that the value of one observation should not be influenced by or dependent on the value of another observation.

    - Random Sampling: The dataset should be obtained through a random sampling process, 
      where each observation has an equal chance of being included in the sample.
    """

    # Perform variance test using Bartlett's test
    bartlett_stat, bartlett_p_value = bartlett(*groups)

    print("Bartlett's test:")
    print("Test statistic:", bartlett_stat)
    print("p-value:", bartlett_p_value)
    print()
