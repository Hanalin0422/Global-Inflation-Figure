"""
import urllib.request as req
import requests
from bs4 import BeautifulSoup
import config

code = req.urlopen("https://developers.google.com/public-data/docs/canonical/countries_csv")
html = BeautifulSoup(code, "html.parser")
country_list = html.select('tr')

latest_global_cpi_list = []
for country_info in country_list[1::]:
  dict = {}
  lat, lng, country = country_info.text.split('\n')[2:5:]
  api_url = f'https://api.api-ninjas.com/v1/inflation?country={country}'
  response = requests.get(api_url, headers={'X-Api-Key': config.key}).json()
  if len(response) != 0:
    dict['country'] = country
    dict['lat'] = lat
    dict['lng'] = lng
    dict['cpi'] = response[0]['yearly_rate_pct']
    latest_global_cpi_list.append(dict)
    print(True)
  else:
    print(False)

print(latest_global_cpi_list)

"""