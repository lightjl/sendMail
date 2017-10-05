#-*- encoding: utf-8 -*-
#-*- encoding: gbk -*-

import emailAccount
from imbox import Imbox

eBox = Imbox('imap-mail.outlook.com',
        username=emailAccount.hotname,
        password=emailAccount.hotpass,
        ssl=True,
        ssl_context=None)

messages_folder = eBox.messages(folder='others')


for uid, message in messages_folder:
# Every message is an object with the following keys
    print(message.subject)
