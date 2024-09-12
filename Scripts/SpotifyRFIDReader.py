import RPi.GPIO as GPIO

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from mfrc522 import MFRC522
from mfrc522 import SimpleMFRC522

from time import sleep
from datetime import datetime

DEVICE_ID="b3f6b64c79b31836c18dd14149bb5e52a7179f63"
CLIENT_ID="1db5f8d1464f4035815de3107db0deb1"
CLIENT_SECRET="25a2c263af4d44f480545d062c095737"

#Phone Device Id: "a1a8e894265575a556b26f2af2d263f2fc1dd17f"
#Mac Device Id: "d0b5e7c78058824cc2e1e895a3b5cc17d3c6bfa0" --In use
#RPi Device Id: "ff6850daf16ef9d022ec1ca134c5e88d9c9bf990"
#Windows Device Id: "b3f6b64c79b31836c18dd14149bb5e52a7179f63"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://localhost:8080/callback", scope="user-read-playback-state,user-modify-playback-state"))


reader = SimpleMFRC522()

#Reading
print("Place tag")

try:
    tagId, tagData = reader.read()
    
    fullLink = tagData.split("-") #Creates an array with the link and media tpye: ["sadjhasda7sbd7", "Playlist"]
    _mediaLink = fullLink[0] #Underscore because this has a lot of white space at the end so we strip the whitespace later and reuse variable name
    _mediaType = fullLink[1]
    
    mediaType = _mediaType.strip(" ") # Our media type without whitespace
    mediaLink = _mediaLink.strip(" ") # Our media link without whitespace
    
    sp.transfer_playback(device_id=DEVICE_ID, force_play=False) # Transfer playback to the targeted device.
    
    if mediaType == "Playlist":
        sp.shuffle(True, DEVICE_ID)
        sp.start_playback(device_id=DEVICE_ID, context_uri="spotify:playlist:" + mediaLink)
    elif mediaType == "Album":
        print("Play album")
    elif mediaType == "Song":
        sp.start_playback(device_id=DEVICE_ID, uris=["spotify:track:" + mediaLink])  
finally:
     GPIO.cleanup()


