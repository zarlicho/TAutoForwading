from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetInlineBotResultsRequest
from telethon import TelegramClient, events
from telethon import TelegramClient, events, sync
import csv
import time
api_id = '8977367'
api_hash = 'd9a8cbdd0ba21647bee37edbfe322cec'
phone = '+62085771014979'
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))



chats = []
last_date = None
chunk_size = 200
groups=[]
bot = []
channel = "1623988554"
# get all channels
channel_username = 'DataSaham2Bot'# your channel
groupUsername = "Python group.py"# your group
# message = []
# for message in client.get_messages(channel_username, limit=1):
#     # get last message text
#     message = message.message

@client.on(events.NewMessage)
async def handle_new_message(event):
    if event.is_private:
        chat = event.message.message
        print(event.message.message)
        # send message to channel
        await client.send_message(groupUsername, chat)
# if get new message
client.start()
client.run_until_disconnected()