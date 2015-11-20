#Author:L337H4X0R
#Purpose: Pull Suspected Accounts, Report for abuse.
#Installation Instructions
#Make sure you have GMAIL less secure apps setup
import smtplib
from time import sleep
import urllib.request
import json
import urllib

try:
    from urllib.error import URLError
except ImportError:
    from urllib2 import URLError  # python 2

def main():
    while True:
        url = 'http://URLHERE/api2.php'
        r = urllib.request.urlopen(url)
        data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
        for details in data:
            dbID = details['id']
            jihadiUsername = details['username']
            jihadiID = details['suspectid']
            jihadiText = details['msg']
        to = 'abuse@telegram.org'
        gmail_user = 'GMAILUSERNAME'
        gmail_pwd = 'GMAILPWD'
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        smtpserver.login(gmail_user, gmail_pwd)
        header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:Abuse-ISIS \n'
        msg = header + '\n Hello,\n We have detected a ISIS account using your telegram service.\n Account UserName:' + jihadiUsername + '(id=' + jihadiID +')\n The user sent the following in a suspected ISIS groupchat:\n' + jihadiText +'\n Thanks for your support \n\n'
        smtpserver.sendmail(gmail_user, to, msg)
        print ("Email Sent!")
        smtpserver.close()
        url = ('http://URLHERE/api2.php')
        data = urllib.parse.urlencode({'id'  : jihadiID})
        binary_data = data.encode('ascii')
        content = urllib.request.urlopen(url,binary_data)





















if __name__ == '__main__':
    main()
