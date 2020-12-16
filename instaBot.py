from instabot import Bot
import time
import datetime

bot = Bot()
pic = "test.jpg"
User = input("Digite usuario de IG: ")
Password = input("Password: ")

def uploadPic():
    bot.login(username = User, password = Password)
    bot.upload_photo( pic, caption = "This is test from python")
    print("Logged and uploaded")


def correoAutomatizado():
    while True:
        unix = int(time.time())
        tiempo = str(datetime.datetime.fromtimestamp(unix).strftime("%I:%M:%S:%p"))
        if tiempo == "09:30:00:PM":
            uploadPic()

correoAutomatizado()      