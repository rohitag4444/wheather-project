# WHEATHER PROJECT
import tkinter as tk
import requests as rq

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

API_KEY = "74d33c6f4f03b7c4280ea3e3016573fd"

# function to get the wheather information
def get_wheather():
    city = city_entry.get()

    #prepare our data
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"

    }
    #send request 
    response = rq.get(BASE_URL , params=params)
    data = response.json()
    if data["cod"] == 200:
        temp = data["main"]["temp"]
        wheather_description = data["weather"][0]["description"]
        output_label.config(text = f"Temperature: {temp}°C\nDescription: {wheather_description}")
    else:
        output_label.config(text = "City not found❌")
    print(data)



# create gui of the app
root = tk.Tk()
root.geometry("800x800")
root.title("Wheather App")

# top label
top_label = tk.Label(root , text = "Enter the city name " , font = ("Arial" , 12))
top_label.pack(pady=10)

# city label
city_label =tk.Label(root , text = "City Name:" , font = ("Arial" , 20))
city_label.pack(pady=10)

# entry box
city_entry = tk.Entry(root , font = ("Arial" , 15))
city_entry.pack(pady=10)

# submit button
submit_button = tk.Button(root , text = "Submit" , font = ("Arial" , 15) , bg = "orange" , fg = "white", command = get_wheather)
submit_button.pack(pady=10)

# outputlabel
output_label = tk.Label(root , bg="#ABCFEC" , font = ("Arial" , 15))
output_label.pack(pady=10)

root.mainloop()





 


