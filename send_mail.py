import smtplib
from email.mime.text import MIMEText

def send_mail(student, matric_number, mahallah, rating, comments):
  port = 2525
  smtp_server = 'smtp.mailtrap.io'
  login = '811b59731fb9bb'
  password = '41d59477edad95'
  message = f"<h3>New Feedback Submission</h3><ul><li>Student : {student}</li>li>Matric Number : {matric_number}</li>li>Mahallah: {mahallah}</li>li>Rating : {rating}</li>li>Comments : {comments}</li></ul>"

  sender_email = 'ex1@ex1.com'
  reciever_email = 'ex2@ex1.com'
  msg = MIMEText(message, 'html')
  msg['Subject'] = 'Cafe Feedback'
  msg['From'] = send_mail
  msg['To'] = reciever_email

  #send mail'
  with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    #server.login(login, password)
    server.login("811b59731fb9bb", "41d59477edad95")
    server.sendmail(sender_email, reciever_email, msg.as_string())