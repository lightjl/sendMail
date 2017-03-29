# !/usr/bin/env python3
# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import emailAccount
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import datetime
import email
from email import encoders

sender = 'presouce@163.com'
smtpserver = 'smtp.163.com'

def sendMail(sub, context):
    msg = MIMEText(context, _subtype='plain',_charset='gb2312')  # 中文需参数‘utf-8’，单字节字符不需要
    msg['Subject'] = Header(sub, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(emailAccount.username, emailAccount.password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

def sendToKindle(sub_folder, file_name):
    file_name = file_name + '.txt'
    receiver = 'yamieborn_1@kindle.cn'
    '''
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "convert" + str(datetime.datetime.now())
    msg['From'] = sender
    msg['To'] = "Your Kindle" + "<" + receiver + ">"
    att = MIMEText(open(os.path.join(sub_folder, file_name), 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="%s"' % file_name
    msg.attach(att)
    '''
    #msg = open(os.path.join(sub_folder, file_name), 'rb').read()
    '''
    msg = MIMEText(open(os.path.join(sub_folder, file_name), 'r').read(),'base64', _charset='utf-8')
    msg['Subject'] = "convert" + str(datetime.datetime.now())
    msg['From'] = sender
    msg['To'] = "Your Kindle" + "<" + receiver + ">"
    '''

    msg = open(os.path.join(sub_folder, file_name), 'r', encoding='utf-8').read()

    msg = MIMEText(open(os.path.join(sub_folder, file_name), 'r').read(),'base64', _charset='utf-8')
    msg['Subject'] = Header("convert" + str(datetime.datetime.now()), 'utf-8')

    server = smtplib.SMTP()
    server.connect('smtp.163.com')
    print("start login")
    server.login(emailAccount.username, emailAccount.password)
    print("start sending email")
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()

def send_attachment_kd(sub_folder, file_name):
    receiver = 'yamieborn_1@kindle.cn'
    msg = MIMEMultipart()
    msg['Subject'] = 'convert: 小说 ' + file_name
    msg['From'] = sender
    msg['To'] = "Your Kindle" + "<" + receiver + ">"
    part = email.mime.base.MIMEBase('application', "octet-stream")
    #fpath=os.path.join(KINDLE_DIR,filename)
    filename_txt = sub_folder + file_name + ".txt"
    #print filename_txt.decode('utf-8'
    filecontent=open((filename_txt),'rb').read()
    part.set_payload(filecontent)
    encoders.encode_base64(part)

    part.add_header('Content-Disposition', 'attachment', filename=file_name+ '.txt')
    msg.attach(part)

    server=smtplib.SMTP()
    server.connect('smtp.163.com')
    server.login(emailAccount.username, emailAccount.password)
    server.sendmail(sender,receiver,msg.as_string())
    server.quit()
    print("Send successfully")

'''
sub_folder = os.path.join(os.getcwd(), "/xs/")
send_attachment_kd(sub_folder, '刀镇星河 第一百零五章 雷电一型')
'''