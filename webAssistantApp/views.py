from django.shortcuts import render, redirect


# Create your views here.
dict1 = {'msg': ''}


def autoTrial(request):
    return render(request, "webAssistantApp/index.html", dict1)


def runTrial(request):
    query = request.POST['passer']

    import pyttsx3
    import datetime
    import wikipedia
    import smtplib
    import webbrowser as wb
    import psutil
    import pyjokes
    import os
    import pyautogui
    import json
    from urllib.request import urlopen
    import wolframalpha
    import time

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
        speak("The current time is")
        speak(time2)

    def date():
        year1 = datetime.datetime.now().year
        month1 = datetime.datetime.now().month
        day1 = datetime.datetime.now().day
        speak(("The current date is", day1, month1, year1))

    def wishMe():
        speak("Welcome back Mister Sibi")
        time1()
        date()

        # Greeting Statements

        hour = datetime.datetime.now().hour
        if 6 <= hour < 12:
            speak("Good Morning Sir")
        elif 12 <= hour < 18:
            speak("Good Afternoon Sir")
        elif 18 <= hour < 24:
            speak("Good Evening Sir")
        else:
            speak("Good Night Sir")

        speak("BodySoda at your service. Please tell me how can I help you today?")

    def countDown():
        global my_timer

        my_timer = 10
        for x in range(10):
            my_timer -= 1
            time.sleep(1)

    def sendEmail(to1, content1):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        server.login('rockzccp@gmail.com', 'vetbeem7311')
        server.sendmail("18bcs001@mcet.in", to1, content1)
        server.close()

    def screenshot():
        img = pyautogui.screenshot()
        img_dir = 'C:/Sibi/Python Program Screenshot Pictures'
        cnt = len(os.listdir(img_dir))
        name = '/screenshot' + str(cnt) + '.png'
        img.save(img_dir + name)

    def cpu():
        usage = str(psutil.cpu_percent())
        speak(('CPU is at', usage))

        battery = psutil.sensors_battery()
        speak(('Battery is at', battery.percent))

    def joke():
        joke1 = pyjokes.get_joke()
        print(joke1)
        dict1['msg'] = joke1
        return render(request, "webAssistantApp/index.html", dict1)

    '''
    def playMusic():
        songs_dir = 'C:/Users/cibip/Music'
        music = os.listdir(songs_dir)
        speak('What should I play?')


        def musicUtil():
            ans = takeCommand().lower()
            res = []
            if(len(ans) > 0):
                res = [i for i in music if ans in i.lower()]
            if (len(res) > 0):
                os.startfile(os.path.join(songs_dir, res[0]))
            elif 'random' in ans or 'you choose' in ans:
                no = random.randint(1, len(os.listdir(songs_dir)))
                os.startfile(os.path.join(songs_dir, music[no]))
            else:
                speak('I could not understand. Please try again')
                musicUtil()
        musicUtil()
    '''

    query = query.lower()

    if 'time' in query:
        time1()

    elif 'date' in query:
        date()

    elif 'wish' in query:
        wishMe()

    elif 'wikipedia' in query:
        speak("Searching")
        query = query.replace('wikipedia', '')
        try:
            result = wikipedia.summary(query, sentences=3)
            print(result)
            speak(('According to wikipedia', result))
        except Exception as e:
            print(e)
            speak('Some ambiguity found, please try again')

    elif 'cpu' in query or 'battery' in query:
        cpu()

    elif 'joke' in query:
        joke()

    elif 'word' in query:
        speak('Opening MS Word...')
        ms_word = r'C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE'
        os.startfile(ms_word)

    elif 'show note' in query:
        speak('showing notes')
        file = open('notes.txt', 'r')
        print(file.read())
        file.close()

    elif 'screenshot' in query or 'snap' in query:
        screenshot()
        speak('Screenshot saved, Sir')

    elif 'remember anything' in query:
        remember = open('memory.txt', 'r')
        speak('You asked me to remember that ' + remember.read())
        remember.close()

    elif 'news' in query:
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
            speak('Here are some top headline update from Business')
            print('===================TOP HEADLINES===================' + '\n')
            for item in data['articles']:
                print(str(i) + '. ' + item['title'], end='\n')
                print(item['description'], end='\n\n')
                speak(item['title'])
                i += 1
                if i > 5:
                    break

        except Exception as e:
            print(str(e))

    elif 'where is' in query:
        query = query.split('where is')
        location = query[-1]
        speak('User asked to locate ' + location)
        wb.open_new_tab('https://www.google.com/maps/place/' + location)

    elif 'calculate' in query:
        client = wolframalpha.Client(wolframalpha_app_id)
        indx = query.lower().split().index('calculate')
        query = query.split()[indx + 1:]
        res = client.query(''.join(query))
        answer = next(res.results).text
        print('The Answer is :', answer)
        speak(('The Answer is :', answer))

    elif 'what is' in query or 'who is' in query:
        client = wolframalpha.Client(wolframalpha_app_id)
        res = client.query(query)
        try:
            print(next(res.results).text)
            speak(next(res.results).text)
        except StopIteration:
            print('No results')

    elif 'logout' in query:
        os.system('shutdown -l')
    elif 'restart' in query:
        os.system('shutdown /r /t 1')
    elif 'shutdown' in query:
        os.system('shutdown /s /t 1')

    # return redirect('home')
    return render(request, "webAssistantApp/index.html", dict1)
