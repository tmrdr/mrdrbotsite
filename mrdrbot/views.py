from django.shortcuts import render, redirect
import subprocess
import sys
import mrdrbot.singleton
from .models import TextFood, Toggled


# Create your views here.
def index(request):
    context = {
        "textfoods": TextFood.objects.values('id', 'name'),
        "botstatus": Toggled.objects.values('id', 'onstatus')
    }
    print(context)
    return render(request, 'mrdrbot/index.html', context)


def startbot(reqest):
    mrdrbot.singleton.proc = subprocess.Popen([sys.executable, 'mrdrbot.py'])
    Toggled.objects.filter(id=1).update(onstatus = True)
    # print(djangotwitter.singleton.proc)
    return redirect('index')

def stopbot(request):
    mrdrbot.singleton.proc.kill()
    Toggled.objects.filter(id=1).update(onstatus = False)
    return redirect('index')

def update(request):
    request.GET['content']
    print("This is user selection: ", request.GET['content'])

    with open('botfood.txt', 'r') as botfood:
        first_line = botfood.readline().rstrip()
        leftover_text = botfood.read()
        whole_text = first_line + '\n' + leftover_text

        print("This is current botfood.txt: ", first_line)

    TextFood.objects.filter(name=first_line).update(food = whole_text)

    to_be_loaded = TextFood.objects.filter(name = request.GET['content'])

    for loaded in to_be_loaded:
        freshBotFood = loaded.food

    with open('botfood.txt', 'w') as botfood:
        botfood.write(freshBotFood)

    return redirect('index')

def about(request):
    return render(request, 'mrdrbot/about.html')
