# 2024 AIS3 B8專題

<!-- 基於聚類分析技術的惡意程式變體辨識方法研究 -->
<!-- 簡報https://docs.google.com/presentation/d/1mOfBjBmEhjUG6e3FxfknjdLlehB1IKIz/edit?usp=sharing&ouid=109894482775983337768&rtpof=true&sd=true -->
❇️✳️✴️🟢✅☑️🔺🔶

# 現在目標
- [x] 透過爬蟲抓MalwareBazaar上的病毒樣本
- [x] 寫個腳本自動跑capa分析病毒
- [x] 了解jaccard index的流程
- [x] 選擇要用capa分析報告中的哪些數值
    🔺capa抓的特徵不太適合做比較
- [x] 病毒分析報告->能丟到jaccard index格式
- [x] 透過jacaard將資料分析出相似度
    🔺不確定怎麼配置jacaard才能分析的比較準
- [ ] jacca結果化成一個圖
- [ ] 確認相關度量化要用的演算法
- [ ] 畫出圖示表達變體彼此關聯性

# 流程簡介
1. 把wannacry及其變體丟到capa
2. 提取capa分析報告丟到jaccard index分析相關度
3. 判斷該變體與本體的相似度

## 可做延伸
- 換算法
- 更多種病毒
- 與其他病毒做比對 看結果
- 
- 

# 8/1助教討論
## 到目前進度
- 寫了腳本自動抓MalwareBazaar的病毒
- 寫了腳本自動跑capa分析病毒並匯入txt文件中
- 將capa分析出來的報告提取ATT&CK and MBC
- 將ATT MBC做成array分析 [1,0,0,1,1,0,1,0,0,0,0,1]
- 把資料丟到jaccard比對相似度
- 根據相似度做成圖片


## 後續延伸
- 跟非勒索軟體、勒索軟體作比對看看 看數值的差距 
- [x] 圖片改相似度矩陣
- 找別的算法 看畫出來得圖有沒有不一樣
    - 一維?
- [x] 交叉比對 
- plus升級版本 只吃變體 分更開
- LLM吃分析array 
    - 萊姆

- 抱歉私心- 挑戰bypass掉我們的分析系統
    - 因為分析存在漏洞
        - 多使用一些不相關的內容 來嘗試欺騙capa多分析出摸到的功能



# 8/2
想問助教的問題
- 可能喂LLM嗎


---
- 變體圖形化分隻
    - STIX圖表?
- 下載最新變體並直接分析
- 不使用jaccard，而是改自己用AI去分析看看
    - 早上上半堂ice講的分類模型?
- 自己刻一個相似的變體丟去看相似度
    - 可以結合capa是如何分析的，嘗試bypass檢測看看
- 把更多類型的病毒透過capa分析，透過ML、DL來分析報告，判斷他屬於哪種病毒類型


::: success
## 可以做的事
> 任何想到該做的事
#### 雜 
- 把變體們的sha去Virus total 上查查看
#### 資料前處理/比對
- 上標籤
- 可 先找出真的很像的變體 (搞不好你可幫忙)
- 想 要怎麼把分析出來的全部投影到一個二維的圖上
- [ing] 串chatGPT API

#### 可以讓有分類權重跟沒有分類權重的結果都去對比一次相似度

**說明學到什麼**
#### :D
:::



## 貢獻(大致
- 吳玥儒(萊姆)
    - jaccard分析
    - 
<!-- 
1.把wannacry檔案分成 空 <10kb >10kb
2.
-->
- 鄭宇兩(貝坦)
    - 寫powershell腳本跑capa分析惡意軟體
    - 分析capa概念
    - 篩選capa特徵
- 曹凱翔(l3obo)
    - jaccard分析
    - 
- 蔡士煒(小蔡)
    - 統整步驟
    - 抓惡意軟體爬蟲撰寫
    - 


---
# 惡意程式變體偵測專題計畫

## 1. 主題概述
**主題**：惡意程式變體偵測

**目標**：
1. 針對惡意軟體（如Emotet、Wannacry）進行變體偵測。
2. 使用capa工具分析特徵，並對比變體和原始樣本的相似度。

## 2. 具體步驟
### 2.1 惡意軟體樣本選擇
- 針對Emotet木馬和Wannacry勒索軟體，蒐集多個樣本及其變體。

### 2.2 使用capa進行分析
- 下載並配置capa工具。
- 將惡意軟體樣本和變體丟入capa，生成功能特徵報告。

### 2.3 特徵比對
- 使用相似度演算法（如Jaccard index）比較原始樣本和變體的capa報告。
- 將特徵向量投放到向量空間中，評估樣本之間的相似度。

### 2.4 變體創建與測試
- 參考開源惡意軟體代碼，創建自製變體。
- 將自製變體丟入capa，生成報告並與原始變體進行比對。

### 2.5 結果分析與報告
- 分析相似度比對結果，找出最接近原始樣本的變體。
- 總結研究成果，撰寫報告。

## 3. 詳細步驟

### 3.1 蒐集惡意軟體樣本
- 利用安全研究平台或開源數據庫（如[VirusTotal](https://www.virustotal.com/)、[MalwareBazaar](https://bazaar.abuse.ch/)）蒐集Emotet和Wannacry樣本。
- 惡意軟體共享社區
    - VirusShare: 一個免費的惡意軟體樣本庫，==需要註冊才能訪問==。它提供了大量的惡意軟體樣本，但使用時需要特別小心和遵守法律。
    - Malshare: 另一個惡意軟體分享平台，提供大量樣本供安全研究使用。

### 3.2 capa配置與使用
- 下載capa工具並安裝：
  ```bash
  git clone https://github.com/mandiant/capa.git
  cd capa
  pip install -r requirements.txt
  ```
  
- 使用capa分析樣本：
複製程式碼
```bash
capa path/to/malware_sample
```

### 3.3 相似度分析
- 使用Python進行Jaccard index計算：
```bash
def jaccard_similarity(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union
```
### 3.4 變體創建
- 參考開源惡意軟體代碼（如GitHub上的惡意軟體項目），修改和創建新的變體。
- 測試變體的有效性並確保其功能完整。

### 3.5 結果報告
- 生成和分析capa報告，並將結果可視化以便更直觀地展示相似度。

## 4. 延伸計畫
- **AI相似度演算法**：
  - 探索和實現更高效的AI相似度演算法（如神經網絡或聚類算法），提升變體偵測的準確性。

- **基線工具與評估**：
  - 確立capa作為基線工具，並對比AI演算法的性能。

## 5. 工具與技術
- **capa**：功能特徵分析工具。
- **Jaccard index**：相似度計算。
- **Python**：數據處理和分析。
- **開源惡意軟體代碼**：變體創建參考。

## 6. 參考資料
- [capa GitHub](https://github.com/mandiant/capa)
- [VirusTotal](https://www.virustotal.com/)
- [MalwareBazaar](https://bazaar.abuse.ch/)

- [jaccardindex example](https://github.com/es0/MalwareSimilarityGraphhttps://) 

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


- 被坦
- 小菜
    - 在抓更多的惡意軟體
    - 抓最新的軟體判斷他是哪種
    - 交叉比對
        - 相關延伸圖
    - 願景 分析未被分析的病毒 判斷偏向哪種


- 13bo
    - 優化jaccard分析





- 下載惡意軟體
    - https://virusshare.com/
    - https://github.com/ytisf/theZoo/
    - https://github.com/fabrimagic72/malware-samples/tree/master/Ransomware/Wannacry
    - https://github.com/Endermanch/MalwareDatabase
    - https://github.com/chronosmiki/RANSOMWARE-WANNACRY-2.0


#### Emotet
![image](https://hackmd.io/_uploads/r1jytPwFR.png)
- [MalwareBazaar | Emotet](https://bazaar.abuse.ch/browse/tag/Emotet/)
- [VirusTotal | Emotet](https://www.virustotal.com/gui/file/fc11f30fb0debf8b8f42a7e9c0678df69c8b171c0038ea7aca7217b43b3c220f/detection)
fc11f30fb0debf8b8f42a7e9c0678df69c8b171c0038ea7aca7217b43b3c220f

- [malpedia | Emotet (Malware Family)](https://malpedia.caad.fkie.fraunhofer.de/details/win.emotet)


#### WannaCry
- [VirusTotal | ](https://www.virustotal.com/gui/file/3ecc0186adba60fb53e9f6c494623dcea979a95c3e66a52896693b8d22f5e18b/detection)
3ecc0186adba60fb53e9f6c494623dcea979a95c3e66a52896693b8d22f5e18b
- [MalwareBazaar | WannaCry](https://bazaar.abuse.ch/browse/signature/WannaCry/)
- [MalShare](https://malshare.com/search.php?query=YRP/WannaCry_Ransomware)


<br>
<br>
<br>




## 簡報流程
(記得檢查投影會被切到的部分)
(記得加頁數)
- [capa簡介](https://github.com/mandiant/capa)，說明分析內容
    - 說明capa在幹嘛 以此來作為我們分析報告是準的佐證
    - 感覺可以逆向本體來證明capa的報告是對的
- wanncry簡介
    - 病毒簡介
- Jaccard 指數的定義




# jaccard index介紹

給定兩個集合 A 和 B，Jaccard 指數 J(A, B) 定義為：
    > $J(A, B)=\frac{A∩B}{A∪B}$ ($\frac{交集元素數量}{聯集元素數量}$)


```python
import numpy as np

def jaccard_binary(x,y):
    """A function for finding the similarity between two binary vectors"""
    intersection = np.logical_and(x, y)
    union = np.logical_or(x, y)
    similarity = intersection.sum() / float(union.sum())
    return similarity

# Define some binary vectors
x = [0,1,0,0,0,1,0,0,1]
y = [0,0,1,0,0,0,0,0,1]
z = [1,1,0,0,0,1,0,0,0]

# Find similarity among the vectors
simxy = jaccard_binary(x,y)
simxz = jaccard_binary(x,z)
simyz = jaccard_binary(y,z)

print(' Similarity between x and y is', simxy, '\n Similarity between x and z is ', simxz, '\n Similarity between x and z is ', simyz)
```

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

## 一些嘗試


### 比對文件方式
(by ChatGPT)
三種不同的相似度度量方式來比較它們的相似程度：

- Jaccard Index: 0.286
這個指數表示兩個文本之間的相似度約為 28.6%。Jaccard 指數是通過計算兩個集合的交集與並集之間的比率來得出。
Cosine Similarity: 0.445

- Cosine 相似度為 0.445
表示這兩個文本在特徵空間中的角度較小，相似度約為 44.5%。這是一種常用於文本比較的相似度度量方法，特別是在詞頻向量空間中。
Dice Coefficient: 0.445

- Dice 系數也為 0.445
表示兩個文本的重合部分佔總數的 44.5%。這是一種基於相交詞語數量與總詞語數量之和的度量。

程式碼: 
```python
import re

# Basic stop words list
STOP_WORDS = {
    'the', 'and', 'is', 'in', 'it', 'of', 'to', 'a', 'with', 'as', 'for', 'on', 'that', 'this',
    'by', 'an', 'are', 'be', 'or', 'from', 'at', 'was', 'which', 'but', 'has', 'have', 'not', 'can'
}

def preprocess_text(text):
    """Preprocess the text by removing punctuation, converting to lowercase, splitting into words, and removing stop words."""
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    words = text.split()
    words = [word for word in words if word not in STOP_WORDS]
    return set(words)

def jaccard_index(set1, set2):
    """Calculate Jaccard Index between two sets."""
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    if not union:
        return 0.0
    return len(intersection) / len(union)

def cosine_similarity(set1, set2):
    """Calculate cosine similarity between two sets."""
    intersection = len(set1.intersection(set2))
    return intersection / ((len(set1) * len(set2)) ** 0.5)

def dice_coefficient(set1, set2):
    """Calculate Dice coefficient between two sets."""
    intersection = len(set1.intersection(set2))
    return (2 * intersection) / (len(set1) + len(set2))

# Read the contents of the files
with open("/mnt/data/wanna.txt", "r") as file1, open("/mnt/data/01.txt", "r") as file2:
    text1 = file1.read()
    text2 = file2.read()

# Preprocess the texts
set1 = preprocess_text(text1)
set2 = preprocess_text(text2)

# Calculate similarity metrics
jaccard = jaccard_index(set1, set2)
cosine = cosine_similarity(set1, set2)
dice = dice_coefficient(set1, set2)

jaccard, cosine, dice

```

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


# capa介紹

## 版本
- 7.1.0
## 簡介
- 沙箱，有動(v7.0)、靜分析
    - 相較靜態；動態分析可以用來執行有被打包過的病毒檔
    - 分別說明動、靜態分析過程
    - [靜態參考](https://cloud.google.com/blog/topics/threat-intelligence/capa-automatically-identify-malware-capabilities/)
## 分析資料消化
### capa分析出來的東西大致可分為四種
- 基本資訊(威脅指標?)
    - 不看
- ATT&CK
    - 最常聽到的攻擊類型標準
- MBC
    - 同樣也是惡意軟體攻擊類型的一種
    - 更細(?
    - 微行為(Micro-behaviors)
- Capability
    - 說明大致在幹嘛

### 現在問題
1. 如果ATT&CK or MBC有多或少要怎麼判斷
- ATT
    - 有多的情況:
        - 先分析大類有哪些(14類) 把較不相關的刪掉
        - 再根據相關程度做不同的權重分析
        - *問題*: 需要給類別中全部細項作評分?
    - 有少的情況:
        - 看少哪類一樣判斷權重
        - *問題*: 
    - 目前想法:
        - 先找出較為重要的那幾項作為主要評斷標準
            - ex:
        - 就真的慢慢分析相關ATT&CK
        - 先排除掉過於大眾的內容
        - **選出核心行為，如果少的話大扣分，多的話則判斷是多什麼來給不同權重**
- MBC
    - 基本上問題也類似上面，有八個子項目


2. Capability要不要採納 (現在偏好不用
    - 因為MBC感覺已經夠完整
    - 多跑幾次同樣動作(ex: xor)可能會因此被混淆(?
<!-- 決定不採納 ~~資料太多了~~ -->
---


### 本體
- [ATT&CK Tactic](https://attack.mitre.org/)
    - DEFENSE EVASION (防禦規避)
        - T1222
            - 修改檔案讀寫權限
        - T1027
            - 對自己的數據進行加密以防止被抓到
    - DISCOVERY (探索環境)
        - T1083
            - 探索系統中的所有檔案
        - T1012
            - 查詢註冊表
    - EXECUTION (執行)
        - T1129
            - 攻擊者可能通過加載共享模組來執行惡意代碼。這可能涉及使用系統庫或其他共享組件，在另一個進程的上下文中運行其代碼，從而避免偵測。
        - T1569.002
            - 攻擊者可能通過服務執行惡意代碼。這涉及創建或修改系統服務，以在服務上下文中執行其代碼，這有助於保持持久性或獲得更高的權限。
    - PERSISTENCE (不被銷毀 立足點)
        - T1543.003
            - 攻擊者可能會創建或修改 Windows 服務以建立持久性。
<!-- - 第一次認真看ATTCK (汗-->


- [Malware Behavior Catalog Objective(MBC)](https://github.com/MBCProject/mbc-markdown/tree/main/micro-behaviors)

![image](https://hackmd.io/_uploads/SJt-7xYKC.png)

    - 也是分析惡意程式行為
    - CRYPTOGRAPHY
        -  Encrypt Data::AES [C0027.001] 
        -  Encrypt Data::RC4 [C0027.009]
        -  Encryption Key::RC4 KSA [C0028.002]
        -  Generate Pseudo-random Sequence [C0021]
        - 不好判斷 感覺很多都會有加密行為 不能當好的依據 
    - DATA
        - Checksum::CRC32 [C0032.001] 
        - Compression Library [C0060] 
        - Encode Data::XOR [C0026.002] 
            - <h5 style="color:red">加密檔案</h5>


    - DEFENSE EVASION 
        - Obfuscated Files or Information::Encoding-Standard Algorithm [E1027.m02]
        - Obfuscated Files or Information::Encryption-Standard Algorithm [E1027.m05] 
    - DISCOVERY 
        - Code Discovery::Enumerate PE Sections [B0046.001] 
        - File and Directory Discovery [E1083]
        - System Information Discovery [E1082]
    - FILE SYSTEM 
        - Copy File [C0045] 
        - Create Directory [C0046]
        - Get File Attributes [C0049]
        - Read File [C0051]
        - Set File Attributes [C0050]
        - Writes File [C0052] 
    - OPERATING SYSTEM
        -  Registry::Query Registry Value [C0036.006]
        -  Registry::Set Registry Key [C0036.001]
            -  註冊表變更
    - PROCESS
        - Check Mutex [C0043]
        -  Create Process [C0017]
        -  Terminate Process [C0018]




## 要採納的條件
### ATT&CK
- 全部類型:
    - [ ] Initial Access (初始訪問)
    - [ ] Reconnaissance (偵查)
    - [ ] Execution (執行)
    - [ ] Persistence (不被銷毀立足點)
    - [ ] Privilege Escalation (特權提升)
    - [ ] Defense Evasion (防禦規避)
    - [ ] Credential Access (憑證訪問)
    - [ ] Discovery (探索環境)
    - [ ] Lateral Movement (橫向移動)
    - [ ] Collection (數據收集)
    - [x] Exfiltration (數據外傳)
    - [ ] Command and Control (指揮與控制)
    - [ ] Impact (影響)
    - [x] Resource Development (資源開發)


- 基本上不會有的
    - Resource Development (資源開發)
    - Exfiltration (數據外傳)
### MBC
- 全部類型
    - [ ] Communication
    - [ ] Cryptography
    - [ ] Data
    - [ ] File System	
    - [x] Hardware
    - [x] Memory
    - [ ] Process
    - [ ] Operating System

- 基本上不會有
    - Hardware
    - Memory


## 參考資料
- [說明capa沙箱動態分析](https://cloud.google.com/blog/topics/threat-intelligence/dynamic-capa-executable-behavior-cape-sandbox/)
- [capa2.0](https://cloud.google.com/blog/topics/threat-intelligence/capa-2-better-stronger-faster/)
- [capa自動分析](https://cloud.google.com/blog/topics/threat-intelligence/capa-automatically-identify-malware-capabilities/)






# 討論構思主題過程

---
討論過程
---
### 較可能的
流量分析 http
假新聞
刻惡意程式


## 主題討論
- 工控方面
    - ~~助教不熟~~
    - 暫放棄
- AI分析

- 圖像化(? 
- 也可鑑識、建議藍一點
- 開發 自己寫code
- 教授說？sandbox...執行以後...分析哪個來源...
- 分析惡意軟體 然後加強他

- Defense Evasion
- sandbox
    - cuckoo
- 有sandbox執行過惡意程式 怎麼把他的動作轉換成圖示表 ex Virustotal
- LSTM很適合做API分析
    - DL+ML? 
- google hacking LLM
- 優化情資蒐集平台


### 放棄的
提案被打槍的原因：有人做過 不創新、難以實現

1.太難 可能做不出來
2.太弱(沒有創意) ->安全牌
流量分析
假消息


- IDA plugin
    - (去年有人做gidra plugin)
    - 因: 我們都不熟IDA和Reverse

- 工控
    - 相關性不大


### 待估
<h2 style="color:red;"> </h2>
## 暗網爬蟲 （備備案
- 太大略
- 特定網站?
- 消化資料
- 現有太多
- **創新性不夠**
    

## 惡意軟體分析、復現
- antiscan

## 流量分析(沒有加密的)
- 有加密的不行 
- 現有技術太成熟 不建議
- 可能會被被噹爆

## 可視化
- 不知道要可視化什麼

## 以CVE搜CVE
- 資料少
- 關聯性難找

## 假情資

## 惡意軟體(最終稿)
(惡意程式變體偵測)

做木馬 emotet bemtet 找他變體
然後丟capa 
看特徵
參考open source Malware
刻一個類似的出來
丟回capa ，對比和原本變體的相似度 看差多少
延伸：
輸入哪一種惡意程式
1.Wannacry 勒索
2.emotet 木馬
<!-- jaccard index -->
樣本經過capa
找到同一個樣本 但有變體
(投放在一個向量空間中 比較近 因為有相似的結構)
跟demo 
可能只有...的那一塊是差不多的

capa ->跑出報告
會離原本的很近 就會跑


如果真的要AI
相似度的演算法(比對)

推薦capa是因為它是baseline （AI應該很難超過）




做情資
<!-- 基於聚類分析技術的惡意程式變體辨識方法研究 -->
<!-- 基於聚類分析技術的惡意軟體變體辨識方法研究 -->




## 老師0730下午 說想看到的
- 靜態檔案
- API特徵
- 怎麼轉化成Technique這張表
    - （沒有很容易）


### 已有主題


## 我們有的技能
串AI
區塊鏈
爬暗網
流量分析

# 每日總結

## D1結論
### ~~明天再說~~
q



## D2結論
### 暫定主題"基於聚類分析技術的惡意軟體變體辨識方法研究"
### 統整open-source-Malware分類

## D3結論
### 確認專題製作題目
### 抓取wannacry本體及變體樣本並分析
### 分析capa報告不需要看的ATT&CK跟MBC類型



---
組員
吳玥儒(萊姆)
鄭宇兩(貝坦)
曹凱翔(l3obo)
蔡士煒(小蔡)









