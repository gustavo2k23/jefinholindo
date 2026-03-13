import requests
def get_weather(city_name, API_KEY):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=pt"
    response = requests.get(url)
      #exbido o status code ee a resposta da API para diagnostico
      
    print("codigo de status:", response.status_code)
    print("resposta da API:", response. text)
    if response.status_code == 200:
        data = response.json()
        city= data["name"]
        country=data["sys"]["country"]
        temp= data['main']["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"previsao do tempo para {city},{country}:")
        print(f"temperatura:{temp}°c")
        print(f"condiçao:{weather_desc.capitalize()}")
        print(f"umidade:{humidity}%")
        print(f"velocidade do vento:{wind_speed}m/s")
    else:
        print("erro ao obter os dados. verifique o nome da cidade e tente novamente.")


if __name__=="__main__":
    API_KEY = "482b8c48f006dde8f978d8afdedfcf1a" #substitua pela sua chave de bobao
    cidade = input("digite o nome da cidade:")
    get_weather(cidade, API_KEY)