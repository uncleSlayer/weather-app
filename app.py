from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        city_name = request.form['city_name']
        url_for_data = f'https://foreca-weather.p.rapidapi.com/location/search/{city_name}'

        querystring = {"lang": "en", "country": "in"}

        headers = {
            "X-RapidAPI-Key": "b59a59dd98mshc0bbc70af115b20p15df41jsnea7943c367e9",
            "X-RapidAPI-Host": "foreca-weather.p.rapidapi.com"
        }

        response = requests.request(
            "GET", url_for_data, headers=headers, params=querystring).json()

        print(response)

        if response['locations'] != []:
            id = response['locations'][0]['id']
        else:
            id = 0

        url_for_temp = f"https://foreca-weather.p.rapidapi.com/current/{id}"

        querystring_for_temp = {"alt": "0", "tempunit": "C",
                                "windunit": "MS", "tz": "Europe/London", "lang": "en"}

        headers_for_temp = {
            "X-RapidAPI-Key": "b59a59dd98mshc0bbc70af115b20p15df41jsnea7943c367e9",
            "X-RapidAPI-Host": "foreca-weather.p.rapidapi.com"
        }

        temp = requests.request("GET", url_for_temp, headers=headers_for_temp, params=querystring_for_temp).json()
        print(temp)

        temperature = temp['current']['temperature']

        output = {
            'city_name': response['locations'][0]['name'],
            'state_name': response['locations'][0]['adminArea'],
            'country_name': response['locations'][0]['country'],
            'temperature': temperature
        }

        return render_template('index.html', data= output)
    return render_template('index.html', data={'city_name': ' :give input first', 'state_name': ' :give input first', 'country_name': ' :give input first', 'temperature': ' :give input first'})
app.run(debug=True)
