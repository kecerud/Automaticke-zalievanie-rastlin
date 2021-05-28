#! /usr/bin/env python3

from flask import Flask, render_template, redirect, url_for
import psutil
import datetime
import water
import os

app = Flask(__name__)

def template(title = "Zavlazovanie", text = ""):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timeString = now
    templateDate = {
        'title' : title,
        'time' : timeString,
        'text' : text
        }
    return templateDate

@app.route("/")
def hello():
    templateData = template()
    return render_template('main.html', **templateData)

@app.route("/naposledy_zaliate")
def check_naposledy_zaliate():
    templateData = template(text = water.get_naposledy_zaliate())
    return render_template('main.html', **templateData)

@app.route("/sensor")
def action():
    status = water.get_status()
    message = ""
    if (status == 1):
        message = "Chyba mi voda :( Zalej ma!"
    else:
        message = "Mam dostatok vody :) "

    templateData = template(text = message)
    return render_template('main.html', **templateData)

@app.route("/water")
def action2():
    water.pump_on()
    templateData = template(text = "Prave si zalial svoju rastlinu!")
    return render_template('main.html', **templateData)

@app.route("/auto/water/<toggle>")
def auto_water(toggle):
    running = False
    if toggle == "ON":
        templateData = template(text = "Automaticke zalievanie je ZAPNUTE")
        for process in psutil.process_iter():
            try:
                if process.cmdline()[1] == 'auto_water.py':
                    templateData = template(text = "Automaticke zalievanie je uz spustene.")
                    running = True
            except:
                pass
        if not running:
            os.system("python3.6 auto_water.py")
    else:
        templateData = template(text = "Automaticke zalievanie je VYPNUTE")
        water.pump_off()
        os.system("pkill -f water.py")

    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='10.3.141.1', port=81, debug=True)
