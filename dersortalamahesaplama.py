#!/usr/bin/env python
# -*- coding: utf-8 -*-

dersortalamahesaplama_ico = """
#########################################################
#        DERS ORTALAMA HESAPLAMA - GH0ST S0FTWARE       #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#        Mail Address : pentestdatabase@gmail.com       #
# LINKEDIN : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################
"""

print dersortalamahesaplama_ico

ders_adi = raw_input('Ders Adini Giriniz = ')

star = '****************************************'

print star

sinav_1 = input('1.Sinav Notunuzu Giriniz = ')
sinav_2 = input('2.Sinav Notunuzu Giriniz = ')
performans_1 = input('1.Performans Notunuzu Giriniz = ')
performans_2 = input('2.Performans Notunuzu Giriniz = ')
proje = input('Proje Notunuzu Giriniz = ')

print star

ders_ort = (sinav_1 + sinav_2 + performans_1 + performans_2 + proje)/5

print ders_adi, 'dersinden aldiginiz not = ', ders_ort

print star
