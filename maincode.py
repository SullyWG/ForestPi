
import time
import os
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

save_path = '/var/www/html'
file_name = "index.html"
theCreate = os.path.join(save_path,file_name)

while True:
        # The read_adc function will get the value of the specified channel (0-7).
        value = mcp.read_adc(1)
        if value > 1000:
                print('FIRE')
                print(value)
                f = open(theCreate,'w')

                message = """<html>
                <head></head>
                <body><p> Fire!</p></body>
                </html>"""
                f.write(message)
                f.close()

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
        #Pause for half a second.
        time.sleep(1)

