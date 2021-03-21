import time
import os
import Adafruit_MCP3008

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

