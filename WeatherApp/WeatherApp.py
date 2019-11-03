# importing modules

import json
import requests
from tkinter import *
from PIL import ImageTk,Image

# Required Details
root = Tk()
root.geometry("425x425")
root.title("Weather App")
root.configure(bg='white')

# for images

img = ImageTk.PhotoImage(Image.open('WEAT.png'))
panel = Label(root,image=img)
panel.place(x=0,y=0)

lable_0 = Label(root,text="MyWeather",width = 20,bg='white',font=("bold",24),fg='brown')
lable_0.place(x=-75,y=93)

city_names = StringVar()
entry_1 = Entry(root,textvariable=city_names)
city_names.set("")
entry_1.place(x=5,y=140)



lable_2 = Label(root,text="Temprature : ",width = 15,bg='white',font=("bold",10),fg='blue')
lable_2.place(x=-20,y=220)

lable_3 = Label(root,text="FeelsLike : ",width = 15,bg='white',font=("bold",10),fg='blue')
lable_3.place(x=-20,y=240)

lable_5 = Label(root,text="AirQualInd : ",width = 15,bg='white',font=("bold",10),fg='blue')
lable_5.place(x=-20,y=260)

lable_6 = Label(root,text="Longitude : ",width = 15,bg='white',font=("bold",10),fg='blue')
lable_6.place(x=-20,y=280)

lable_7 = Label(root,text="Latitude : ",width = 15,bg='white',font=("bold",10),fg='blue')
lable_7.place(x=-20,y=300)

lable_temp = Label(root,text="",width = 5,bg='white',font=("bold",10),fg='blue')
lable_temp.place(x=80,y=220)

lable_feeltemp = Label(root,text="",width = 5,bg='white',font=("bold",10),fg='blue')
lable_feeltemp.place(x=80,y=240)

lable_AQI = Label(root,text="",width = 5,bg='white',font=("bold",10),fg='blue')
lable_AQI.place(x=80,y=260)

lable_Longitude = Label(root,text="",width = 5,bg='white',font=("bold",10),fg='blue')
lable_Longitude.place(x=80,y=280)

lable_Latitude = Label(root,text="",width = 5,bg='white',font=("bold",10),fg='blue')
lable_Latitude.place(x=80,y=300)

# api config
def getTemp():

    api_key = "95dace7de296455999e47ce82e8cda2e"
    aqi_key = "ccedb1e2d83b406d93ddafa7d7bddb0e"
    base_url = "https://api.weatherbit.io/v2.0/current?city="
    print(base_url)
    city_name = entry_1.get()
    complete_url = base_url+city_name+"&key="+api_key
    #https://api.weatherbit.io/v2.0/current?city=Mumbai&key=95dace7de296455999e47ce82e8cda2e
    #def WeatherFore(loc):
    #Key=str("95dace7de296455999e47ce82e8cda2e")
    #url=https://api.weatherbit.io/v2.0/current
    #fop="https://api.weatherbit.io/v2.0/current?city="+loc+"&key="+Key
    #print(fop)
    #response=requests.get(fop)#sending a get response to the url
    #if(response.text=="temp"):
        #print(response.text)
    #print(response,response.text,type(response.text))
    #j_response=json.loads(response.text)
    #print(j_response,type(j_response))
    #current_temp=j_response['data'][0]["temp"]
    #current_feel_temp=j_response['data'][0]["app_temp"]
    #print("Current temperature"+str(current_temp))
    #print("Current feel-like temperature"+str(current_feel_temp))
#WeatherFore(input("Enter the city "))
# module response get

    response = requests.get(complete_url)
    if(response.text=="temp"):
        print(response.text)
    print(response,response.text,type(response.text))
    j_response=json.loads(response.text)
    #print(response,response.text,type(response.text))
    x=response.json()

    
    current_temp=j_response['data'][0]["temp"]
    current_feel_temp=j_response['data'][0]["app_temp"]
    air_quality_index=j_response['data'][0]["aqi"]
    longitude=j_response['data'][0]["lon"]
    latitude=j_response['data'][0]["lat"]

    lable_temp.configure(text=current_temp)
    lable_feeltemp.configure(text=current_feel_temp)
    lable_AQI.configure(text=air_quality_index)
    lable_Longitude.configure(text=longitude)
    lable_Latitude.configure(text=latitude)
    
Button(root,text="Submit",width=20,bg='brown',fg='white',command=getTemp).place(x=122,y=170)



mainloop()
