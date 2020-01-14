from rdkit import Chem
from mordred import descriptors, Calculator
import pandas as pd
import numpy as np

class PreProcessing:
    
    def missing_descriptors(self, df_X, threshold):
        cols = df_X.columns
        drop_cols_list = []
        for i in range(len(cols)):
            col = df_X.iloc[:,i]
            value = col.isnull().sum()
            if value > threshold:
                drop_cols_list.append(cols[i])
        return drop_cols_list
    
    def var0_descriptors(self, df_X):
        cols = df_X.columns
        drop_cols_list = []
        for i in range(len(cols)):
            col = df_X.iloc[:,i]
            value = col.var()
            if value == 0:
                drop_cols_list.append(cols[i])
        return drop_cols_list
    
    def search_highly_correlated_variables(self, df_X, threshold_of_r):
        """
        search variables whose absolute correlation coefficient is higher than threshold_of_r
        Parameters
        ----------
        x: numpy.array or pandas.DataFrame
        threshold_of_r: float
            threshold of correlation coefficient
        Returns
        -------
        highly_correlated_variable_numbers : list
            the number of variables that should be deleted
        """
        x = df_X
        x = pd.DataFrame(x)
        r_in_x = x.corr()
        r_in_x = abs(r_in_x)
        for i in range(r_in_x.shape[0]):
            r_in_x.iloc[i, i] = 0
        highly_correlated_variable_numbers = []
        for i in range(r_in_x.shape[0]):
            r_max = r_in_x.max()
            r_max_max = r_max.max()
            if r_max_max >= threshold_of_r:
                print(i + 1)
                variable_number_1 = np.where(r_max == r_max_max)[0][0]
                variable_number_2 = np.where(r_in_x.iloc[:, variable_number_1] == r_max_max)[0][0]
                r_sum_1 = r_in_x.iloc[:, variable_number_1].sum()
                r_sum_2 = r_in_x.iloc[:, variable_number_2].sum()
                if r_sum_1 >= r_sum_2:
                    delete_x_number = variable_number_1
                else:
                    delete_x_number = variable_number_2
                highly_correlated_variable_numbers.append(delete_x_number)
                r_in_x.iloc[:, delete_x_number] = 0
                r_in_x.iloc[delete_x_number, :] = 0
            else:
                break

        return list(x.columns[highly_correlated_variable_numbers])
    