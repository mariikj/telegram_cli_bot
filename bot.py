from pyrogram import Client, filters
from pyrogram.raw import functions
import csv

app = Client("my_account",config_file="config.ini")

def get_channel_lists():
    channel_names = []
    with open("channel_lists.csv", mode = 'r')as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            channel_names.append(line)
        return channel_names
            

@app.on_message(filters.channel)
async def project_board_messages(client, message):
    print(message.chat.username)
    if message.chat.username == 'project_board':
        await app.send_message("@Marii_kj", message.text)
        await app.send_message("@Marii_kj", "from: @" + str(message.chat.username))

#checking if a channel is already added 
def channel_exists(channel_name):

    with open("channel_lists.csv", mode = 'r')as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if channel_name == line[0]:
                return True
    csv_file.close()
    return False  

#adding new channel with "add_channel 'channel name'" message that i personally should send 
@app.on_message(filters.me)
async def add_channel(client, message):
    
    command = message.text.split()[0]
    channel_name = message.text.split()[1]

    if command == "add_channel":
        with open("channel_lists.csv", mode='a') as csv_file:
            if channel_exists(channel_name) == False:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([channel_name])

print(get_channel_lists())
app.run()