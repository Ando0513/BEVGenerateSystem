# BEVGenerateSystemについて

<p>緯度と経度に対応するGoogleMapによる航空写真を入手します。各種Buttonは消せません。いまのところ。</p>
<img src=preview.png width=50%>

# Requirement
<p>for pip</p>

- selenium == 4.15.2
<p>as driver</p>

- chrome
- chromedriver


# 初回セットアップ
<p>BEVGenerateSystemではSeleniumを使用します。Seleniumは、Chrome上の操作を自動化するプロジェクトです。
したがって、Chromeと対応するChromeドライバをインストールする必要があります。</p>
<p>Chrome</p>

[https://www.google.com/intl/ja_jp/chrome/](https://www.google.com/intl/ja_jp/chrome/)

<p>ChromeDriver</p>

[https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

<p>ここから、Chromeに対応するバージョン、ＯＳを選びます。</p>
<p>＊私の環境だと、chromeバージョンは115より新しいので、

[https://googlechromelabs.github.io/chrome-for-testing/#stable](https://googlechromelabs.github.io/chrome-for-testing/#stable) からインストールできます。</p>

<p>ChromeDriverのリンクをgoogle.pyのCHROMEDRIVERで指定します。</p>

```
CHROMEDRIVER = 'C:/Users/andoy/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'  #こ↑こ↓  
```
# 使い方　for v0
<p>取得したいBEV画像が位置する、緯度、経度を用意します。
それぞれ緯度をlat,経度をlogのリストに追加します。
python google.pyを打ち込めば動くはずです。</p>

google.py
```
lat = [37.3618461,37.3490862,37.3545187] #こ↑こ↓に緯度　と
lon = [140.3679248, 140.3627885,140.3647392] #こ↑こ↓に経度　を追加
```

terminal
```
$ python3 google.py
```
output
```
result1.png
result2.png
result3.png
...
```
