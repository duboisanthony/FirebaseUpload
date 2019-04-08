import datetime
import os
import json
import pyrebase

config = {
  "apiKey": "AIzaSyAIX7fYVofol2g2gBOZo9PWP8NW36ifRCw",
    "authDomain": "fir-upload-d0dfd.firebaseapp.com",
    "databaseURL": "https://fir-upload-d0dfd.firebaseio.com",
    "projectId": "fir-upload-d0dfd",
    "storageBucket": "fir-upload-d0dfd.appspot.com",
    "messagingSenderId": "76547066474"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

db = firebase.database()

storage = firebase.storage()

# THIS IS THE WORKING VERSION

#INSTAGRAM SCRAPER COMMAND: instagram-scraper wales_wanderer -u Stevony -p Balou54321! -d C:\GoogleNetworkDrive\wales_wanderer -t image --media-metadata

# data = { "owner": "OwnerTESTING",
#          "url" : "urlTest",
#          "likes": "likesTest",
#          "timestamp": "TimeStampTest"
# }
# db.child("Test1").push(data)

#db.child("instagramTest").child("https://scontent-lga3-1.cdninstagram.com/vp/9973a37784a3ce1ea201764333093aa7/5D4B802C
# /t51.2885-15/e35/52314003_130206778033363_2071471912495371069_n.jpg?_nc_ht=scontent-lga3-1.cdninstagram.com&se=7&ig_cache_key=MTk5NDA2MzA2MDg3MzM0MDU4Ng%3D%3D.2")

#WORKING
#storage.child("bucket2/lightsOUT.jpg").put("Lighthouse.jpg")

#Store pictures in Storage
user_profile = "wales_wanderer2"
directory = "C:\\GoogleNetworkDrive\\" + user_profile

# json_data = json.load(open(directory + "\\" + user_profile + '.json', encoding="utf8"))
#
# storage.child("InstagramTest3/" + "photo1" + ".jpg").put(directory + "\\" + "47583180_2020413301590828_8853182771559530135_n.jpg")
# zeurl = storage.child("InstagramTest3/" + "photo1" + ".jpg").get_url(None)
#
# for r in json_data:
#     print("Owner is : " + r['owner']['id'])
#     print("url " + r['display_url'])
#     print("likes " + str(r['edge_media_preview_like']['count']))
#     print("timestamp " + str(r['taken_at_timestamp']))


photoNumb = 0

for filename in os.listdir(directory):
  if filename.endswith(".jpg"):
    storage.child("uploads/" + str(photoNumb) + ".jpg").put(directory + "\\" + filename)
    data = {"imageUrl": storage.child("uploads/" + str(photoNumb) + ".jpg").get_url(None),
            "mGotFiltered": "false",
            "name": str(photoNumb) + ".jpg"}
    key = db.child("uploads/").push(data)
    print("Photo : " + str(photoNumb) + " uploaded")
    photoNumb += 1
    continue
  else:
    continue
