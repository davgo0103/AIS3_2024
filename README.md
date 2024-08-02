# 說明

### 下載
- dwn1.py 第一支自動下載惡意軟體的程式
- dlFinal.py 最終版自動下載程式解壓後自動使用capa分析惡意程式

### 分析轉換
- toJSON.py 把capa分析後的txt文字檔案轉換為JSON格式

### 比較
- sim.py 分析初版，使用JSON格式的capa報告進行比較
  - ![image](https://github.com/user-attachments/assets/48b0b984-23f3-4a8a-b958-6aee8d98bf6b)
- simnum.py 分析第二版，使用轉換為二進制格式的capa報告進行比較
- simclus.py 分析最終版把畫圖的方法分離出來，不然每次都跑好久
  - draw.py 畫圖用的，只能搭配simclus.py產生的檔案畫圖
 
# 使用
- 先下載惡意軟體後，再進行分析和比較畫圖。
- 大部分的程式中都有參數可以調整或是選擇要執行、選擇的內容
