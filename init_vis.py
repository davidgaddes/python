"""This module gives a basic visualization of data from Lending Tree"""
import pandas as pd
from sklearn.datasets import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

NBA = pd.read_csv("nba_2013.csv")
LENDTR_Q3_17 = pd.read_csv("LoanStats_2017Q3_simplified.csv")

# sns.distplot(LENDTR_Q3_17["inc_to_pymnt"], bins=50, ax=AX1_INC_PYMNT)
# sns.boxplot(LENDTR_Q3_17["inc_to_pymnt"], ax=AX2_INC_PYMNT)
#sns.pairplot(LENDTR_Q3_17[["loan_amnt", "mths_since_last_delinq", "annual_inc"]])

def hist_boxwisk(var_name, bin_num, x_lab, y_lab):
    """This function generates a hist, box and whiskers plot in a fig"""
    fig = plt.figure()
    sns.set_style("darkgrid",{"axes.facecolor":".9"})
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    ax1.set(xlabel=x_lab, ylabel=y_lab)
    ax2.set(xlabel=x_lab, ylabel=y_lab)
    sns.distplot(var_name, bins=bin_num, ax=ax1)
    sns.boxplot(var_name, ax=ax2)
hist_boxwisk(LENDTR_Q3_17['annual_inc'], 50, 'dollars', 'amount')
hist_boxwisk(LENDTR_Q3_17['loan_amnt'], 50, 'dollars', 'amount')
hist_boxwisk(LENDTR_Q3_17['dti'], 50, 'debt to income', 'amount')
hist_boxwisk(LENDTR_Q3_17['inc_to_pymnt'], 50, 'income to payment', 'amount')
hist_boxwisk(LENDTR_Q3_17['sub_grade_num'], 35, 'Lending Club Rating', 'amount')
plt.show()
