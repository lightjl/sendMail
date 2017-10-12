#-*- encoding: utf-8 -*-
#-*- encoding: gbk -*-

import emailAccount
from imbox import Imbox
import imaplib
import logging
import time


# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')



'''
messages_folder = eBox.messages(folder='xiaoshuo')


for uid, message in messages_folder:
# Every message is an object with the following keys
    print(message.subject)
    print((message.body)['plain'])
    eBox.move(uid, 'others')
'''

def moveMail(subject, fromFolder, toFolder):
    eBox = Imbox('imap-mail.outlook.com',
        username=emailAccount.hotname,
        password=emailAccount.hotpass,
        ssl=True,
        ssl_context=None)
    messages_folder = eBox.messages(folder=fromFolder, subject=subject)
    
    for uid, message in messages_folder:
    # Every message is an object with the following keys
        logging.debug(message.subject)
        eBox.move(uid, toFolder)
    eBox.logout()

def checkMailList(folder):
    checkFlag = True
    list_mail = []
    while checkFlag:
        try:
            checkFlag = False
            eBox = Imbox('imap-mail.outlook.com',
                    username=emailAccount.hotname,
                    password=emailAccount.hotpass,
                    ssl=True,
                    ssl_context=None)
            messages_folder = eBox.messages(folder=folder)
            for uid, message in messages_folder:
            # Every message is an object with the following keys
                logging.debug(message.subject)
                list_mail.append(message.subject)
                # print((message.body)['plain'])
            eBox.logout()
        except:
            time.sleep(10)
            checkFlag = True
        
    return list_mail



def checkMailFolderList(folderlist):
    eBox = Imbox('imap-mail.outlook.com',
        username=emailAccount.hotname,
        password=emailAccount.hotpass,
        ssl=True,
        ssl_context=None)
    list_mail = []
    for folder in folderlist:
        messages_folder = eBox.messages(folder=folder)
        for uid, message in messages_folder:
        # Every message is an object with the following keys
            logging.debug(message.subject)
            list_mail.append(message.subject)
            # print((message.body)['plain'])
    eBox.logout()
    return list_mail