import time
import threading

def func1():
  t = threading.Thread(target=func2)
  t.start()
  Print("Do stuff here")

def func2():
  time.sleep(10)
  print("Do more stuff here")

func1()
print("Func1 has returned")
