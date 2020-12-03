
""" This module is the main controller for the web app """

#importing necessary libraries and functions
from flask import Flask, request, render_template, Markup, redirect
import pyttsx3
from datetime import date, datetime
import time
import sched
import logging
from weather_update import get_weather
from news_filter import get_headlines, get_urls
from covid_data import national_covid_stats, exe_covid_stats



logging.basicConfig(level=logging.DEBUG, filename='sys.log', format='%(levelname)s:%(message)s')
s = sched.scheduler(time.time, time.sleep)
app = Flask(__name__)
engine = pyttsx3.init()
notifications = []
disp_alarm = []
dl_alarms = []
alrm_tms = []
to_be_ann = []



@app.route('/')
def hello():
    return render_template('template.html', title='Daily Update', notificattions=notifications, image='my_alarm.jpg')


@app.route('/index')
def controller():
    s.run(blocking=False)

    check_alarms(disp_alarm)

    silent_notif()

    notif = request.args.get('notif')
    if notif:
        logging.info(' Notification deleted.')
        delete_notification(notif)

    #creating alarm based on user input
    alarm_time = request.args.get("alarm")
    if alarm_time:
        alarm_hhmm = alarm_time[-5:-3] + ':' + alarm_time[-2:]
        disp_alarm.append({'title': 'My Alarms', 'content': "You set an alarm for " + str(alarm_hhmm)})
        logging.info(' Alarm set for ' + alarm_hhmm)
        alrm_tms.append(alarm_time)

        my_weather = request.args.get('weather')
        if my_weather:
            to_be_ann.append(get_weather())
        else:
            to_be_ann.append(" ")

        my_news = request.args.get('news')
        if my_news:
            to_be_ann.append(get_headlines()[0] + get_headlines()[1] + get_headlines()[2])
        else:
            to_be_ann.append(" ")

        return redirect(request.path, code=302)


    dl_alrm = request.args.get('alarm_item')
    if dl_alrm:
        logging.info(' Alarm deleted at ' + str(time.gmtime()[3]) + ':' + str(time.gmtime()[4]))
        for num, alarm in enumerate(disp_alarm):
            if alarm['title']==dl_alrm:
                disp_alarm.remove(alarm)
                alrm_tms.remove(alrm_tms[num])
                return redirect(request.path, code=302)


    return render_template('template.html', title='Smart Alarm', notifications=notifications, image='my_alarm.jpg', alarms=disp_alarm)


def check_alarms(list_alarms):

    """ This function takes a list of alarms as it's argument, it doesn't
    return a value but the alarm goes off if the criteria is fulfilled """

    #checking data and time of alarm, if correct then alarm will go off
    now = time.gmtime()
    time_now = str(now[0]) + '-' + str(now[1]) + "-" + "0" + str(now[2]) + "T"  + str(now[3]) + ':' + str(now[4])

    for num, alarm in enumerate(list_alarms):
        if time_now == alrm_tms[num]:
            announce("Your briefing is ready." + exe_covid_stats() + to_be_ann[0] + to_be_ann[1])
            disp_alarm.remove(alarm)
            alrm_tms.remove(alrm_tms[num])

def silent_notif():

    """ This function takes no arguments. It checks the time continually
    and every hour on the hour notifies the user of headlines, weather and
    national and local covid data. """

    now = time.gmtime()
    time_now = str(now[3]) + ':' + str(now[4])

    if time_now[(len(time_now)+1)//2:] == '00':

        logging.info(" Hourly update.")
        notifications.clear()

        notifications.append({'title': 'Covid Update', 'content': national_covid_stats() + exe_covid_stats() } )
        #notifications.append({'title': 'Covid Headlines', 'content': '. '.join(get_covid_news()) })
        notifications.append({'title': 'Local Weather', 'content': get_weather()} )

        for item, val in enumerate(get_headlines()):
            notifications.append({'title': 'News', 'content': Markup(u'<a href="{url}">{headline}</a>').format(url=get_urls()[item], headline=val)})



def delete_notification(notif):

    """ This function takes a user input as it's argument, if true then
    it removes the notificaion the user wanted deleted from the list os it
    won't show on their dashboard anymore. """

    for item in notifications:
        if item['title']==notif:
            notifications.remove(item)
            return redirect(request.path, code=302)

def announce(announcement):

    """ This function takes a string as its argument that it announces to the
    user. """

    try:
        engine.endLoop()
    except:
        logging.error(' PyTTSx3 Endloop error')

    engine.say(announcement)
    engine.runAndWait()



if __name__ == '__main__':

    logging.info(' Application starting...')
    app.run()
