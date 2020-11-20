import tkinter as tk
from tkinter import font
import PIL.Image

import requests

API_KEY = '1394035231568e37066c239aaaa34f93' #TODO insert API key from Openweathermap.com

#functions
def test_function(entry):
    print("button clicked", entry)

def format_response(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']
        humid = weather['main']['humidity']
        wind = weather['wind']['speed']
        final_str = 'City: %s \nConditions: %s \nTemperature (D): %s\n Humidity: %s\n Wind speed: %s' % (name, description, temperature, humid, wind)

    except:
        final_str = 'There was a problem retrieving that information.'

    return final_str








def get_weather(city):
    weather_key = API_KEY
    url = 'http://api.openweathermap.org/data/2.5/weather?1394035231568e37066c239aaaa34f93'
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params)
    weather = response.json()
    format_response(weather)

    label['text'] = format_response(weather)


#6a681cac28a4a5b1626f6986f7727b06
#api.openweathermap.org/data/2.5/forecast?q=London,us&mode=xml
HEIGHT = 500
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()



frame = tk.Frame(root, bg="#87cefa", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 18))
entry.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", bg="gray", fg="white", font=('Courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='#90c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 18))
label.place(relx=0, rely=0, relwidth=1, relheight=1)





root.mainloop()