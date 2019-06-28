import requests
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
first = "16046"

for i in range(1,400):  
    params = {'nothing' : first}
    response = requests.get(url,params=params)
    print(response.text)
    ret = response.text  
    print([int(s) for s in ret.split() if s.isdigit()][0])
    first = [int(s) for s in ret.split() if s.isdigit()][0]