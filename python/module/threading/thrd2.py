import threading, requests, time

def getHtml(url):
    response = requests.get(url)
    time.sleep(1)
    print(url, len(response.text), ' chars')

t1 = threading.Thread(target=getHtml, args=('http://google.com',))
t1.start()

print("### End ###")