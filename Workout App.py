import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput


import time
import datetime
import os

time = 23
# This app will be a Kivy produced workout app. 
# Have workouts to choose from
# It will have the function to add workouts/ and delete workouts maybe check off workouts
# Perhaps take the time and the day
# Have calculation how much weight has been pushed and where you can type in sets and reps and weight 
Window.clearcolor = (.65,.50, .4, 1)

class widget(FloatLayout):
    def __init__(self, **kwargs):
        super(widget, self). __init__(**kwargs)

class MyWorkoutApp(App):
    def build(self):
        self.food = Button(text = "Food", size_hint=(.5, .1),pos_hint={'x':.2, "top":.1})
        def count(self):
            print("ham")
        return FloatLayout()
    
        
        


    '''def timer(self):
        seconds = int(input("How many seconds do you want your workout?"))
        for i in range(seconds):
            print(str(seconds - i) + " seconds remain in workout")
            time.sleep(1)
        print("Workout is completed!")
        Clock.schedule_interval(timer, 1)'''
    
    

        



if __name__ == "__main__":
    MyWorkoutApp().run()