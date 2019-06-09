# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 09:12:41 2019

@author: Paulina
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.garden.mapview import MapMarker, MarkerMapLayer
#import matplotlib
#matplotlib.use("module://kivy.garden.matplotlib.backend_kivy")
from math import pi
import funkcja
import random



class Apka(BoxLayout):
    my_map = ObjectProperty()
    pic = ObjectProperty()
    tekst = ObjectProperty()
    data_layer = ObjectProperty()
    
    
    def search_location(self): #funkcja lokalizująca obiekty
        self.data_layer = MarkerMapLayer()
        self.my_map.add_layer(self.data_layer)
        self.lati = self.my_map.lat
        self.long = self.my_map.lon

            
        print(self.lati)
        print(self.long)
        
        list_of_points= [
                ['zegar_praga.jpg', 50+5/60+12/3600, 14+25/60+14/3600],
                ['sagrada_familia.jpg', 50.06465009, 19.94497990000002],
                ['sacre_coeur.jpg', 48.8863280, 2.3430490],
                ['london_eye.jpg', 51.5007316, -0.1186893],
                ['notre_dame.jpg', 48.8540278, 2.3473245],
                ['koloseum.jpg', 41.8895897, 12.4940828],
                ['fontanna.jpg', 41.9008219, 12.4830284],
                ['eiffel_tower.jpg', 48.8583157, 2.2943230],
                ['big_ben.jpg', 51.4995730,  -0.1245830],
                ['arc.jpg' , 48.8738178, 2.2950626],
                ['akropol.jpg', 37.9666670, 23.7166670]
                ]
        try:
            self.my_map.remove_marker(self.marker)
        except:
            pass
        
        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        
    
        
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        #zmiana formatu wywietlania znakow
        self.search_lat.text = "{:5.5f}".format(self.latitude)
        self.search_long.text = "{:5.5f}".format(self.longitude)
        
      #użycie funkcji obliczającej odległosc 
        for i in range(len(list_of_points)):
            if self.pic.source == list_of_points[i][0]:
                s = funkcja.Vincenty(self.lati*pi/180, self.long*pi/180, list_of_points[i][1]*pi/180, list_of_points[i][2]*pi/180)
        
        points=[]
        if s > 100:
            self.tekst.text = "Odleglosc pomiedzy {} m".format(round(s, 3))
            score = 0
            points.append(score)   
        else:
            self.tekst.text = "zdobywasz punkt!"
            score = 1
            points.append(score)
            
        sum_of_points = points.count(1)
        self.score.text = "Twoje punkty : {}".format(sum_of_points)
            
            
    def zmiana_pic(self): #funkcja zmieniająca zdjęcie sposrod dostepnych
        obiekty = ['sagrada_familia.jpg', 'zegar_praga.jpg', 'sacre_coeur.jpg',
                   'london_eye.jpg', 'london_eye.jpg', 'notre_dame.jpg', 
                   'koloseum,jpg', 'fontanna.jpg', 'eiffel_tower.jpg',
                   'big_ben.jpg', 'arc.jpg', 'akropol.jpg' ]

        
        self.pic.source = random.choice(obiekty)
        
        try:
            self.clear()
        except ValueError:
            pass
            
        

    def clear(self):
        self.my_map.remove_layer(self.data_layer)
        
        
        
        
class MapViewViewApp(App):
    def build(self):
        return Apka()
#pass

if __name__ == '__main__':
    MapViewViewApp().run()