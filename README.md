# Chemoinformatics_Tools

# Visualization
機械学習による予測根拠を可視化するプログラム(ノートブック形式)
決定木系のアルゴリズムから得られる feature importance に基づき原子の重要度を示したweightを取得します.  
weghtは化合物の所有する部分構造に機械学習モデルから得られたfeature importanceを割り当て, それを部分構造上に存在する原子数で平均化したもので表されます.  
赤は正, 青は負の寄与を表しています. feature importanceを用いた場合は非負であるため視認性が下がる欠点があります.
<div align="center">
  <img width="537" alt="image" src="https://user-images.githubusercontent.com/39366279/108008230-3e94f000-7043-11eb-8c15-9b849a36a300.png">
</div>
