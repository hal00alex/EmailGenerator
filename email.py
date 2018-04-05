#http://effbot.org/pyfaq/how-do-i-send-mail-from-a-python-script.htm
#import smtplib
import os
from subprocess import Popen, PIPE
def main():
  print "Hello Master\n"
  sendmail_location = "insert your prefernce here" # sendmail location
  p = os.popen("%s -t" % sendmail_location, "w")
  p.write("From: %s\n" % "you@you.com")
  p.write("To: %s\n" % "person@person.com")
  p.write("Subject: Test\n")
  p.write("\n") # blank line separating headers from body
  p.write("You made an automated email")
  status = p.close()
  if status != 0:
    print "Sendmail exit status", status
  print "Goodbye Master\n"
main()
