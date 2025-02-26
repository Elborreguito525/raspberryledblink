# TimeLapse fotografico con LED

## Descripcion

Este proyecto consiste en la implementación de un sistema para tomar fotografías y hacer parpadear una luz cada vez que se realiza una fotografia en tu CANSAT utilizando una Raspberry Pi 2 Zero 2 W y un codigo de Python enlazado a un archivo de bash. El propósito es conseguir modificando el lente para poder obtener fotos infrarojas para oservar las zonas con vegetacion que tienen agua.

## Funcionamento scripts

El script principal de bash que guardamos en la carpeta de root
```blue
#!/bin/bash

for ((i = 0 ; i < 10 ; i++)); do
	sudo rapistill -w 1920 -h 1080 -o /var/out.jpg
  cp -v /var/out.jpg /home/usuari/Documents/$(date '+%Y%m%d%H%M%S').jpg
  sudo python3 /root/raspberryled.py
  sleep 0
done
```
IMPORTANTE la comanda rapistill no existe en el Raspbery OS 64bits i 32 bits (default).
```blue 
sudo rpicam-still --output /var/out.jpg
```
Para hacer-lo en esta nueva version:
```blue
#!/bin/bash

mkdir /home/usuari/Documents/$(date +%F%R)
rpicam-still -timeout 59000 -timelapse 1000 -o /home/usuari/Documents/$(date +F%R)/image%04d.jpg
sudo python3 led.py
```
I luego con el archivo de rasbberry tambien almacenado en la carpeta de root para poder ser exectuado sin tocar el script.

```blue
import RPi.GPIO as GPIO

from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)

sleep(0.5)
GPIO.output(3,GPIO.HIGH)
sleep(0,5)
GPIO.output(GPIO.LOW)
```

