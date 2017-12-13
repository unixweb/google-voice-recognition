#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Run a recognizer using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio. Hot word detection "OK, Google" is supported.

The Google Assistant Library can be installed with:
    env/bin/pip install google-assistant-library==0.0.2

It is available for Raspberry Pi 2/3 only; Pi Zero is not supported.
"""

import logging
import subprocess
import sys

import aiy.assistant.auth_helpers
import aiy.audio
import aiy.voicehat
from google.assistant.library import Assistant
from google.assistant.library.event import EventType
aiy.i18n.set_language_code('de-DE')

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)


GET_VOLUME = r'amixer get Master | grep "Front Left:" | sed "s/.*\[\([0-9]\+\)%\].*/\1/"'
SET_VOLUME = 'amixer -q set Master %d%%'


def power_off_pi():
    aiy.audio.say('Good bye!')
    subprocess.call('sudo shutdown now', shell=True)


def reboot_pi():
    aiy.audio.say('Wir sehen uns gleich wieder')
    subprocess.call('sudo reboot', shell=True)


def say_ip():
    ip_address = subprocess.check_output("hostname -I | cut -d' ' -f1", shell=True)
    aiy.audio.say('My IP address is %s' % ip_address.decode('utf-8'))

def say_internet_ip():
    internet_address = subprocess.check_output("wget -qO- ifconfig.co", shell=True)
    aiy.audio.say('My IP address is %s' % internet_address.decode('utf-8'))

def say_turn_tablelamp_on():
    aiy.audio.say('Schalte Tischlampe ein')
    subprocess.call('mosquitto_pub -h mqtt.unixweb.de -t lamp1 -m "ON"', shell=True)

def say_turn_tablelamp_off():
    aiy.audio.say('Schalte Tischlampe aus')
    subprocess.call('mosquitto_pub -h mqtt.unixweb.de -t lamp1 -m "OFF"', shell=True)

# Unicorn HAT 
def say_turn_pi_blue():
    aiy.audio.say('Schalte Pi auf Blau')
    subprocess.call('mosquitto_pub -h mqtt.unixweb.de -t mygoogleassistant -m "blue"', shell=True)

def say_turn_pi_red():
    aiy.audio.say('Schalte Pi auf Rot')
    subprocess.call('mosquitto_pub -h mqtt.unixweb.de -t mygoogleassistant -m "red"', shell=True)

def say_turn_pi_green():
    aiy.audio.say('Schalte Pi auf Grün')
    subprocess.call('mosquitto_pub -h mqtt.unixweb.de -t mygoogleassistant -m "green"', shell=True)

def say_turn_pi_clear():
    aiy.audio.say('Schalte Pi aus')
    subprocess.call('mosquitto_pub -h mqtt.unixweb.de -t mygoogleassistant -m "clear"', shell=True)



def set_volume(change):
    old_vol = subprocess.check_output(GET_VOLUME, shell=True).strip()
    try:
        logging.info("volume: %s", old_vol)
        new_vol = max(0, min(100, int(old_vol) + change))
        subprocess.call(SET_VOLUME % new_vol, shell=True)
        aiy.audio.say('Volume at %d %%.' % new_vol)
    except (ValueError, subprocess.CalledProcessError):
        logging.exception("Error using amixer to adjust volume.")

def process_event(assistant, event):
    status_ui = aiy.voicehat.get_status_ui()
    if event.type == EventType.ON_START_FINISHED:
        status_ui.status('ready')
        if sys.stdout.isatty():
            print('Say "OK, Google" then speak, or press Ctrl+C to quit...')

    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        status_ui.status('listening')

    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        print('You said:', event.args['text'])
        text = event.args['text'].lower()
        if text == 'power off':
            assistant.stop_conversation()
            power_off_pi()
        elif text == 'reboot':
            assistant.stop_conversation()
            reboot_pi()
        elif text == 'ip address':
            assistant.stop_conversation()
            say_ip()
        elif text == 'internet ip':
            assistant.stop_conversation()
            say_internet_ip()
        elif text == 'turn on table lamp':
            assistant.stop_conversation()
            say_turn_tablelamp_on()
        elif text == 'turn off table lamp':
            assistant.stop_conversation()
            say_turn_tablelamp_off()
        elif text == 'turn raspberry blue on':
            assistant.stop_conversation()
            say_turn_pi_blue()
        elif text == 'turn raspberry red on':
            assistant.stop_conversation()
            say_turn_pi_red()
        elif text == 'turn raspberry green on':
            assistant.stop_conversation()
            say_turn_pi_green()
        elif text == 'turn raspberry off':
            assistant.stop_conversation()
            say_turn_pi_clear()
        elif text == 'volume up':
            assistant.stop_conversation()
            set_volume(10)
        elif text == 'volume down':
            assistant.stop_conversation()
            set_volume(-10)
        elif text == 'max volume':
            assistant.stop_conversation()
            set_volume(100)
        elif text.startswith('repeat after me'):
            assistant.stop_conversation()
            aiy.audio.say(text[15:])

    elif event.type == EventType.ON_END_OF_UTTERANCE:
        status_ui.status('thinking')

    elif event.type == EventType.ON_CONVERSATION_TURN_FINISHED:
        status_ui.status('ready')

    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        sys.exit(1)


def main():
    credentials = aiy.assistant.auth_helpers.get_assistant_credentials()
    with Assistant(credentials) as assistant:
        for event in assistant.start():
            process_event(assistant, event)


if __name__ == '__main__':
    main()
