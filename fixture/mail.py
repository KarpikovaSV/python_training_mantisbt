import poplib
import email
import quopri
import time
from email.parser import Parser


class MailHelper:

    def __init__(self, app):
        self.app = app

    def get_mail(self, username, password, subject):
        for i in range(15):
            pop = poplib.POP3(self.app.config['james']['host'])
            pop.user(username)
            pop.pass_(password)
            num = pop.stat()[0]
            if num > 0:
                for n in range(num):
                    msglines = pop.retr(n+1)[1]
                    msgtext = "\n".join(map(lambda x: x.decode('utf-8'), msglines))
                    msgtextEncoded = quopri.decodestring(msgtext)
                    msgtextEncoded2 = msgtextEncoded.decode('utf-8')
                    msg = email.message_from_string(msgtextEncoded2)
                    # msg = email.message_from_string(msgtext)
                    msg_subject = msg.get("Subject")
                    if subject in msg_subject:
                        pop.dele(n+1)
                        pop.quit()
                        return msg.get_payload()
            pop.close()
            time.sleep(3)
        return None

