import time
import threading
def hello():
    x = 0
    while x < 100000000:
        pass
        x += 1
start = time.clock()
t = threading.Thread(target=hello, args=())
t.start()
t.join()
end = time.clock()
print "The time was {}".format(end - start) 