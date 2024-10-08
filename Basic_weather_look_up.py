# here i am declaring dictionary value 
weather_data={'kodimial':{'temperature':23, 'humidity':50,'condition':'sunny'},'wanparthy':{'temperature':34, 'humidity':45,'condition':'cloudy'},'mahaboobnagar':{'temperature':23, 'humidity':34,'condition':'rainy'}}
def basic_weather_lookup():# defining function
    while True:#i am trying to repeat again until user want to break the loop 
        input_city_name=input("enter city name")#entering input here
        if input_city_name in weather_data: #using conditional statement i am comparing input to dictionary
            weather_format=lambda data:f"Temperature:{data['temperature']}ºC,humidity:{data['humidity']}%,condition:{data['condition']}"
            weather_result=weather_data[input_city_name]
            print(weather_format(weather_result))
        else:#else this error should be executed
            print("city is not found!, please enter valid city name")
        try_again=input("enter 'RAV' to exit / enter 'VIJ' to try again").strip().upper()#here if user want to break or repeat the loop 
        if try_again!='VIJ':
            break
basic_weather_lookup()#i am calling the function from here
