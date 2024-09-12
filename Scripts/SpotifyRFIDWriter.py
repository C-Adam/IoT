import RPi.GPIO as GPIO

from mfrc522 import MFRC522
from mfrc522 import SimpleMFRC522
from time import sleep
from datetime import datetime

reader = SimpleMFRC522()

#Writing
_mediaLink = input("Input album/song link: ")
mediaType = input("What type of media is this? (Song, Playlist, Album) ")

mediaLink = _mediaLink.strip(" ")

fullLink = mediaLink + "-" + mediaType

print("Place tag to write the album/song to")
try:
    reader.write(fullLink)
    print("Successfuly written:")
    print("Card Id:", reader.read()[0])
    print("Card Data:", reader.read()[1])
finally:
    GPIO.cleanup()

