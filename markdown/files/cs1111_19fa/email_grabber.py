import re
import urllib.request

url = "https://engineering.virginia.edu/departments/computer-science/faculty"

email_pattern = r"([a-z0-9]+)@[a-z\.]+\.(com|edu|org)"
req = urllib.request.urlopen(url)
text = req.read().decode("UTF-8")

regex = re.compile(email_pattern)
for i in regex.finditer(text):
    print(i.group(0), i.group(1), i.group(2))