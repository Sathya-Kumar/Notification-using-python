import smtplib
from email.message import EmailMessage
def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "example@gmail.com"   #use your email id from which you wish to send your message from
    msg['from'] = user
    password = "abcdefghijklmnop"    #generate and use an app password for the above specified email id
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

if __name__=='__main__':
    email_alert("Batsy", "It's vigilantism time", "sathya.kum.rao@gmail.com")
