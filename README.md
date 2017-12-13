# google-voice-recognition
Google Assistant AIY Voice Kit

## Prerequisite

	*  1 Google Voice Kit incl. Raspberry Pi
	*  1 Raspberry Pi with Unicorn HAT 

## Python 3

	sudo apt-get install python3-pip python3-dev
	sudo pip3 install unicornhat

Alternative :

	 curl -sS https://get.pimoroni.com/unicornhat | bash

	 git clone https://github.com/google/aiyprojects-raspbian.git voice-recognizer-raspi

## Further Info about Google AIY Voice Kit
https://aiyprojects.withgoogle.com/voice/#makers-guide-1-1--source-code


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



Replace the ExecStart Path and install the main.py for Google AIY in /home/pi/voice-recognizer-raspi/src

Start and Check if some errors:

	sudo service voice-recognizer start
	sudo service voice-recognizer status





