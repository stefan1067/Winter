import machine
from machine import Pin
import time
from machine import I2C

#from smbus import SMBus
#prova
#
# Setup
green = Pin("PC5", Pin.OUT)
red = Pin("PB0", Pin.OUT)

#Inizializza la comunicazione I2C
i2c = machine.I2C(scl=machine.Pin("PB6"), sda=machine.Pin("PB7"), freq=400000)

#i2c .scan ()	#Scansione della scheda

address =0x5D # quando pad SA0 collegato a tensione di alimentazione
addressTerra=0x5C #quando pad SA0 collegato a terra

#nbyte=numero di byte da leggere
data = bytearray(2)
#i2c.scan()
# registro di controllo del sensore
CTRL_REG1 = 0x10
WHO_AM_I = 0x0F
# registro di output della temperatura
TEMP_OUT_L = 0x2B
TEMP_OUT_H = 0x2C


# configurazione del sensore di pressione
#i2c.writeto_mem(address,WHO_AM_I , b'\x00')
#Registro di dati della temperatura del barometro LPS22HH
TEMP_OUT_L = 0x2B
TEMP_OUT_H = 0x2C
PRESS_OUT_XL = 0x28
PRESS_OUT_L = 0x29
PRESS_OUT_H = 0x2A
#who_am_i = i2c.readfrom_mem(address, WHO_AM_I, 1)
#print("ID del dispositivo: " + str(who_am_i[0]))
#i2c.readfrom_mem_into(address, sda, data)
#La funzione readfrom_mem restituirà una stringa di byte con i dati recuperati dal dispositivo e successivamente esecuzionde del print
#press_xl = i2c.readfrom_mem(address, PRESS_OUT_H, 1)
# Loop
while True:
	print("prova")
	green.value(1)
	red.value(0)
	green.value(1)
	time.sleep(1)
	green.value(0)
	red.value(1)
	time.sleep(1)
    