import RPi.GPIO as GPIO

from mfrc522 import MFRC522
from mfrc522 import SimpleMFRC522
from time import sleep
from datetime import datetime

reader = SimpleMFRC522()

#Writing
text = input("New Data: ")
print("Place tag")

try:
    reader.write(text)
    tagId, writtenText = reader.read()
    print("Written:", writtenText)
finally:
    GPIO.cleanup()


#Reading
'''
print("Place tag")

tagId, writtenText = reader.read()

try:
    print("Tag Id:", tagId)
    print("Written Text:", writtenText)
finally:
    GPIO.cleanup()
'''
