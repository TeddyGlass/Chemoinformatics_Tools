# Chemoinformatics_Tools
ケモインフォマティクス関連のツールを集約させたリポジトリ  

1. [機械学習QSARモデルの予測根拠可視化](#anchor1)
2. [Mordred記述子算出](#anchor2)

<br>
<br>


<a id="anchor1"></a>
# 1 Visualization of Prediction Basis from ML Model


### ディレクトリ名
```visualization```  


### 概要

<div align="center">
  <img width="700" alt="title" src="https://user-images.githubusercontent.com/39366279/108031694-a152af80-7074-11eb-849c-f30ecaa5fb47.png">
</div>

フィンガープリントを特徴量とした機械学習QSARモデルの予測根拠を可視化するプログラム(ノートブック形式).  
決定木系のアルゴリズムから得られる feature importance に基づき原子の重要度を示したweightを取得します.  
化合物の所有する部分構造に機械学習モデルから得られたfeature importanceを割り当て, それを部分構造上に存在する原子数で平均化することでweightが算出されます.  
weightの値に基づき化学構造に色を割り当てます.  
赤は正, 青は負の寄与を表しています. 
しかし, feature importanceを用いた場合は, weightが非負であるため視認性が下がる欠点があります.

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
