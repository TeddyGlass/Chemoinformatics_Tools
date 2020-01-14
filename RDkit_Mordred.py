from rdkit import Chem
from mordred import descriptors, Calculator
import pandas as pd
import numpy as np

class Mordred:
    
    def __init__(self):
        self.mols = []
        self.index = []

    def load_sdf(self, file):
        suppl = Chem.SDMolSupplier(file)
        self.index = []
        self.mols = []
        for i in range(len(suppl)):
            if suppl[i] is not None:
                self.index.append(i)
                self.mols.append(suppl[i])
    
    def calculation(self):
        # calculaton of descriptors
        calc = Calculator(descriptors)
        # clean up df
        df_descriptors =  calc.pandas(self.mols)
        df_descriptors = df_descriptors.astype(str)
        masks = df_descriptors.apply(lambda d: d.str.contains('[a-zA-Z]' ,na=False))
        df_descriptors = df_descriptors[~masks]
        df_descriptors = df_descriptors.astype(float)
        # reset index 
        df_descriptors['index'] = self.index
        df_descriptors = df_descriptors.set_index('index')
        return df_descriptors

def main():
    file_list = ['humanCL(3DMol)1387_train_1482.sdf', 'blined_humancl_95_test_1482.sdf']
    df_list = []
    for file in file_list:
        mord = Mordred()
        mord.load_sdf(file)
        descriptor = mord.calculation()
        df_list.append(descriptor)
    return df_list