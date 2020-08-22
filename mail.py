# Credits to TutorialsPoint.com https://www.tutorialspoint.com/python/python_sending_email.htm
import smtplib

sender = 'safinzaman@outlook.com'
receivers = ['safinzaman@outlook.com']

message = """From: From Person <safinzaman@outlook.com>
To: To Person <safinzaman@outlook.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print "Successfully sent email"
except SMTPException:
   print "Error: unable to send email"