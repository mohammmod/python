import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("useremail", "password")

msg = "this is just my first python massge !"
server.sendmail("from whom", "to whoem", msg)
server.quit()
