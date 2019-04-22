# THIS CODE IS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING
# A TUTOR OR CODE WRITTEN BY OTHER STUDENTS - Shayan Jiwani, Sam Larson, Safa Tinaztepe

import pandas as pd
import seaborn as sb
import statsmodels.api as sm
import matplotlib.pyplot as plt
from Final_Project import preproc


# Returns an Ordinary Least Squares regression analysis of 2 variables
# Graphs histograms of the probability distribution functions of x and y variables
def linear_regression(df):
    frame = df
    x, y = frame.iloc[:, 0:1], frame.iloc[:, 1:2]

    model = sm.OLS(y, x).fit()
    print(model.summary())
    sb.set(color_codes=True)
    sb.distplot(x)
    plt.show()
    sb.distplot(y)
    plt.show()


data_path = 'data/fifa.csv'
fifa_df = preproc.load_data(data_path=data_path)

# Example of x,y columns to graph probability distribution functions and linearly regress via OLS
reg_df = pd.DataFrame(columns=[fifa_df['SlidingTackle'], fifa_df['Wage']])
ayy = fifa_df[['GKHandling', 'Wage']].copy()
yoo = ayy

# preproc.full_print(ayy)
linear_regression(yoo)

