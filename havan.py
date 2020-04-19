import smtplib
import config
import guihav
import email_room

roomz = guihav.get_rooms() #returns list of rooms in string format
room_emails = {302:"leon.tadina@gmail.com",303:"leones.tadina@gmail.com"}

emails_with_mail = []
for r in roomz:
    if int(r) in room_emails:
        emails_with_mail.append(room_emails[int(r)])


#we want room numbers in format {302:"leon.tadina@gmail.com",301:"tony@gmail.com,..........}
#gui to get all the room numnbers that have received mail [[[[yes]]]

person = "leon.tadina@gmail.com"
def send_email(subject,message):
    
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(config.EMAIL_ADRESS, config.PASSWORD)
    message = ("Subject: %s \n\n %s" % (subject,message))
    for i in emails_with_mail:
        server.sendmail(config.EMAIL_ADRESS,i,message)
    server.quit()
    print("success email")


subj = "Hello dear havannah house resident : you have mail!"
msg = "You've got mail,come downstairs whenever to collect it.\n Have a nice day \n the staff"
send_email(subj,msg)
