# fufubot_hkmtr_info

可以使用```python hkmtr.py 上水 旺角```查询 从旺角到上水的推荐路线 实时发车时间 首尾班车推荐路线 车站开放时间 车票价格 行车时间

出发和到达站支持使用上水/SHS/sheungshui的格式填写名称 填写简体会自动转换为繁体

Q:點解文字系廣東話？

A:嚟香港點解唔用廣東話？

類似於

```txt
[Hong Kong MTR車票價格]
由 [東鐵綫] 上水 (Sheung Shui) [SHS] 去 [觀塘綫] 旺角 (Mong Kok) [MOK] 嘅車票價格：
首班車時間：05:40
首班車路綫: 上水 (Sheung Shui) > 東鐵綫 (East Rail Line) > 九龍塘 (Kowloon Tong) > 觀塘綫 (Kwun Tong Line) > 旺角 (Mong Kok)
末班車時間：00:04
尾班車路綫: 上水 (Sheung Shui) > 東鐵綫 (East Rail Line) > 九龍塘 (Kowloon Tong) > 觀塘綫 (Kwun Tong Line) > 旺角 (Mong Kok)
上述時間為列車由月台開出的實際時間。乘搭尾班車的乘客須於列車開出前最少5分鐘入站。
車站開放時間：05:30-01:17
乘搭首/尾班車的乘客必須使用本頁列明的轉乘路綫，因有關的轉乘路綫可能與行程指南所建議的路綫不同。

[東鐵綫] 上水 (Sheung Shui) 嘅實時發車時間：
線路：東鐵綫 (East Rail Line)
實時到站信息：(上行)
時間：2025-03-20 05:56:20，目的地：羅湖，站台號：1
時間：2025-03-20 05:59:40，目的地：落馬洲，站台號：1
時間：2025-03-20 06:05:23，目的地：羅湖，站台號：1
時間：2025-03-20 06:11:45，目的地：落馬洲，站台號：1
實時到站信息：(下行)
時間：2025-03-20 05:39:20，目的地：金鐘，站台號：2
時間：2025-03-20 05:42:39，目的地：金鐘，站台號：2
時間：2025-03-20 05:47:39，目的地：金鐘，站台號：2
時間：2025-03-20 05:54:00，目的地：金鐘，站台號：2


車廂類型：普通等
路線名稱：最快路綫
成人票價：HK$ 13.6 (CN¥14.45)
學生票價：HK$ 7.1
行車時間：39分鐘
路線：
在上水2號月台往金鐘方向乘車
在九龍塘2號月台往黃埔方向轉車

車廂類型：普通等
路線名稱：路綫二
成人票價：HK$ 13.6 (CN¥14.45)
學生票價：HK$ 7.1
行車時間：47分鐘
路線：
在上水2號月台往金鐘方向乘車
在紅磡2號月台往烏溪沙方向轉車
在何文田1號月台往調景嶺方向轉車

車廂類型：普通等
路線名稱：路綫三
成人票價：HK$ 13.6 (CN¥14.45)
學生票價：HK$ 7.1
行車時間：51分鐘
路線：
在上水2號月台往金鐘方向乘車
在大圍3號月台往屯門方向轉車
在鑽石山2號月台往黃埔方向轉車


【票價適用及支付方式】
本頁票價僅適用於以下方式進出港鐵重鐵網絡*時：
- 八達通
- 感應式信用卡／扣賬卡（Visa、Mastercard、銀聯，銀聯扣賬卡除外）
- 二維碼（AlipayHK 易乘碼、MTR Mobile 車票二維碼、雲閃付港鐵乘車碼、騰訊乘車碼）
- 全國交通一卡通（China T-Union Card）

除八達通外，上述支付方式均僅適用於港鐵重鐵網絡*。

【通用規則】
- 以感應式卡、二維碼或交通聯合卡支付的車費，均按成人八達通票價計算，不適用任何小童、學生、長者或特惠票價。
- 政府公共交通費用補貼計劃及其他港鐵車費優惠不適用。
- 經尖沙咀站／尖東站轉乘視為兩個獨立車程並分開收費。
- 二維碼乘車需入閘前預先選定票種及等級，入閘後不可更改。

【匯率參考】
- 港幣兌人民幣匯率：0.92
- 人民幣兌港幣匯率：0.941
- 資料獲取時間：2025-03-20 03:14:53
匯率由八達通卡有限公司網頁獲取，僅供參考，實際以讀寫器所存匯率為準。

【全國交通一卡通特別提示】
- 港鐵不提供人民幣增值服務，請向發卡機構查詢。
- 入港前需確保卡內餘額不少於人民幣50元，最高儲值額為人民幣1,000元。

*不適用於機場快綫、輕鐵、港鐵巴士、港鐵接駁巴士及東鐵綫頭等。
備註：使用感應式信用卡／扣賬卡乘搭港鐵時，系統會於每日營運結束後統一結算當日乘車總額。銀行賬單上一般只會顯示每日或多日累計的總車費金額。
```

如果直接調用query_ticket_price時 可以使用lang="E"切換為英文模式

類似於

```txt
[Hong Kong MTR Ticket Prices]
Ticket prices from [東鐵綫] 上水 (Sheung Shui) [SHS] to [觀塘綫] 旺角 (Mong Kok) [MOK]:
First Train Time: 05:40
First Train Route: 上水 (Sheung Shui) > 東鐵綫 (East Rail Line) > 九龍塘 (Kowloon Tong) > 觀塘綫 (Kwun Tong Line) > 旺角 (Mong Kok)
Last Train Time: 00:04
Last Train Route: 上水 (Sheung Shui) > 東鐵綫 (East Rail Line) > 九龍塘 (Kowloon Tong) > 觀塘綫 (Kwun Tong Line) > 旺角 (Mong Kok)
The time shown is the scheduled departure time from the platform.  Passengers for the last train should enter the station at least 5 minutes before the scheduled departure time.
Station Opening Hours: 05:30-01:17
Passengers taking the first/last train must use the transfer routes listed on this page, as the recommended routes in the travel guide may differ.

Real-time departure times from [東鐵綫] 上水 (Sheung Shui):
Line: 東鐵綫 (East Rail Line)
Real-time Arrivals (Up):
Time: 2025-03-20 05:56:20, Destination: Lo Wu, Platform: 1
Time: 2025-03-20 05:59:40, Destination: Lok Ma Chau, Platform: 1
Time: 2025-03-20 06:05:23, Destination: Lo Wu, Platform: 1
Time: 2025-03-20 06:11:45, Destination: Lok Ma Chau, Platform: 1
Real-time Arrivals (Down):
Time: 2025-03-20 05:39:20, Destination: Admiralty, Platform: 2
Time: 2025-03-20 05:42:39, Destination: Admiralty, Platform: 2
Time: 2025-03-20 05:47:39, Destination: Admiralty, Platform: 2
Time: 2025-03-20 05:54:00, Destination: Admiralty, Platform: 2


Car Type: Standard
Route Name: Route 1
Adult Price: HK$ 13.6 (Approx. CN¥14.45)
Student Price: HK$ 7.1
Travel Time: 39 minutes
Route:
Board at Sheung Shui Platform 2 towards Admiralty
Interchange at Kowloon Tong Platform 2 towards Whampoa

Car Type: Standard
Route Name: Route 2
Adult Price: HK$ 13.6 (Approx. CN¥14.45)
Student Price: HK$ 7.1
Travel Time: 47 minutes
Route:
Board at Sheung Shui Platform 2 towards Admiralty
Interchange at Hung Hom Platform 2 towards Wu Kai Sha
Interchange at Ho Man Tin Platform 1 towards Tiu Keng Leng

Car Type: Standard
Route Name: Route 3
Adult Price: HK$ 13.6 (Approx. CN¥14.45)
Student Price: HK$ 7.1
Travel Time: 51 minutes
Route:
Board at Sheung Shui Platform 2 towards Admiralty
Interchange at Tai Wai Platform 3 towards Tuen Mun
Interchange at Diamond Hill Platform 2 towards Whampoa


[Fare Applicability and Payment Methods]
The fares shown on this page apply only when using the following payment methods on the MTR heavy rail network*:
- Octopus
- Contactless credit/debit cards (Visa, Mastercard, UnionPay; UnionPay debit cards are not accepted)
- QR codes (AlipayHK EasyGo, MTR Mobile QR Code Ticket, UnionPay MTR Transit QR Code, Tencent Transit QR Code)
- China T-Union Card

Except for Octopus, the above payment methods are only available for the MTR heavy rail network*.

[General Rules]
- Fares paid with contactless cards, QR codes or China T-Union Cards are charged at the Adult Octopus fare; concessionary fares do not apply.
- The Public Transport Fare Subsidy Scheme and other MTR fare promotions are not applicable.
- MTR rides which interchange at Tsim Sha Tsui / East Tsim Sha Tsui station will be considered as two separate single journeys.
- For QR code rides, passenger type and class must be selected before entry and cannot be changed after entry.

[Exchange Rate Reference]
- HKD to RMB exchange rate: 0.92
- RMB to HKD exchange rate: 0.941
- Data retrieved at: 2025-03-20 03:14:53
Rates are obtained from the Octopus Cards Limited website for reference only. The actual rate is determined by the rate stored in the Octopus reader at the time of transaction.

[China T-Union Card Special Notes]
- RMB top-up service is not available on MTR. Please contact the card issuer for enquiries.
- Before arriving in Hong Kong, passengers should ensure the card has a balance of at least RMB50, with a maximum stored value of RMB1,000.

*Not available at Airport Express, Light Rail, MTR Bus, MTR Feeder Bus and East Rail Line First Class.
Note: When using contactless credit/debit cards for MTR rides, the system will consolidate all rides and settle the total daily fare after end-of-service. Your bank statement will typically show one aggregated transaction per day or multiple days.
```

## warning

<!-- 咁嗨鍾意將人哋啲霖法當自己嘅Idea然後drop低去自己嘅Project度，

仲要屌翻人哋嘅撲街，真係好嗨卵有創意，建議翻去學習下點樣做人。

唔好意思，我唔係聖人，我唔會原諒你，建議你刪埋你個repo，唔好再出現喺我面前。-->

ㄍㄢˋ ㄏㄞˋ ㄓㄨㄥ ㄧˋ ㄐㄧˋ ㄔㄤ ㄖㄣˊ ㄉㄧˋ ㄧ ㄈㄚˇ ㄉㄤˋ ㄗ˙ ㄏㄞˇ ㄍㄜ˙ ㄇㄨㄛˋ ㄈㄚ ㄉㄤ ㄗㄜˋ ㄗˇ ㄧˋ ㄉㄧㄝˋ ㄍㄨㄛˇ ㄓ˙ ㄏㄨˋ ㄧˇ ㄉㄜ ㄒㄧㄢˋ ㄇㄚㄣˊ ㄔㄨㄛˋ ㄍㄨㄛˇ ㄉㄚˋ ㄍㄜ˙ ㄉㄧ ㄉㄞˋ，

ㄓㄥˋ ㄨㄛˋ ㄉㄧ ㄉㄧㄝˋ ㄍㄜ˙ ㄅㄤˇ ㄖㄣˊ ㄉㄧ ㄐㄧㄝˊ ㄇㄚˋ ㄍㄨㄚˇ ㄍㄠ ㄞˇ ㄓㄢˇ ㄘㄨㄥˋ，

ㄓㄣ ㄍㄜ ㄏㄠˇ ㄏㄠ ㄌㄧㄣˊ ㄉㄧˋ ㄈㄢˋ ㄏㄜˊ ㄏㄠˇ ㄍㄜ ㄔㄨㄥˊ ㄧˇ ㄅㄚˇ ㄧㄡˇ ㄔㄨㄤˋ，ㄐㄧㄢˋ ㄉㄧㄢˇ ㄍㄨㄛ ㄋㄧㄚˊ ㄍㄨㄛˋ ㄏㄠˋ ㄧˋ ㄐㄧㄢˋ ㄍㄜ˙ ㄒㄧㄝˋ ㄅㄧㄢˋ ㄏㄨㄛˇ ㄧㄒㄧㄢˋ ㄧㄞˋ ㄉㄧㄢˋ ㄈㄢˋ
