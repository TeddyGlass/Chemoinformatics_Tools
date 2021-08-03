# Chemoinformatics_Tools

1. [機械学習QSARモデルの予測根拠可視化](#anchor1)
2. [Mordred記述子算出](#anchor2)

<br>
<br>


<a id="anchor1"></a>
# 1 Visualization of prediction basis from finger print based machine learning model  
The aim of this code is to improve interpretability of QSAR(Quantitative Structure-Activity Relationships) model which uses machine learning based on fingert print.
Applying this code, you can map colors onto the chemical structure according to contribution for the prediction, it enable us to interptet partial structures contributing to the prediction of pharmacological, physicochemical, and toxicological activities.  
Here we show a simple implementation using RandomForest which is a typical CART （Classification and Regression Tree） algorithm. Note that this interpretation algrithm can be applied to other machne learning algorithms, e.g. ,LightGBM, XGBoost and Neural Network (which is applied Permutation Importance to get feature importance), is theoretically possible. Therefore, this interpretation algrithm can be used for general purpose. 
In this implementation, colors are assigned to chemical structures based on the weight calculated from the importance of features obtained from the machine learning model.Weight can be obtained by the following simple calculation.
 - Fingerprintの各ビットに関するFeature importanceを取得  
 - 各ビットに対応する部分構造上の原子数を用いてFeature importanceを平均化  
 <br>
 以上の処理によりWeightが算出され,Weightの値に基づき化学構造に色が割り当てられます.

<div align="center">
  <img width="700" alt="chem" src="https://user-images.githubusercontent.com/39366279/108010711-d77a3a00-7048-11eb-85c5-a9bdb294d94c.png">
  <img width="700" alt="table" src="https://user-images.githubusercontent.com/39366279/108010752-f082eb00-7048-11eb-9e1c-cf0b779b9531.png">
</div>
<br>

### サンプルデータ
[Hansen et al.](https://pubs.acs.org/doi/abs/10.1021/ci900161g) が提供する化合物の変異原性データベースを用いました.
<br>
<br>


<a id="anchor2"></a>
# 2 Mordred Calculator

### ディレクトリ名
```descriptors``` 

#### 概要
三次元化した化合物のsdfファイルから, Mordred記述子を算出しcsvファイルを出力するプログラム<br>
<br>

#### 機能
記述子にはMordredの記述子を使用.<br>
2D, 3D記述子の両者を算出<br>
※ FingerPrint等の算出にも対応したバージョンにアップグレード予定<br>
※ RDKitにはロードに失敗する化合物が存在する. そのような化合物の記述子計算はスキップされ行から外される.<br>
※ 入力化合物数と出力化合物数が異なる場合があるため, 出力csvファイルのindexとSMILESを参照する必要がある.<br>

以下の環境での動作確認済です.<br>

**環境**
* Miniconda3
* Python 3.7.4<br>

 **パッケージ**<br>

 *・RDkit*<br>
 ```
 $ conda install -c conda-forge rdkit
 ```
 *・Mordred*<br>
```
conda install -c mordred-descriptor mordred
```
 <br>

#### 使用方法
コマンドラインからDescriptor_ver1.0.1.pyを実行する.<br>
引数は以下のように設定する
* sdf_path: 参照するsdfファイルのパス
* csv_path: 保存するcsvファイルのパス
* 算出する記述子のタイプ ( 2D or 3D )<br>
※3Dに設定した場合は2D記述子と３D記述子の両方が算出される.<br>

#### 実行例
```
$ python Descriptor_ver1.0.1.py test.sdf test.csv 3D
```
