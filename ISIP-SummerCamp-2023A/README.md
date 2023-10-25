# Web 題目說明

- 如何啟動?
- 個別題目說明以及連線資訊

## Writeups
[HackMD解答](https://hackmd.io/@edstudiotw/SJdajeAJp)

## How to Start the lab
- First you must in the directory `Web_Verified`
- Next, enter the command below

```
docker-compose up -d
```
P.S. 第一題 Port 8007 的題目請依照順序解題
## Find GET Method 
> 你會使用開發者工具找到神秘的 header 嗎?
- [ ] Port: 8007
## Find POST Method
> 你會使用開發者工具找到被藏起來的 request parmater 嗎?
- [ ] Port: 8007
## Mystery Header ?
> 網路餅乾莫名其妙就跑到我的電腦上了，他是怎麼被新增進來的呢？你能透過觀察開發者工具的網路流量中，找出該伺服器回應的神秘 Header 嗎？請試著登入看看管理系統，帳號密碼為 guest / guest 提交FLAG的時候，請直接打出 HTTP Header 的名稱例如：X-Forward-For
- [ ] Port: 8007
## Find Mystery Cookies
> 那你知道在哪裡可以修改跟檢視 Cookie 嗎？找找看除了 UserID 有沒有其他神秘的 Cookie ?
- [ ] Port: 8007
## Modify the Cookie !
> 那你知道在哪裡可以修改跟檢視 Cookie 嗎？聽說把 Cookie 改成 admin 好像就可以看到一些神秘的頁面喔！
- [ ] Port: 8007
## Find DELETE METHOD
> 我好像發現一個API，可以拿來刪除使用者誒！可是我只是一個版主，我可以偷偷刪掉別人嗎？聽到開發人員在討論，刪除的方法好像有點特別，不是一般人碰得到的Method ...那我該用什麼Method 呢？提示：請使用 BurpSuite / Postman 做送出
- [ ] Port: 8007
## Website Under Development & Leak Cookie
> 你學會如何找Cookie 了對吧！那如果 Cookie 被加密了怎麼辦 ?
P.S. 小宸在網頁開發部門工作，他在部署測試環境時忘記將開發資料夾上鎖… 解密的Key好像放在某個地方，尤其是搜尋引擎不會去的地方
- [ ] Port: 8002
## May I have the free point ?
> 你能協助宸宸看到購買 Flag Point 的頁面嗎？
- [ ] Port: 8100
## Free point for me ?
> 這…這是可以免費拿的嗎？嘗試用划算的價格買到 Flag Point ?
- [ ] Port: 8100
## Fix My Blog …
> 我的部落格因為是從家裡轉移到雲端的，雖然我把它開起來了，但是東西都看不到，有啥方法可以幫我修改這些舊的網址 http://wpblog-kikihost.xyz:8022到新的網址 http://ctf-isip.tyc4d.tw:8022 嗎？
- [ ] Port: 8022
## You can’t see me
> 宸宸發現某個神秘的ID按下去之後，莫名其妙就到了奇怪的地方，你能找出中間經過了哪些重要的地方嗎?
- [ ] Port: 8005
## Where is Edward
> 你知道水平越權是什麼嗎？你能幫我找找 Edward 在哪裡嗎？
- [ ] Port: 8001

Hint: 我為你攔截好封包ㄌ，可以送到 BurpSuite Inturder 分析唷
```
GET /user/§5§ HTTP/1.1Host: ctf-isip.tyc4d.tw:8001
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://ctf-isip.tyc4d.tw:8001/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: session=286d8192-f687-4fc2-b45c-a18c8df0a7d1.vMjCIR82uYDbDrjYWiH2zW9GPs4
Connection: close


```
## Welcome2SQL
> 你想知道伺服器怎麼驗證你的身份嗎？可以看看我精心設計的MAGIC喔！預覽一下你輸入的東西，到SQL之後到底長啥樣？
- [ ] Port: 8003
## WHERE are you (Shopping Cart)
> 小宸是一個SQL小白，他想知道怎麼樣可以只選出他想要的資料，但他只會用WHERE，你可以幫他想想怎麼樣才能讓隱藏的FLAG出現在購物車嗎？HINT: 網站的備份SQL被宸宸找到了，但FLAG是假的… 希望能夠幫助你理解FLAG的相對位置…
- [ ] Port: 8056

## Infomation_Sc...?
> 一般RDBMS (關聯式資料庫管理系統)，都會存有一個TABLE(資料表)，你知道怎麼利用裡面的資訊，來查詢有甚麼樣子的欄位嗎?
請幫助宸宸尋找flag_table中，有幾個欄位的類型是 varchar ? 
Hint: 答案只需要填寫數字
- [ ] Port: 8056

## Dump All Data!
> 小宸已經學會如何使用 information_schema了，現在他想玩拼拼看，你可以拼出正確的語法，藉由登入網站所回傳的結果，來選出幾千筆客戶資料中，唯一的一筆 FLAG 嗎？ Use SQLMAP
- [ ] Port: 8056

## Let the cow Moooooooooow
> 小宸想要寫一個網站可以幫忙他做 生成一隻ASCII文字藝術的牛，他找到現成的應用程式可以完成這件事情，於是他決定讓使用者直接把想要查詢的參數，傳到程式裡面執行
- [ ] Port: 8008

## Real-World
> 自己玩玩看囉，觀察一下有沒有一些有用的資訊，運用先前所學，想辦法透過某個神秘的後台拿到 flag 吧!
- [ ] Port: 8300
- [ ] Port: 8380
