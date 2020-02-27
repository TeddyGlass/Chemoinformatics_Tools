# Mordred記述子テーブルの自動生成プログラム

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
① Descriptor.pyのparamsを設定する<br>
* sdf_path: 参照するsdfファイルのパス ( str )
* csv_path: 保存するcsvファイルのパス ( str )
* 算出する記述子のタイプ ( str '2D' or '3D' )
※3Dに設定した場合は2D記述子と３D記述子の両方が算出される.<br>

② PythonファイルDescriptor.pyを実行する.<br>