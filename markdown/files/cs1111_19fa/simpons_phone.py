import re
import urllib.request

url = "https://storage.googleapis.com/cs1111/practice/simpsons_phone_book.txt"

phone_pattern = "((J[a-z]*) (Neu[a-z]*)) ([0-9]{3}-[0-9]{4})"
req = urllib.request.urlopen(url)
text = req.read().decode("UTF-8")

regex = re.compile(phone_pattern)

for i in regex.findall(text):
    print(i)