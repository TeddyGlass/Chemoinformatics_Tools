from rdkit import Chem
from mordred import descriptors, Calculator
import argparse


def load_sdf(sdf_path):
    suppl = Chem.SDMolSupplier(sdf_path)
    smiles_list = []
    index_list = []
    mol_list = []
    for i in range(len(suppl)):
        mol = suppl[i]
        if mol is not None:
            smiles = Chem.MolToSmiles(mol)
            smiles_list.append(smiles)
            index_list.append(i)
            mol_list.append(mol)
    return mol_list, smiles_list, index_list,


def calculation(mol_list, smiles_list, index_list):
    calc = Calculator(descriptors)
    df = calc.pandas(mol_list)
    df = df.astype(str)
    masks = df.apply(
        lambda d: d.str.contains('[a-zA-Z]', na=False))
    df = df[~masks]
    df = df.astype(float)
    # reset index
    df['SMILES'] = smiles_list
    df['index'] = index_list
    df = df.set_index('index')
    return df


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('sdf_path', help='path of sdf')
    parser.add_argument('csv_path', help='path of destination csv')
    args = parser.parse_args()

    mol_list, smiles_list, index_list = load_sdf(args.sdf_path)
    df_dsc = calculation(mol_list, smiles_list, index_list)
    df_dsc.to_csv(args.csv_path)
    print('Columns size: ', len(df_dsc.columns))
