import os

def pullrestart():
    os.system("git pull https://jordanchiquet:E4miqtng14+12@github.com/jordanchiquet/disbot.git")
    os.system("sudo systemctl restart disbotren")