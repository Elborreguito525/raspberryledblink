# TimeLapse fotografico con LED

## Descripcion

Este proyecto consiste en la implementación de un sistema para tomar fotografías y hacer parpadear una luz cada vez que se realiza una fotografia en tu CANSAT utilizando una Raspberry Pi 2 Zero 2 W y un codigo de Python enlazado a un archivo de bash. El propósito es conseguir modificando el lente para poder obtener fotos infrarojas para oservar las zonas con vegetacion que tienen agua.

## Funcionamento scripts

El script principal de bash
'''
#!/bin/bash

for ((i = 0 ; i < 10 ; i++)); do
	sudo rapistill -w 1920 -h 1080 -o /var/out.jpg
  cp -v /var/out.jpg /home/usuari/Documents/$(date '+%Y%m%d%H%M%S').jpg
  sudo python3 /root/raspberryled.py
  sleep 0
done
'''
