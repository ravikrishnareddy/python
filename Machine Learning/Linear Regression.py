import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.preprocessing import PolynomialFeatures
import statsmodels.formula.api as smf
import seaborn as sns

boston = load_boston()

boston = pd.DataFrame(data = np.c_[boston['data'], boston['target']], columns = list(boston['feature_names'])+['medv'])
boston.head()
boston.shape
boston.info()
boston.describe()

lm_fit = smf.ols('medv ~ LSTAT', data = boston).fit()
lm_fit.summary()

lm_fit.predict(pd.DataFrame(data = [5, 10, 15], columns = ["LSTAT"]))

sns.regplot(x = 'LSTAT', y = 'medv', data = boston, ci = False)

# Get outliers
outliers = lm_fit.outlier_test()

# Get leverage statistic
hatvalues = lm_fit.get_influence().hat_matrix_diag

# Get standardized residuals
rstandard = lm_fit.get_influence().resid_studentized_internal

# Get studentized residuals
rstudent = lm_fit.get_influence().resid_studentized_external

sns.scatterplot(x = hatvalues, y = abs(rstudent))

# Plot residuals against fitted values
sns.scatterplot(x = lm_fit.fittedvalues, y = lm_fit.resid)

# Plot studentized residuas against fitted values
sns.scatterplot(x = lm_fit.fittedvalues, y = abs(lm_fit.get_influence().resid_studentized_external))

# Plot leverage statistic again fitted values
sns.scatterplot(x = lm_fit.fittedvalues, y = lm_fit.get_influence().hat_matrix_diag)


###
# Residual plot confirms a non-linear relationship

lm_fit_poly = smf.ols('medv ~ np.vander(LSTAT, 5)', data = boston).fit()
lm_fit_poly.summary()
