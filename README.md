# google-voice-recognition
Google Assistant AIY Voice Kit

## Prerequisite

	*  1 Google Voice Kit incl. Raspberry Pi
	*  1 Raspberry Pi with Unicorn HAT 

## Python 3 for Raspberry with Unicorn HAT

	sudo apt-get install python3-pip python3-dev
	sudo pip3 install unicornhat

Alternative :

	 curl -sS https://get.pimoroni.com/unicornhat | bash

## Install Google AIY Vocie SDK Kit:

	 git clone https://github.com/google/aiyprojects-raspbian.git voice-recognizer-raspi

## Further Info about Google AIY Voice Kit

https://aiyprojects.withgoogle.com/voice/#makers-guide-1-1--source-code

https://aiyprojects.withgoogle.com/voice/#makers-guide-3-4--run-your-app-automatically

## Install as a service and replace some entrys

Install as a service  in /lib/systemd/system/voice-recognizer.service
	
	[Unit]
	Description=voice recognizer
	After=network.target ntpdate.service

	[Service]
	Environment=VIRTUAL_ENV=/home/pi/voice-recognizer-raspi/env
	Environment=PATH=/home/pi/voice-recognizer-raspi/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
	ExecStart=/home/pi/voice-recognizer-raspi/env/bin/python3 -u src/main.py
	WorkingDirectory=/home/pi/voice-recognizer-raspi
	StandardOutput=inherit
	StandardError=inherit
	Restart=always
	User=pi

	[Install]
	WantedBy=multi-user.target



 * Replace the ExecStart Path and install the "main.py" for Google AIY in /home/pi/voice-recognizer-raspi/src

Start and Check if some errors:

	sudo service voice-recognizer start
	sudo service voice-recognizer status




## Raspberry Pi Unicorn Hat

	sudo python /home/rpi/google-voice-recognition/main.py

Edit the colour.py if you like to change colors and implement more features.

#  MQTT Testing
  Using :  mosquitto_pub -h mqtt.unixweb.de -t mygoogleassistant -m "red"

  Using :  mosquitto_pub -h mqtt.unixweb.de -t mygoogleassistant -m "blue"

  Using :  mosquitto_pub -h mqtt.unixweb.de -t mygoogleassistant -m "green"

  Using :  mosquitto_pub -h mqtt.unixweb.de -t mygoogleassistant -m "clear"

# Google AIY Voice Kit
 Using : "Hey Google, turn raspberry blue on"

 Using : "Hey Google, turn raspberry red on"

 Using : "Hey Google, turn raspberry green on"

 Using : "Hey Google, turn raspberry off"

# Youtube Video - Google Voice Kit and Unicorn Hat in action

https://www.youtube.com/watch?v=Y2POBkDlNpk


