from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetInlineBotResultsRequest
from telethon import TelegramClient, events
from telethon import TelegramClient, events, sync
import csv
import time
api_id = '19375432'
api_hash = 'd8d30e25ef10976279733d89d601f9e4'
phone = '+62085233025941'
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
channel = "19375432"
# get all channels
channel_username = 'DataSaham2Bot'# your channel
groupUsername = "JOSS ALERT"# your group
# message = []
# for message in client.get_messages(channel_username, limit=1):
#     # get last message text
#     message = message.message
@client.on(events.NewMessage)
async def handle_new_message(event):
    if event.is_private:
        chat = event.message.message
        # if message contains picture then download it and send it
        # get user name
        user = event.message.sender_id
#         print(user)
        if user == 1623988554:
#             print("bot detected")
            if event.message.media:
                if event.message.media.photo:
                    await event.message.forward_to(groupUsername)
            else:
                await event.message.forward_to(groupUsername)
# if get new message
client.start()
client.run_until_disconnected()
