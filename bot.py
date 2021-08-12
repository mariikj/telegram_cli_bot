from pyrogram import Client, filters

app = Client("my_account",config_file="config.ini")

@app.on_message(filters.channel)
async def project_board_messages(client, message):
    print(message.chat.username)
    if message.chat.username == 'project_board':
        await app.send_message("@Marii_kj", message.text)
        await app.send_message("@Marii_kj", "from: " + str(message.chat.username))


@app.on_message(filters.private)
async def private_messages(client, message):
   await app.send_message("@Marii_kj", message.text)
   await app.send_message("@Marii_kj", "from: @" + message.chat.username)

app.run()