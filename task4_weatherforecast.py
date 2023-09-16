import tkinter as tk
import requests
from datetime import datetime as dt
from datetime import timedelta

# this function fetches weather
def fetch_weather():
    city = city_entry.get()
    key = "f51dac37e0d9c9bd7074cecc290d21bc"
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={key}")
    response = r.json()

    temp = response.get("main").get("temp")
    feels_like = response.get("main").get("feels_like")
    min_temp = response.get("main").get("temp_min")
    max_temp = response.get("main").get("temp_max")
    condition = response.get("weather")[0].get("main")

    today = r.headers.get("date")
    today_obj = dt.strptime(today, "%a, %d %b %Y %H:%M:%S %Z")
    timezone_offset = int(response.get("timezone"))
    today_obj = today_obj + timedelta(seconds=timezone_offset)
    time = today_obj.time()

    today = today.split(" ")
    day = today[0][:-1]
    date = today[1] + " " + today[2] + " " + today[3]

    temp_label.config(text=f"Temperature: {temp}°C")
    feels_like_label.config(text=f"Feels Like: {feels_like}°C")
    min_max_label.config(text=f"Min Temp: {min_temp}°C, Max Temp: {max_temp}°C")
    condition_label.config(text=f"Condition: {condition}")
    date_label.config(text=f"Date: {date}, {day}")
    time_label.config(text=f"Time: {time}")

window = tk.Tk()
window.title("Weather Information")

# labels for input
city_label = tk.Label(window, text="Enter City:")
city_entry = tk.Entry(window)
fetch_button = tk.Button(window, text="Fetch Weather", command=fetch_weather)

# labels to display info
temp_label = tk.Label(window, text="")
feels_like_label = tk.Label(window, text="")
min_max_label = tk.Label(window, text="")
condition_label = tk.Label(window, text="")
date_label = tk.Label(window, text="")
time_label = tk.Label(window, text="")

# placing widgets into window's grid
city_label.grid(row=0, column=0)
city_entry.grid(row=0, column=1)
fetch_button.grid(row=0, column=2)
temp_label.grid(row=1, column=0, columnspan=3)
feels_like_label.grid(row=2, column=0, columnspan=3)
min_max_label.grid(row=3, column=0, columnspan=3)
condition_label.grid(row=4, column=0, columnspan=3)
date_label.grid(row=5, column=0, columnspan=3)
time_label.grid(row=7, column=0, columnspan=3)

# start tkinter loop
window.mainloop()