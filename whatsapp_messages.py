
import pip     
pip.main(["install", "--user", 'pywhatkit'])

import pywhatkit as kit
import datetime

# Phone number of the recipient (include the country code, e.g., +91 for the India)
phone_number = '+911234567890'

# Message to send
message = "Happy BirthDay"

# Set the time for sending the message (24-hour format)
send_time = datetime.datetime.now() + datetime.timedelta(minutes=1)

# Automate the WhatsApp message
kit.sendwhatmsg(phone_number, message, send_time.hour, send_time.minute)
