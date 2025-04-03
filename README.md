# fufubot_hkmtr_info

可以使用```python hkmtr.py 上水 旺角 C```查询 从旺角到上水的推荐路线 实时发车时间 首尾班车推荐路线 车站开放时间 车票价格 行车时间

出发和到达站支持使用上水/SHS/sheungshui的格式填写名称 填写简体会自动转换为繁体

*Replace 'C' with 'E' for English output, default is Cantonese.*

Q:點解文字系廣東話？

A:嚟香港點解唔用廣東話？

類似於

```txt
[Hong Kong MTR車票價格]
由 （落馬洲 [LMC]） 去往 （旺角 [MOK]） 嘅車票價格：
【首末班車】
(首：06:38)落馬洲 > 東鐵綫 > 九龍塘 > 觀塘綫 > 旺角
(末：22:55)落馬洲 > 東鐵綫 > 九龍塘 > 觀塘綫 > 旺角
車站開放時間：06:28-23:05

【發車時間】
落馬洲，東鐵綫，下行:
17:20:38，于 1 月台，開往：金鐘
17:29:38，于 2 月台，開往：金鐘
17:39:38，于 1 月台，開往：金鐘
17:45:38，于 2 月台，開往：金鐘

【路線信息】
普通等 最快路綫（49分鐘）
成人票價：HK$ 45.4 (CN¥48.04) 學生票價：HK$ 43.1
- 在落馬洲1號或2號號月台往金鐘方向乘車
- 在九龍塘2號月台往黃埔方向轉車

普通等 路綫二（57分鐘）
成人票價：HK$ 45.4 (CN¥48.04) 學生票價：HK$ 43.1
- 在落馬洲1號或2號號月台往金鐘方向乘車
- 在紅磡2號月台往烏溪沙方向轉車
- 在何文田1號月台往調景嶺方向轉車

普通等 路綫三（61分鐘）
成人票價：HK$ 45.4 (CN¥48.04) 學生票價：HK$ 43.1
- 在落馬洲1號或2號號月台往金鐘方向乘車
- 在大圍3號月台往屯門方向轉車
- 在鑽石山2號月台往黃埔方向轉車

【匯率參考】
港幣兌人民幣: 0.923
人民幣兌港幣: 0.945
更新時間:2025-04-03 14:36:22
```

For English output, add **lang="E"** as parameter when calling query_ticket_price.

```txt
[Hong Kong MTR Ticket Prices]
Ticket prices from (Lok Ma Chau [LMC]) to (Mong Kok [MOK]):
[First and Last Train Info]
(First: 06:38)Lok > East Rail Line > Kowloon Tong > Kwun Tong Line > Mong
(Last: 22:55)Lok > East Rail Line > Kowloon Tong > Kwun Tong Line > Mong
Station Opening Hours: 06:28-23:05

[Departure Time]
Lok Ma Chau,East Rail Line,Down:
17:20:31,At Platform:1,To:Admiralty
17:29:31,At Platform:2,To:Admiralty
17:39:31,At Platform:1,To:Admiralty
17:45:31,At Platform:2,To:Admiralty

[Route Information]
Standard Route 1(49 minutes)
Adult Price: HK$ 45.4 (Approx. CN¥48.04) Student Price: HK$ 43.1
- Board at Lok Ma Chau Platform 1 or 2 towards Admiralty
- Interchange at Kowloon Tong Platform 2 towards Whampoa

Standard Route 2(57 minutes)
Adult Price: HK$ 45.4 (Approx. CN¥48.04) Student Price: HK$ 43.1
- Board at Lok Ma Chau Platform 1 or 2 towards Admiralty
- Interchange at Hung Hom Platform 2 towards Wu Kai Sha
- Interchange at Ho Man Tin Platform 1 towards Tiu Keng Leng

Standard Route 3(61 minutes)
Adult Price: HK$ 45.4 (Approx. CN¥48.04) Student Price: HK$ 43.1
- Board at Lok Ma Chau Platform 1 or 2 towards Admiralty
- Interchange at Tai Wai Platform 3 towards Tuen Mun
- Interchange at Diamond Hill Platform 2 towards Whampoa

[Exchange Rate]
HKD->CNY: 0.923
CNY->HKD: 0.945
Last Update:2025-04-03 14:36:22
```

## warning

<!-- 咁嗨鍾意將人哋啲霖法當自己嘅Idea然後drop低去自己嘅Project度，

仲要屌翻人哋嘅撲街，真係好嗨卵有創意，建議翻去學習下點樣做人。

唔好意思，我唔係聖人，我唔會原諒你，建議你刪埋你個repo，唔好再出現喺我面前。-->

ㄍㄢˋ ㄏㄞˋ ㄓㄨㄥ ㄧˋ ㄐㄧˋ ㄔㄤ ㄖㄣˊ ㄉㄧˋ ㄧ ㄈㄚˇ ㄉㄤˋ ㄗ˙ ㄏㄞˇ ㄍㄜ˙ ㄇㄨㄛˋ ㄈㄚ ㄉㄤ ㄗㄜˋ ㄗˇ ㄧˋ ㄉㄧㄝˋ ㄍㄨㄛˇ ㄓ˙ ㄏㄨˋ ㄧˇ ㄉㄜ ㄒㄧㄢˋ ㄇㄚㄣˊ ㄔㄨㄛˋ ㄍㄨㄛˇ ㄉㄚˋ ㄍㄜ˙ ㄉㄧ ㄉㄞˋ，

ㄓㄥˋ ㄨㄛˋ ㄉㄧ ㄉㄧㄝˋ ㄍㄜ˙ ㄅㄤˇ ㄖㄣˊ ㄉㄧ ㄐㄧㄝˊ ㄇㄚˋ ㄍㄨㄚˇ ㄍㄠ ㄞˇ ㄓㄢˇ ㄘㄨㄥˋ，

ㄓㄣ ㄍㄜ ㄏㄠˇ ㄏㄠ ㄌㄧㄣˊ ㄉㄧˋ ㄈㄢˋ ㄏㄜˊ ㄏㄠˇ ㄍㄜ ㄔㄨㄥˊ ㄧˇ ㄅㄚˇ ㄧㄡˇ ㄔㄨㄤˋ，ㄐㄧㄢˋ ㄉㄧㄢˇ ㄍㄨㄛ ㄋㄧㄚˊ ㄍㄨㄛˋ ㄏㄠˋ ㄧˋ ㄐㄧㄢˋ ㄍㄜ˙ ㄒㄧㄝˋ ㄅㄧㄢˋ ㄏㄨㄛˇ ㄧㄒㄧㄢˋ ㄧㄞˋ ㄉㄧㄢˋ ㄈㄢˋ
