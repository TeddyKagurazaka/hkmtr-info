# fufubot_hkmtr_info
可以使用```python hkmtr.py 上水 旺角```查询 从旺角到上水的推荐路线 实时发车时间 首尾班车推荐路线 车站开放时间 车票价格 行车时间

出发和到达站支持使用上水/SHS/sheungshui的格式填写名称 填写简体会自动转换为繁体

Q:點解文字系廣東話？

A:嚟香港點解唔用廣東話？


類似於
```txt
[Hong Kong MTR車票價格]
由 [東鐵綫] 上水 (Sheung Shui) 去 [觀塘綫] 旺角 (Mong Kok) 嘅車票價格：

請留意，該車票價格僅計算使用八達通拍卡或使用乘車二維碼入閘嘅價格，唔包括購買單程票嘅價格。

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
時間：2023-07-22 10:44:12，目的地：羅湖，站台號：1
時間：2023-07-22 10:48:12，目的地：羅湖，站台號：1
時間：2023-07-22 10:52:12，目的地：落馬洲，站台號：1
時間：2023-07-22 10:56:12，目的地：羅湖，站台號：1
實時到站信息：(下行)
時間：2023-07-22 10:45:12，目的地：金鐘，站台號：2
時間：2023-07-22 10:50:12，目的地：金鐘，站台號：2
時間：2023-07-22 10:54:12，目的地：金鐘，站台號：2
時間：2023-07-22 10:58:12，目的地：金鐘，站台號：2


車廂類型：普通等
路線名稱：最快路綫
成人票價：13.2
學生票價：6.9
行車時間：39分鐘
路線：
在上水2號月台往金鐘方向乘車
在九龍塘2號月台往黃埔方向轉車

車廂類型：普通等
路線名稱：路綫二
成人票價：13.2
學生票價：6.9
行車時間：47分鐘
路線：
在上水2號月台往金鐘方向乘車
在紅磡2號月台往烏溪沙方向轉車
在何文田1號月台往調景嶺方向轉車

車廂類型：普通等
路線名稱：路綫三
成人票價：13.2
學生票價：6.9
行車時間：51分鐘
路線：
在上水2號月台往金鐘方向乘車
在大圍3號月台往屯門方向轉車
在鑽石山2號月台往黃埔方向轉車
```

如果直接調用query_ticket_price時 可以使用lang="E"切換為英文模式

類似於
```txt
[Hong Kong MTR Ticket Prices]
Ticket prices from [東鐵綫] 上水 (Sheung Shui) to [觀塘綫] 旺角 (Mong Kok):

Please note that the ticket prices only apply to Octopus card or QR code entry, and do not include the price of single journey tickets.

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
Time: 2023-07-22 11:00:27, Destination: Lo Wu, Platform: 1
Time: 2023-07-22 11:04:27, Destination: Lok Ma Chau, Platform: 1
Time: 2023-07-22 11:08:27, Destination: Lo Wu, Platform: 1
Time: 2023-07-22 11:12:27, Destination: Lo Wu, Platform: 1
Real-time Arrivals (Down):
Time: 2023-07-22 11:01:27, Destination: Admiralty, Platform: 2
Time: 2023-07-22 11:06:27, Destination: Admiralty, Platform: 2
Time: 2023-07-22 11:10:27, Destination: Admiralty, Platform: 2
Time: 2023-07-22 11:14:27, Destination: Admiralty, Platform: 2


Car Type: Standard
Route Name: Route 1
Adult Price: 13.2
Student Price: 6.9
Travel Time: 39 minutes
Route:
Board at Sheung Shui Platform 2 towards Admiralty
Interchange at Kowloon Tong Platform 2 towards Whampoa

Car Type: Standard
Route Name: Route 2
Adult Price: 13.2
Student Price: 6.9
Travel Time: 47 minutes
Route:
Board at Sheung Shui Platform 2 towards Admiralty
Interchange at Hung Hom Platform 2 towards Wu Kai Sha
Interchange at Ho Man Tin Platform 1 towards Tiu Keng Leng

Car Type: Standard
Route Name: Route 3
Adult Price: 13.2
Student Price: 6.9
Travel Time: 51 minutes
Route:
Board at Sheung Shui Platform 2 towards Admiralty
Interchange at Tai Wai Platform 3 towards Tuen Mun
Interchange at Diamond Hill Platform 2 towards Whampoa
```

