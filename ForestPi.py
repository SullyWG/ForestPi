import time
import os
import Adafruit_MCP3008
import smtplib

#Email Variables
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = 'youremail@email.com' #change this to match your gmail account
GMAIL_PASSWORD = 'yourPassword'  #change this to match your gmail password

class Emailer:
    def sendmail(self, recipient, subject, content):
         
        #Create Headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: " + recipient,
                   "MIME-Version: 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)
 
        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()
 
        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
 
        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit
      
sender = Emailer()
 
sendTo = 'anotheremail@email.com'
emailSubject = "There was a Fire"
emailContent = "There was a Fire at the ForestPi location"

#Defines GPIO pins used to get data, this may change based on your wiring
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Creates path for  HTML file which will update the website
save_path = '/var/www/html'
file_name = "index.html"
theCreate = os.path.join(save_path,file_name)

i = 0

while True:
        # The read_adc function will get the value of the specified channel (0-7).
        value = mcp.read_adc(1)         #Reads ADC channel 1 for MQ-2 Input
        if value > 1000:                #If this value is greater than one, the code returns that there is a fire
                print('FIRE')
                i += 1
                print(value)
                if i >= 5:
                        f = open(theCreate,'w')
        
# Writes file and then creates it in a location for Apache to upload to our website
                        message = """<html>
                        <head></head>
                        <body><p> Fire!</p></body>
                        </html>"""
                        f.write(message)
                        f.close()
                        sender.sendmail(sendTo,emailSubject,emailContent)     #Wrote this bit of code to send me an email if there is sustained smoke for over 5 minutes so I know when to check for a fire


                        #In case there is no fire the same steps occur but the HTML will say there is no fire
                else:
                        print('NO FIRE')
                        print(value)
                        f = open(theCreate,'w')

                        message = """<html>
                        <head></head>
                        <body><p>No Fire!</p></body>
                        </html>"""

                        f.write(message)
                        f.close()
        else:
                i=0
        #Pause for half a second.
        time.sleep(60)

