from load_data import *
from assumption_tests import *
from models import *

from scipy.stats import ttest_ind
from scipy.stats import ttest_rel
from matplotlib import pyplot as plt
from scipy.stats import levene, kruskal, f_oneway
from scipy.stats import shapiro
from scipy.stats import f_oneway
from scipy.stats import pearsonr
from scipy.stats import mannwhitneyu

plotting = False


def pooled_t_test(groups, assumptions=False, crosstab=False):
    """
    Calculate the pooled t-test between two groups of data.
    The test is used to compare the means of two independent groups to determine if they are significantly different from each other.

    - Null hypothesis: There is no significant difference between the means of the two groups.

    Parameters:
    - data (DataFrame): A pandas DataFrame containing the two groups of data.

    Returns:
    - t_stat (float): The calculated t-statistic.
    - p_value (float): The calculated p-value.

    Assumptions: 
    - Normality: The data in each group is approximately normally distributed.
    - Independence: The observations in each group are independent of each other.
    - Homegenity of variances: The variances of the data in each group are approximately equal.
    """

    if assumptions:
        chi2_independence_test(groups, crosstab=crosstab)
        shapiro_normality_test(groups)
        levene_variance_test(groups)

    t_stat, p_value = ttest_ind(*groups)

    return t_stat, p_value


def paired_t_test(groups, assumptions=False):
    """
    Calculate the paired t-test between two groups of data.
    The test is used to compare the means of two dependent groups when the data does not meet the assumptions of the pooled t-test.

    - Null hypothesis: There is no significant difference between the means of the two groups.

    Parameters:
    - data (DataFrame): A pandas DataFrame containing the two groups of data.

    Returns:
    - t_stat (float): The calculated t-statistic.
    - p_value (float): The calculated p-value.

    Assumptions: 
    - Normality: The data in each group is approximately normally distributed.
    - Independence: The observations within each pair are independent of each other.
    - Homogeneity of variances: The variances of the differences between the paired observations are approximately equal.
    """

    if assumptions:
        shapiro_normality_test(groups)
        levene_variance_test(groups)

    t_stat, p_value = ttest_rel(*groups)

    return t_stat, p_value


def pearson_correlation(groups, assumptions=False):
    """
    Calculate the Pearson correlation between two groups of data.

    - Null hypothesis: There is no significant correlation between the two groups.

    Assumptions: 
    - Normality: The data in each group is approximately normally distributed.
    - Independence: The observations in each group are independent of each other.

    Parameters:
    - data (DataFrame): A pandas DataFrame containing the two groups of data.

    Returns:
    - corr (float): The calculated correlation coefficient.
    """
    if assumptions:
        shapiro_normality_test(groups)

    corr, p_value = pearsonr(*groups)

    return corr, p_value


def mann_whitney_u_test(groups, assumptions=False, alternative="two-sided"):
    """
    Calculate the Mann-Whitney U test between two groups of data.
    The test is used to compare the distributions of two independent groups.
    It tells if there is a significant difference between the distributions of the two groups.

    - Null hypothesis: There is no significant difference between the distributions of the two groups.

    Parameters:
    - data (DataFrame): A pandas DataFrame containing the two groups of data.
    - group1 (str): The column name of the first group in the DataFrame.
    - group2 (str): The column name of the second group in the DataFrame.
    - assumptions (bool): If True, perform assumption tests before the Mann-Whitney U test.
                          Default is False.

    Returns:
    - U_stat (float): The calculated U statistic.
    - p_value (float): The calculated p-value.

    Assumptions:
    - Independence: The observations in each group are independent of each other.
    """

    if assumptions:
        pass

    U_stat, p_value = mannwhitneyu(*groups, alternative=alternative)

    return U_stat, p_value


def one_way_anova(groups, assumptions=False):
    """
    Calculate the one-way ANOVA between multiple groups of data.
    The test is used to compare the means of multiple dependent groups when the data does not meet the assumptions of the pooled t-test.

    - Null hypothesis: There is no significant difference between the means of the groups.

    Parameters:
    - data (DataFrame): A pandas DataFrame containing the groups of data.

    Returns:
    - F_stat (float): The calculated F-statistic.
    - p_value (float): The calculated p-value.

    Assumptions: 
    - Normality: The data in each group is approximately normally distributed.
    - Independence: The observations in each group are independent of each other.
    - Equality of variances: The variances of the groups are approximately equal.
    """

    if assumptions:
        shapiro_normality_test(groups)

    F_stat, p_value = f_oneway(*groups)

    return F_stat, p_value


def kruskal(groups, assumptions=False):
    """
    Calculate the Kruskal-Wallis test between multiple groups of data.
    The test is used to compare the medians of multiple independent groups when the data does not meet the assumptions of the one-way ANOVA.

    - Null hypothesis: There is no significant difference between the medians of the groups.

    Parameters:
    - groups (list of arrays): A list containing the groups of data.
    - assumptions (bool): Whether to perform the assumptions check. Default is False.

    Returns:
    - H_stat (float): The calculated H-statistic.
    - p_value (float): The calculated p-value.

    Assumptions: 
    - None for the Kruskal-Wallis test.
    """

    if assumptions:
        # Perform any necessary assumptions checks
        pass

    H_stat, p_value = kruskal(*groups)

    return H_stat, p_value


if __name__ == "__main__":
    pass
