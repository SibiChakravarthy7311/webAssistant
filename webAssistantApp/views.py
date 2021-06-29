from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "90f88c6b30msh6878bf751006f7ap146ef6jsnde0275613b83",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
dict1 = {'success': True, 'speak': False, 'msg': '', 'music': False, 'mail': False, 'chrome': False, 'music1': False,
         'youtube': False, 'google': False, 'todo': False, 'snake': False, 'web': False, 'iframe': False,
         'covid': False, 'web1': False, 'curr_id': 1, 'id': 0, 'head': False, 'para': False, 'text': '', 'color': '',
         'fine': False, 'weather': False, 'songIndex': 10, 'downloadTemplate': False, 'exit': False, 'note': False,
         'memory': False}
# 'colorAction': False, 'centreAction': False, 'backGroundAction': False


def autoTrial(request):
    return render(request, "webAssistantApp/index.html", dict1)


def sendEmail(request):
    import smtplib
    import pyttsx3
    engine = pyttsx3.init()
    voice_id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice', voice_id)

    def speak(audio):
        try:
            engine.say(audio)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print(e)

    dict1['mail'] = False
    to1 = request.POST['email']
    content1 = request.POST['mailContent']
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('rockzccp@gmail.com', 'vetbeem7311')
    server.sendmail('rockzccp@gmail.com', to1, content1)
    server.close()
    speak("Mail has been sent successfully")
    return redirect('home')


def mailView(request):
    return render(request, "webAssistantApp/mailAssistant.html")


def speakOut(request):
    text = request.POST.get('Data')
    import pyttsx3
    import json
    engine = pyttsx3.init()
    voice_id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice', voice_id)

    def speak(audio):
        try:
            # print('Speak :', audio)
            engine.say(audio)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print(e)
    speak(text)
    dict1['speak'] = False
    return HttpResponse(json.dumps(dict1), content_type='application/json')


def thankYou(request):
    dict1['exit'] = False
    return render(request, "webAssistantApp/thankYou.html")


def iframe(request):
    return render(request, "webAssistantApp/frameSource.html")


def runTrial(request):
    query = request.POST.get('Data')
    dict1['speak'] = False
    dict1['todo'] = False
    dict1['snake'] = False
    dict1['music1'] = False
    dict1['downloadTemplate'] = False
    dict1['msg'] = ''
    # dict1['centreAction'] = False
    # dict1['backGroundAction'] = False
    # dict1['colorAction'] = False
    print(query)

    import pyttsx3
    import datetime
    import wikipedia
    import webbrowser as wb
    import psutil
    import pyjokes
    import os
    import pyautogui
    import json
    from urllib.request import urlopen
    import wolframalpha
    import time
    import random

    engine = pyttsx3.init()
    voice_id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice', voice_id)
    wolframalpha_app_id = 'R5XHR5-A8RHLALLTA'

    def speak(audio):
        try:
            # print('Speak :', audio)
            engine.say(audio)
            engine.runAndWait()
            engine.stop()
        except Exception as e:
            print(e)

    def time1():
        time2 = datetime.datetime.now().strftime("%H:%M:%S")  # 24 hour clock
        # speak("The current time is")
        # speak(time2)
        dict1['msg'] = "The current time is "+time2
        dict1['speak'] = True

    def date():
        year1 = datetime.datetime.now().year
        month1 = datetime.datetime.now().month
        day1 = datetime.datetime.now().day
        dict1['msg'] = "The current date is " + str(day1) + " " + str(month1) + " " + str(year1)
        dict1['speak'] = True

    def wishMe():
        text = "Welcome back Mister Sibi. The current time is "
        time2 = datetime.datetime.now().strftime("%H:%M:%S")
        text += time2
        year1 = datetime.datetime.now().year
        month1 = datetime.datetime.now().month
        day1 = datetime.datetime.now().day
        text += ". The current date is " + str(day1) + " " + str(month1) + " " + str(year1)
        date()

        # Greeting Statements

        hour = datetime.datetime.now().hour
        if 6 <= hour < 12:
            text += ". Good Morning Sir. "
        elif 12 <= hour < 18:
            text += ". Good Afternoon Sir. "
        elif 18 <= hour < 24:
            text += ". Good Evening Sir. "
        else:
            text += ". Good Night Sir. "

        text += "EIKO at your service. Please tell me how can I help you today?"
        dict1['msg'] = text
        dict1['speak'] = True

    def countDown():
        global my_timer

        my_timer = 10
        for x in range(10):
            my_timer -= 1
            time.sleep(1)

    def screenshot():
        img = pyautogui.screenshot()
        img_dir = 'C:/Sibi/Python Program Screenshot Pictures'
        cnt = len(os.listdir(img_dir))
        name = '/screenshot' + str(cnt) + '.png'
        img.save(img_dir + name)
        dict1['msg'] = "Screenshot stored at directory "+img_dir
        dict1['speak'] = True

    def cpu():
        usage = str(psutil.cpu_percent())
        text = 'CPU is at ' + usage + "% usage"

        battery = psutil.sensors_battery()
        text += '. Battery level is ' + str(battery.percent) + "%"
        dict1['msg'] = text
        dict1['speak'] = True

    def joke():
        joke1 = pyjokes.get_joke()
        print(joke1)
        # dict1 = {'success': True, 'msg': ''}
        dict1['msg'] = joke1
        dict1['speak'] = True
        # return HttpResponse(json.dumps(dict1), content_type='application/json')
        # return render(request, "webAssistantApp/index.html", dict1)

    query = query.lower()

    if dict1['web']:
        if 'stop' in query:
            dict1['web'] = False
            dict1['iframe'] = False
            dict1['msg'] = 'Web development assistant has closed the session'
            dict1['speak'] = True
        elif 'download' in query:
            dict1['downloadTemplate'] = True
            dict1['msg'] = 'Template is now downloading'
            dict1['speak'] = True
        elif 'clear' in query:
            stylepath = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/css/frameSourceStyle.css'
            stylepath1 = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/css/frameSourceStyle1.css'
            filepath = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/templates/webAssistantApp/frameSource.html'
            filepath1 = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/css/template.html'
            file = open(stylepath, 'w')
            file1 = open(stylepath1, 'w')
            file2 = open(filepath, 'w')
            file3 = open(filepath1, 'w')
            file.write('img{\n\theight: 130px;\n\twidth: 130px;\n}\n')
            file1.write('img{\n\theight: 130px;\n\twidth: 130px;\n}\n')
            file2.write('<!DOCTYPE html>\n<html>\n\t<head>\n\t\t{% load static %}\n\t\t<!--<link rel="stylesheet" '
                        'href="{% static \'webAssistantApp/css/frameSourceStyle.css\' %}">-->\n\t\t<link '
                        'rel="stylesheet" href="{% static \'webAssistantApp/css/frameSourceStyle1.css\' '
                        '%}">\n\t</head>\n\n\t<body>\n\t</body>\n</html>')
            file3.write('<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>EIKO Web Assistant '
                        'Template</title>\n\t\t<link rel="stylesheet" '
                        'href="frameSourceStyle.css">\n\t</head>\n\t<body>\n\t</body>\n</html>')
            file.close()
            file1.close()
            file2.close()
            file3.close()
            obj = outlierElementModel.objects.filter(name='LastElement')[0]
            obj.id = 0
            obj.save()
            dict1['curr_id'] = 0
            dict1['msg'] = 'Template cleared'
            dict1['speak'] = True
        elif 'make' in query or 'change' in query:
            if 'centre' in query:
                # dict1['centreAction'] = True
                filepath = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/css/frameSourceStyle.css'
                filepath1 = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/css/frameSourceStyle1.css'
                file = open(filepath, 'a')
                file1 = open(filepath1, 'a')
                file.write('\n#i' + str(dict1['curr_id']) + '{\n\ttext-align: center;\n}\n')
                file1.write('\n#i' + str(dict1['curr_id']) + '{\n\ttext-align: center;\n}\n')
                file.close()
                file1.close()
                dict1['msg'] = "Aligned to centre"
            elif 'back' in query or 'background' in query:
                query = query.split()[-1]
                dict1['color'] = query
                # dict1['backGroundAction'] = True
                filepath = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/css/frameSourceStyle.css'
                filepath1 = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/css/frameSourceStyle1.css'
                file = open(filepath, 'a')
                file1 = open(filepath1, 'a')
                file.write('\n#i' + str(dict1['curr_id']) + '{\n\tbackground-color: ' + query + ';\n}\n')
                file1.write('\n#i' + str(dict1['curr_id']) + '{\n\tbackground-color: ' + query + ';\n}\n')
                file.close()
                file1.close()
                dict1['msg'] = "Background color changed to " + query
            elif 'round' in query or "circle" in query:
                filepath = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/css/frameSourceStyle.css'
                filepath1 = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/css/frameSourceStyle1.css'
                file = open(filepath, 'a')
                file1 = open(filepath1, 'a')
                file.write('\n.i' + str(dict1['curr_id']) + '{\n\tborder-radius: 50%;\n}\n')
                file1.write('\n.i' + str(dict1['curr_id']) + '{\n\tborder-radius: 50%;\n}\n')
                file.close()
                file1.close()
                dict1['msg'] = "Shaped to round"
            else:
                query = query.split()[-1]
                dict1['color'] = query
                # dict1['colorAction'] = True
                filepath = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/css/frameSourceStyle.css'
                filepath1 = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/css/frameSourceStyle1.css'
                file = open(filepath, 'a')
                file1 = open(filepath1, 'a')
                file.write('\n#i' + str(dict1['curr_id']) + '{\n\tcolor: ' + query + ';\n}\n')
                file1.write('\n#i' + str(dict1['curr_id']) + '{\n\tcolor: ' + query + ';\n}\n')
                file.close()
                file1.close()
                dict1['msg'] = "Text color changed to " + query
            dict1['speak'] = True
        elif dict1['web1']:
            dict1['web1'] = False
            if dict1['head']:
                dict1['head'] = False
                filepath = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/templates/webAssistantApp/frameSource.html'
                filepath1 = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/css/template.html'
                file = open(filepath, 'a')
                file1 = open(filepath1, 'a')
                file.seek(file.seek(0, 2) - 22)
                query = query.strip().capitalize()
                file.write('\n<h1 id="i' + str(dict1['curr_id']) + '">' + query + '</h1>')
                file1.write('\n<h1 id="i' + str(dict1['curr_id']) + '">' + query + '</h1>')
                file.close()
                file1.close()
                dict1['msg'] = 'Heading added'
            elif dict1['para']:
                dict1['para'] = False
                filepath = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/templates/webAssistantApp/frameSource.html'
                filepath1 = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/css/template.html'
                file = open(filepath, 'a')
                file1 = open(filepath1, 'a')
                file.seek(file.seek(0, 2) - 22)
                query = query.strip().capitalize()
                file.write('\n<p id="i' + str(dict1['curr_id']) + '">' + query + '</p>')
                file1.write('\n<p id="i' + str(dict1['curr_id']) + '">' + query + '</p>')
                file.close()
                file1.close()
                dict1['msg'] = 'Paragraph added'
            dict1['speak'] = True
        else:
            if 'add' in query or 'new' in query:
                if 'break' in query or 'line' in query:
                    filepath = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/templates/webAssistantApp/frameSource.html'
                    filepath1 = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/css/template.html'
                    file = open(filepath, 'a')
                    file1 = open(filepath1, 'a')
                    file.seek(file.seek(0, 2) - 22)
                    file.write('\n<br>')
                    file1.write('\n<br>')
                    file.close()
                    file1.close()
                    dict1['msg'] = "Line break added"
                elif 'image' in query:
                    imgSrc = '<img src="https://source.unsplash.com/collection/190727/300x300" alt="Randome Images">'
                    obj = outlierElementModel.objects.filter(name='LastElement')[0]
                    currid = obj.id
                    currid += 1
                    obj.id = currid
                    obj.save()
                    dict1['curr_id'] = currid
                    filepath = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/templates/webAssistantApp/frameSource.html'
                    filepath1 = 'C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/css/template.html'
                    file = open(filepath, 'a')
                    file1 = open(filepath1, 'a')
                    file.write('\n<div id="i' + str(dict1['curr_id']) + '">\n\t<img class="i' + str(dict1['curr_id']) +
                               '" src="https://source.unsplash.com/collection/190727/300x300" alt="Random '
                               'Image">\n</div>')
                    file1.write('\n<div id="i' + str(dict1['curr_id']) + '">\n\t<img class="i' + str(dict1['curr_id']) +
                               '" src="https://source.unsplash.com/collection/190727/300x300" alt="Random '
                               'Image">\n</div>')
                    file.close()
                    file1.close()
                    dict1['msg'] = 'Image added'
                elif 'heading' in query or 'setting' in query:
                    obj = outlierElementModel.objects.filter(name='LastElement')[0]
                    currid = obj.id
                    currid += 1
                    obj.id = currid
                    obj.save()
                    dict1['curr_id'] = currid
                    dict1['msg'] = "Say the text to add to the heading"
                    dict1['web1'] = True
                    dict1['head'] = True
                elif 'para' in query or 'paragraph' in query:
                    obj = outlierElementModel.objects.filter(name='LastElement')[0]
                    currid = obj.id
                    currid += 1
                    obj.id = currid
                    obj.save()
                    dict1['curr_id'] = currid
                    dict1['msg'] = "Say the text to add to the paragraph"
                    dict1['web1'] = True
                    dict1['para'] = True

            dict1['iframe'] = True
            dict1['speak'] = True

    elif dict1['music']:
        query = query.lower()
        i = 0
        songs_dir = 'C:/Sibi/HTML Files/Web Dev Learning/JSMusicPlayer/music'
        music = os.listdir(songs_dir)
        if 'random' in query or 'you choose' in query or 'any song' in query:
            i = random.randint(1, len(music))
            dict1['music'] = False
            dict1['music1'] = True
            dict1['songIndex'] = i
            dict1['msg'] = 'Your song ' + music[i] + ' is now ready'
            dict1['speak'] = True
        else:
            while i < len(music):
                if query in music[i].lower():
                    dict1['music'] = False
                    dict1['music1'] = True
                    dict1['songIndex'] = i
                    dict1['msg'] = 'Your song' + music[i] + ' is now ready'
                    dict1['speak'] = True
                    break
                i += 1
            if not dict1['music1']:
                dict1['msg'] = 'Song unavailable. Please try another song'
                dict1['speak'] = True

    elif dict1['chrome']:
        dict1['chrome'] = False
        chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        wb.get(chromepath).open_new_tab(query + '.com')
        dict1['msg'] = query+".com result displayed in new tab"
        dict1['speak'] = True

    elif dict1['youtube']:
        dict1['youtube'] = False
        wb.open('https://www.youtube.com/results?search_query=' + query)
        dict1['msg'] = query + " youtube search result displayed in new tab"
        dict1['speak'] = True

    elif dict1['google']:
        dict1['google'] = False
        wb.open('https://www.google.com/search?q=' + query)
        dict1['msg'] = query + " google search result displayed in new tab"
        dict1['speak'] = True

    elif dict1['fine']:
        dict1['fine'] = False
        if 'fine' in query or "good" in query:
            dict1['msg'] = "It's good to know that you're fine"
        else:
            dict1['msg'] = "I hope you get well soon."
        dict1['speak'] = True

    elif dict1['weather']:
        dict1['weather'] = False
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=2dd1a460cf060c222ccc60a90cf4d461'.format(query.capitalize())
        res = requests.get(url)
        x = res.json()

        if x["cod"] != "404":
            current_temperature = x["main"]["temp"] - 273.15
            current_pressure = x["main"]["pressure"]
            current_humidiy = x["main"]["humidity"]
            weather_description = x["weather"][0]["description"]
            dict1['msg'] = "Weather report for " + query.capitalize() +".\n Temperature (in celsius) = " + str(current_temperature) + ".\n Atmospheric pressure (in hPa unit) =" + str(
                current_pressure) + ".\n Humidity (in percentage) = " + str(current_humidiy) + ".\n Weather Description = " + str(
                weather_description)

        else:
            dict1['msg'] = " City Not Found "
        dict1['speak'] = True

    elif dict1['note']:
        dict1['note'] = False
        file = open('C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/note files/notes.txt', 'a')
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().month)
        day = str(datetime.datetime.now().day)
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        file.write(day + '-' + month + '-' + year + ' ')
        file.write(strTime)
        file.write(':-')
        file.write(query.capitalize() + "\n")
        file.close()
        dict1['msg'] = 'Done taking notes, Sir'
        dict1['speak'] = True

    elif dict1['memory']:
        dict1['memory'] = False
        speak('You asked me to remember that ' + query.capitalize())
        remember = open('C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/note files/memory.txt', 'a')
        remember.write(query.capitalize() + '\n')
        remember.close()

    elif 'how are you' in query:
        dict1['msg'] = "I am fine Sir. Thanks for asking. How are you Sir?"
        dict1['fine'] = True
        dict1['speak'] = True

    elif "i love you" in query:
        dict1['msg'] = "It's hard to understand, I am still trying to figure this out."
        dict1['speak'] = True

    elif "will you be my gf" in query or "will you be my bf" in query or "bf" in query or "gf" in query:
        dict1['msg'] = "I'm not sure about, may be you should give me some time"
        dict1['speak'] = True

    elif 'introduce' in query or 'who are you' in query or 'what can you' in query or 'creator' in query:
        dict1['msg'] = "I am EIKO, Personal Web assistant, created by Develappers team - Sibi, " \
                       "Siddhu and Jeevithan. \nI can help you in various regards. \nI can search for you on internet. " \
                       "\nI can grab definition for you from wikipedia. \nI can tell you the latest news headlines. " \
                       "\nI can play Music. \nI can maintain your todo tasks. \nI can track covid-19 status. \nI can " \
                       "send emails. \nI can also help you in building a basic webpage. "
        dict1['speak'] = True

    elif 'time' in query:
        time1()

    elif 'date' in query:
        date()

    elif 'wish' in query:
        wishMe()

    elif 'wikipedia' in query:
        query = query.replace('wikipedia', '')
        try:
            result = wikipedia.summary(query, sentences=3)
            dict1['msg'] = 'According to wikipedia, ' + result
        except Exception as e:
            print(e)
            dict1['msg'] = 'Some ambiguity found, please try again'
        dict1['speak'] = True

    elif 'cpu' in query or 'battery' in query or 'status' in query:
        cpu()

    elif "who am i" in query:
        dict1['msg'] = "If you are talking to me, then most probably you are a human"
        dict1['speak'] = True

    elif "why" in query and "this world" in query:
        dict1['msg'] = "Thanks to the Develappers team. Further it is a secret"
        dict1['speak'] = True

    elif 'love' in query:
        dict1['msg'] = "It is 7th sense that destroy all other senses , And I think it is just a mere illusion , " \
                       "It is waste of time "
        dict1['speak'] = True

    elif 'joke' in query:
        joke()

    elif 'email' in query:
        dict1['mail'] = True
        # return render(request, "webAssistantApp/mailAssistant.html")

    elif 'music' in query:
        dict1['msg'] = 'Tell a song to play'
        dict1['speak'] = True
        dict1['music'] = True

    elif 'word' in query:
        ms_word = r'C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE'
        os.startfile(ms_word)
        dict1['msg'] = 'Opening Microsoft Word'
        dict1['speak'] = True

    elif 'chrome' in query:
        dict1['msg'] = "What should I search?"
        dict1['chrome'] = True
        dict1['speak'] = True

    elif 'youtube' in query:
        dict1['msg'] = "What should I search?"
        dict1['youtube'] = True
        dict1['speak'] = True

    elif 'google' in query:
        dict1['msg'] = "What should I search?"
        dict1['google'] = True
        dict1['speak'] = True

    elif 'todo' in query or 'tasks' in query or ('open' in query and 'app' in query):
        dict1['msg'] = "Opening Todo Tasks app"
        dict1['todo'] = True
        dict1['speak'] = True

    elif 'snake' in query  and 'game' in query:
        dict1['msg'] = "Opening Snake Babu Game"
        dict1['snake'] = True
        dict1['speak'] = True

    elif ('start' in query and 'web' in query) or 'development' in query:
        dict1['web'] = True
        dict1['msg'] = "Web Development assistant is ready for you commands"
        dict1['speak'] = True

    elif 'write a note' in query:
        dict1['note'] = True
        dict1['msg'] = 'What should I write, Sir?'
        dict1['speak'] = True

    elif 'show note' in query:
        file = open('C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/note files/notes.txt', 'r')
        note = file.read()
        file.close()
        dict1['msg'] = note
        dict1['speak'] = True

    elif 'remember that' in query:
        dict1['msg'] = 'What should I remember?'
        dict1['speak'] = True
        dict1['memory'] = True

    elif 'remember anything' in query:
        remember = open('C:/Sibi/HTML Files/Web Dev Learning/bodysodaWebAssistant/static/webAssistantApp/note files/memory.txt', 'r')
        dict1['msg'] = 'You asked me to remember that ' + remember.read()
        remember.close()
        dict1['speak'] = True

    elif 'covid' in query:
        dict1['covid'] = True
        dict1['msg'] = "Opening Covid-19 Data App"
        dict1['speak'] = True

    elif 'screenshot' in query or 'snap' in query:
        screenshot()

    elif 'news' in query:
        msg = ''
        try:
            # api key - 4cb8882338d245f0b2e2ee635fc3e927
            jsonObject = urlopen(
                'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey'
                '=4cb8882338d245f0b2e2ee635fc3e927')
            # jsonObject = urlopen('https://newsapi.org/v2/everything?q=tesla&from=2021-02-24&sortBy=publishedAt
            # &apiKey=4cb8882338d245f0b2e2ee635fc3e927')
            data = json.load(jsonObject)
            i = 1

            # speak('Here are some top headline update from tesla')
            msg += 'Here are some top headline update from Business.\n'

            for item in data['articles']:
                if item['title'] != None and item['description'] != None:
                    msg += str(i) + '. ' + item['title'] + '. \n'
                    msg += item['description'] + '. \n\n'
                    i += 1
                    if i > 5:
                        break
            dict1['msg'] = msg
            dict1['speak'] = True
        except Exception as e:
            dict1['msg'] = "Some error Occured: " + str(e) + ". Please try again."
            dict1['speak'] = True

    elif 'weather' in query:
        dict1['weather'] = True
        dict1['msg'] = "Mention a city name for weather report"
        dict1['speak'] = True

    elif 'where is' in query:
        query = query.split('where is')
        location = query[-1]
        text = 'User asked to locate ' + location + '. Google map location will be displayed in a new tab'
        wb.open_new_tab('https://www.google.com/maps/place/' + location)
        dict1['msg'] = text
        dict1['speak'] = True

    elif 'locate' in query:
        query = query.split('locate')
        location = query[-1]
        text = 'User asked to locate ' + location + '. Google map location will be displayed in a new tab'
        wb.open_new_tab('https://www.google.com/maps/place/' + location)
        dict1['msg'] = text
        dict1['speak'] = True

    elif 'calculate' in query:
        client = wolframalpha.Client(wolframalpha_app_id)
        indx = query.lower().split().index('calculate')
        query = query.split()[indx + 1:]
        res = client.query(''.join(query))
        answer = next(res.results).text
        text = 'The Answer is : ' + answer
        dict1['msg'] = text
        dict1['speak'] = True

    elif 'calculator' in query:
        client = wolframalpha.Client(wolframalpha_app_id)
        indx = query.lower().split().index('calculator')
        query = query.split()[indx + 1:]
        res = client.query(''.join(query))
        answer = next(res.results).text
        text = 'The Answer is : ' + answer
        dict1['msg'] = text
        dict1['speak'] = True

    elif 'what is' in query or 'who is' in query or 'when' in query:
        client = wolframalpha.Client(wolframalpha_app_id)
        res = client.query(query)
        try:
            text = next(res.results).text
        except StopIteration:
            text = 'No results'
        dict1['msg'] = text
        dict1['speak'] = True

    elif 'go offline' in query:
        dict1['msg'] = "Thank you for using the EIKO Web Assistant. Let's meet again soon :)"
        dict1['speak'] = True
        dict1['exit'] = True
    '''
    elif 'logout' in query:
        os.system('shutdown -l')
    elif 'restart' in query:
        os.system('shutdown /r /t 1')
    elif 'shutdown' in query:
        os.system('shutdown /s /t 1')
    '''

    return HttpResponse(json.dumps(dict1), content_type='application/json')


def covidWorldView(request):
    dict1['covid'] = False
    countryList = []
    result = len(response['response'])
    for x in range(0, result):
        countryList.append(response['response'][x]['country'])
    countryList.sort()

    if request.method=="POST":
        selectedCountry = request.POST['selectedCountry']

        for x in range(0, result):
            if selectedCountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = total - active - critical - recovered

        context = {'selectedCountry': selectedCountry, 'countryList': countryList, 'new': new, 'active': active,
                   'critical': critical, 'recovered': recovered, 'total': total, 'deaths': deaths}
        return render(request, 'webAssistantApp/covidWorld.html', context)

    context = {'countryList': countryList}
    return render(request, 'webAssistantApp/covidWorld.html', context)


def snakeBabuView(request):
    return render(request, 'webAssistantApp/snakeBabu.html')
