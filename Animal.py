#! /home/shiyanlou/lou-challenge/ python3 

class Animal(object):
    def __init__(self,name):
         self._name=name
    @property 
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
       #judge the length of introducted new name 'value' 
        if len(value)>4:
            self._name=value
    def make_sound(self):
         pass 

