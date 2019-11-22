
import re
import urllib.request

url_base = "https://forecast.weather.gov/zipcity.php?inputstring="
location = input("Get weather for: ")

# <p class="myforecast-current-lrg">71&deg;F</p>

url = url_base + location
print(url)

with urllib.request.urlopen(url) as stream:
   text = stream.read().decode('utf-8')

temp_regex = r'<p class="myforecast-current-lrg">([^&]*)&deg;F</p>'
temp_finder = re.compile(temp_regex)
for match in temp_finder.finditer(text):
   print(match.group(1))

#<td class="text-right"><b>Humidity</b></td>\n<td>81%</td>
humidity_regex = r'<td class="text-right"><b>Humidity</b></td>\n.*<td>([^%]*)%</td>'
humidity_finder = re.compile(humidity_regex)
for match in humidity_finder.finditer(text):
   print(match.group(1))
