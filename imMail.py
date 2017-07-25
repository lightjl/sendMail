from imbox import Imbox
import emailAccount

# SSL Context docs https://docs.python.org/2/library/ssl.html#ssl.create_default_context

imbox = Imbox('imap.163.com',
		username= emailAccount.username,
		password= emailAccount.password,
		ssl=True,
		ssl_context=None)

boxlist = (imbox.folders())[1]
print(boxlist[6])

messages_folder = imbox.messages(folder=boxlist[6])

for uid, message in messages_folder:
    print(message.keys())