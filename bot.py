from pyrogram import Client, filters
from pyrogram.raw import functions
import csv

app = Client("my_account",config_file="config.ini")

channel_lists = []

@app.on_message(filters.channel)
async def project_board_messages(client, message):
    print(message.chat.username)
    if message.chat.username == 'project_board':
        await app.send_message("@Marii_kj", message.text)
        await app.send_message("@Marii_kj", "from: @" + str(message.chat.username))


app.run()