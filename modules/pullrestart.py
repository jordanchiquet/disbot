import subprocess

def pullrestart():
    subprocess.call("git pull https://jordanchiquet:E4miqtng14+12@github.com/jordanchiquet/disbot.git")
    subprocess.call("sudo systemctl restart disbotren")