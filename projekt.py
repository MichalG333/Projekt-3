# -*- coding: utf-8 -*-

from kivy.garden.mapview import MapMarker
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from math import sin, cos, sqrt, atan2,pi
import time


class Form(BoxLayout):
    def draw_marker(self): 
        self.list_of_points = [['Budapeszt.jpg', 48, 19],['Warszawa.jpg', 52, 21],#lista miast oraz ich współrzędnych
                               ['Tokio.jpg', 35, 139],['Moskwa.jpg', 55, 37],['Miami.jpg', 25, 80],
                               ['Bagdad.jpg', 33, 44],['Oslo.jpg', 59, 10],['Sydney.jpg', 33, 151], 
                               ['Rio de Janeiro.jpg', 22, 43],['Waszyngton.jpg', 38, 77],['Mława.jpg', 53, 20]]
        
        try:
            self.my_map.remove_marker(self.marker)
        except:
            pass
        
        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        
        self.marker = MapMarker(lat=self.latitude, lon=self.longitude)
        self.my_map.add_marker(self.marker)
        
        self.search_lat.text="{:10.5f}".format(self.latitude)#szerokosc i dlugosc i ich dokładnosc
        self.search_long.text="{:10.5f}".format(self.longitude)
        
    
    def check_points(self):#funkcja programu odpowiadająca za obliczenie odległosci 
        print(self.i)                                   
        self.latitude = self.my_map.lat
        self.longitude = self.my_map.lon
        time.sleep(1)
        R = 6383.0
        lat1 = (self.latitude)*pi/180
        lon1 = (self.longitude)*pi/180
        lat2 = (self.list_of_points[self.i][1])*pi/180
        lon2 = (self.list_of_points[self.i][2])*pi/180

        dlon = lon1-lon2
        dlat = lat1-lat2
        a = sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
        c = 2*atan2(sqrt(a), sqrt(1 - a))

        odległosc = R*c
        self.dis.append(odległosc)
        print(odległosc)
          
        suma=sum(self.dis)
        #warunek przyznawający punkty za odpowiednio blisko umiejscowiony znacznik
        if suma<1000:
            self.score=100
        elif suma>1000 and suma<10000:
            self.score=50
        else:
            self.score=0
        self.i=self.i+1
        self.my_image.source =self.list_of_points[self.i][0]
        
        if self.i+1==(len(self.list_of_points)):
            self.koniec.text="END GAME"
        self.wynik2.text="{:10.0f}".format(self.score)    
        
    def funkcja0(self): 
        self.wynik2.text='0' 
        self.i=0
        self.dis=[]
        self.my_image.source =self.list_of_points[0][0]
        self.koniec.text="START"
           

class MapViewApp(App):
    pass

MapViewApp().run()