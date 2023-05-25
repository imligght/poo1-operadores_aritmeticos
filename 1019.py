# -*- coding: utf-8 -*-

totalSegundos = int(input())
horas = totalSegundos//3600
minutos = (totalSegundos - horas*3600)//60
segundos = totalSegundos - minutos*60 - horas*3600

print("%d:%d:%d" % (horas, minutos, segundos))