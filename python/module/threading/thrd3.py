import threading, requests, time

class HtmlGetter (threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
    
    def run(self):
        response = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(response.text), ' chars')

t = HtmlGetter('http://google.com')
t.start()

print("### End ###")