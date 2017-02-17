import time;

nag=time.localtime(time.time())
print ("the current time in india is",nag)

localtime=time.asctime(nag)
print("the current local time",localtime)

run=time.ctime(10)
print(run)