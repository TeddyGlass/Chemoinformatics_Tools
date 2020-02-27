from rdkit import Chem
from mordred import descriptors, Calculator
import argparse

params = {
    'sdf_path': './sdf/blined_humancl_95_test_1482.sdf',
    'csv_path': './csv/test.csv',
    # if '3D': calcurate 2D and 3D descriptors,
    # elif '2D': calcurate 2D descriptors
    'descriptor_type': '2D'
}


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


def calculation(mol_list, smiles_list, index_list, descriptor_type):
    if descriptor_type == '2D':
        calc = Calculator(descriptors, ignore_3D=True)
    elif descriptor_type == '3D':
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
    parser.add_argument('sdf_path')
    parser.add_argument('csv_path')
    parser.add_argument('descriptor_type', type=str,
                        help='descriptor_type str 2D or 3D')
    args = parser.parse_args()

    mol_list, smiles_list, index_list = load_sdf(args.sdf_path)
    df_dsc = calculation(mol_list, smiles_list, index_list,
                         args.descriptor_type)
    df_dsc.to_csv(args.csv_path)
    print('Columns size: ', len(df_dsc.columns))
