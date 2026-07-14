import time

import pyautogui
import argparse
a =argparse.ArgumentParser(description="SIMPLE PYTHON BOMBER!!")
a.add_argument("-i","--msg",help="MESSAGE TO BE BOMBED!!",required=True)
a.add_argument("-n","--no",type=int,help="NO of times to be repeated",required=True,)
a.add_argument("-d","--delay",help="DELAY TIME",type=float,default=0.5)

args = a.parse_args()

print("""
███╗   ███╗███████╗ ██████╗
████╗ ████║██╔════╝██╔════╝
██╔████╔██║███████╗██║  ███╗
██║╚██╔╝██║╚════██║██║   ██║
██║ ╚═╝ ██║███████║╚██████╔╝
╚═╝     ╚═╝╚══════╝ ╚═════╝

Message Bomber v1.0
Educational Automation Tool"""

      )
for b in range(10,0,-1):
    print(f"Starting in {b}...")

time.sleep(10)
try:
    for i in range(0,args.no):
        pyautogui.write(args.msg)
        pyautogui.press("enter")
        time.sleep(args.delay)
        print(f"[{i+1}/{args.no}] Sent")
    print("BOMBED!! ", args.no, " Messeges sent.")
except KeyboardInterrupt:
    print("PROGRAM STOPPED BY USER!")
