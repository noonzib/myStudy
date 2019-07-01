import urllib.request as urllib 
import pickle 
url = "http://www.pythonchallenge.com/pc/def/banner.p"

response = urllib.urlopen(url).read()
data = pickle.loads(response)

for line in data:
    result = ""
    for i in range(len(line)):
        char = line[i][0]
        for n in range(line[i][1]):
            result += char
    print(result)

#solve : channel