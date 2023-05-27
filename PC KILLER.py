import os
import time
s=float(input("enter Time In Minutes"))
s= s*60
while(s != 0):
 time.sleep(1)
 s= (s - 1)
 print(s)

if(s==0):
  os.system("shutdown /s")
else:
 print("Exiting the program doing nothing")

