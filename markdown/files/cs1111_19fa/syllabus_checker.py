import urllib.request

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/deniro.csv"

stream = urllib.request.urlopen(url)

for line in stream:
    #print(line)
    print(line.decode("UTF-8").strip())