# -*- coding:utf-8 -*-
"""
    @file: voice.py
    @time: 2018/6/05
"""

import os
import time
import datetime
import pygame
import aiy.voicehat
import pywapi
var = "test"
os.environ['var'] = str(var)
os.system('sh /home/pi/aquestalkpi/talk0.sh $var')
time.sleep(1)
button = aiy.voicehat.get_button()
led = aiy.voicehat.get_led()
def ptos(name):   #python to shell
    os.system('sh /home/pi/aquestalkpi/talk0.sh ' + str(name))
    time.sleep(1)

def weather(result):
	loc = result['location']['name'] # city name
	ptos(str(loc)+"の現在の天気は")

	wtn = result['current_conditions']['text'] #now
	wtn = str(wtn)
	if "Rain" in wtn:
		wtn = "雨"
	elif "Sun" in wtn:
		wtn = "晴れ"
	ten = result['current_conditions']['temperature']
	ptos(str(wtn)+"で"+str(ten)+"度です")

	tl = result["forecasts"][0]["low"]
	th = result["forecasts"][0]["high"]
	ptos("今日の最高気温は"+str(th)+"度で、最低気温は"+str(tl)+"度です")


def mp3(): #load mp3
    pygame.mixer.init()
    pygame.mixer.music.load(r"/home/pi/lol.mp3")
    pygame.mixer.music.play()

def wakeup(h,m):#in raspberrypi  sys_nowtime = nowtime - 8(h)
    while True:
        while True:
            now = datetime.datetime.now()
            if now.hour == h and now.minute == m:
               # mp3()
                led.set_state(aiy.voicehat.LED.BLINK)
                button.wait_for_press()
              #  pygame.mixer.music.stop()
                led.set_state(aiy.voicehat.LED.OFF)
                result = pywapi.get_weather_from_weather_com('JAXX0085')
                ptos("おはようございます")
                weather(result)
               # os.environ['weather'] = "今日の天気は" + weather + "です。"
               # test = os.system('sh /home/pi/aquestalkpi/talk0.sh $weather')
                #/home/pi/Desktop/aquestalkpi/AquesTalkPi $@ | aplay
               # print(test)
                break
            time.sleep(1)
        if now.hour == h and now.minute == m:
            time.sleep(60)
            again = "一分間経過したので、再開します。"
            ptos(again)
            #os.environ['again'] = again
            #os.system('sh /home/pi/Desktop/aquestalkpi/talk0.sh $again')


if __name__ == '__main__':
    ptos("アラームを設定してください")
    h = int(input("何時？："))
    m = int(input("何分？："))
    ptos("設定完了")
    time.sleep(1)
    wakeup(h,m)  

