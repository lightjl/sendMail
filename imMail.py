#-*- encoding: utf-8 -*-
#-*- encoding: gbk -*-

import emailAccount
from imbox import Imbox
import imaplib
import logging


# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')



'''
messages_folder = eBox.messages(folder='xiaoshuo')


for uid, message in messages_folder:
# Every message is an object with the following keys
    print(message.subject)
    print((message.body)['plain'])
    eBox.move(uid, 'others')
'''

def checkMailList(folder):
	eBox = Imbox('imap-mail.outlook.com',
        username=emailAccount.hotname,
        password=emailAccount.hotpass,
        ssl=True,
        ssl_context=None)
	messages_folder = eBox.messages(folder=folder)
	list_mail = []
	for uid, message in messages_folder:
	# Every message is an object with the following keys
	    logging.debug(message.subject)
	    list_mail.append(message.subject)
	    # print((message.body)['plain'])
	eBox.logout()
	return list_mail

