from flask import Flask,render_template
import requests 
from dotenv import load_dotenv,dotenv_values 


config = dotenv_values('.env')


app = Flask(__name__)

def get_weather_data(city):
    API_KEY = config['API_KEY']
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ city }&units=metric&lang=es&appid={API_KEY}'
    r = requests.get(url).json()
    return r

@app.route('/satur')
def satur():
    get_weather_data('Guayaquil')
    return get_weather_data('Guayaquil')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/clima')
def clima():
    r=get_weather_data('Quito')
    print(r)
    weather = {
            'city' : 'Quito',
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
    
    return render_template('weather.html',weather=weather)


if __name__ == '__main__':
    app.run(debug=True)