def handle_message(event):
    with ApiClient(configuration) as api_client:
        # 當使用者傳入文字訊息時
        print("#" * 30)
        line_bot_api = MessagingApi(api_client)
        # event 為 Line Server 傳來的事件物件所有關於一筆訊息的資料皆可從中取得
        # print("event 一個Line文件訊息的事件物件:", event)
        # 在此的 evnet.message.text 即是 Line Server 取得的使用者文字訊息
        user_msg = event.message.text
        print("使用者傳入的文字訊息是:", user_msg)
        # 使用TextMessage產生一段用於回應使用者的Line文字訊息
        bot_msg = TextMessage(text=f"Hiii 你剛才說的是: {user_msg}")

        if user_msg == "電話":
            bot_msg = TextMessage(text="0912345678")
        else user_msg == "地址":
            bot_msg = TextMessage(text="中山區")


        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                # 放置於 ReplyMessageRequest 的 messages 裡的物件即是要回傳給使用者的訊息
                # 必須注意由於 Line 有其使用的內部格式
                # 因此要回覆的訊息務必使用 Line 官方提供的類別來產生回應物件
                messages=[
                    # 要回應的內容放在這個串列中
                    bot_msg,
                    TextMessage(text="Hello World"),
                ]
            )
        )