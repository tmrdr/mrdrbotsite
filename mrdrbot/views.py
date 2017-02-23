from django.shortcuts import render, redirect
import subprocess
import sys
import mrdrbot.singleton


# Create your views here.
def index(request):
    return render(request, 'mrdrbot/index.html')


def startbot(reqest):
    mrdrbot.singleton.proc = subprocess.Popen([sys.executable, '/Users/tobiasmurphy/code/mrdrbotsite/mrdrbot.py'])
    # print(djangotwitter.singleton.proc)
    return redirect('index')

def stopbot(request):
    mrdrbot.singleton.proc.kill()
    return redirect('index')

def about(request):
    return render(request, 'mrdrbot/about.html')
