#!/bin/bash

mkdir /home/usuari/Documents/$(date +%F%R)
rpicam-still -timeout 59000 -timelapse 1000 -o /home/usuari/Documents/$(date +F%R)/image%04d.jpg
sudo python3 led.py
