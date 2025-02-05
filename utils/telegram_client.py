from telethon import TelegramClient
from config import API_ID, API_HASH, BOT_TOKEN

""" 
    It's asking a phone number to sign in to account,
    but if you try to login Telegram can block your account.
    So I decided don't make it so far. Maybe I can buy a
    account to check it.
"""

with TelegramClient('anon', API_ID, API_HASH) as client:
    client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))

# client = TelegramClient('anon', API_ID, API_HASH)
#
#
# async def main():
#     me = await client.get_me()
#
#     print(me.stringify())
#
#     username = me.username
#     print(username)
#     print(me.phone)
#
#     async for dialog in client.iter_dialogs():
#         print(dialog.name, 'has ID', dialog.id)
#
#     # You can send messages to yourself...
#     await client.send_message('me', 'Hello, myself!')
#
#     message = await client.send_message(
#         'me',
#         'This message has **bold**, `code`, __italics__ and '
#         'a [nice website](https://example.com)!',
#         link_preview=False
#     )
#
#     print(message.date)
#
#     await client.send_message('me', "Cool!", reply_to=message.id)
#
#     await client.send_file('me', 'M:/Desktop/Книги/Саморазвитие/Мозг/Элленберг Джордан - Как не ошибаться. Сила математического мышления - 2017.fb2')
#
#     # You can print the message history of any chat:
#     # async for message in client.iter_messages('me'):
#     #     print(message.id, message.text)
#     #     break
#
# with client:
#     client.loop.run_until_complete(main())
