# Chemoinformatics_Tools
ケモインフォマティクス関連のツールを集約させたリポジトリ
<br>

# 1 Visualization of Prediction Basis from ML Model
### ディレクトリ名
```visualiza```  
### 概要
機械学習による予測根拠を可視化するプログラム(ノートブック形式).  
決定木系のアルゴリズムから得られる feature importance に基づき原子の重要度を示したweightを取得します.  
化合物の所有する部分構造に機械学習モデルから得られたfeature importanceを割り当て, それを部分構造上に存在する原子数で平均化することでweightが算出されます.  
weightの値に基づき化学構造に色を割り当てます.  
赤は正, 青は負の寄与を表しています. 
しかし, feature importanceを用いた場合は, weightが非負であるため視認性が下がる欠点があります.
<div align="center">
  <img width="537" alt="image" src="https://user-images.githubusercontent.com/39366279/108008230-3e94f000-7043-11eb-8c15-9b849a36a300.png">
</div>
### サンプルデータ
[Hansen et al.](https://pubs.acs.org/doi/abs/10.1021/ci900161g) が提供する化合物の変異原性データベースを用いました.
