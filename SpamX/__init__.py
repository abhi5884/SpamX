import asyncio
import os
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters

ULOG = [1549789242, 2007315257]

if os.path.exists(".env"):
    load_dotenv(".env")
    
__version__ = "v0.1"

# -------------CONFIGS--------------------
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
ALIVE_PIC = os.getenv("ALIVE_PIC", "")
ALIVE_MSG = os.getenv("ALIVE_MSG", "")
PING_MSG = os.getenv("PING_MSG", "")
SESSION = os.getenv("SESSION", None)
SESSION2 = os.getenv("SESSION2", None)
SESSION3 = os.getenv("SESSION3", None)
SESSION4 = os.getenv("SESSION4", None)
SESSION5 = os.getenv("SESSION5", None)
SESSION6 = os.getenv("SESSION6", None)
SESSION7 = os.getenv("SESSION7", None)
SESSION8 = os.getenv("SESSION8", None)
SESSION9 = os.getenv("SESSION9", None)
SESSION10 = os.getenv("SESSION10", None)
SESSION11 = os.getenv("SESSION11", None)
SESSION12 = os.getenv("SESSION12", None)
SESSION13 = os.getenv("SESSION13", None)
SESSION14 = os.getenv("SESSION14", None)
SESSION15 = os.getenv("SESSION15", None)
SESSION16 = os.getenv("SESSION16", None)
SESSION17 = os.getenv("SESSION17", None)
SESSION18 = os.getenv("SESSION18", None)
SESSION19 = os.getenv("SESSION19", None)
SESSION20 = os.getenv("SESSION20", None)
LOGS_CHANNEL = os.getenv("LOGS_CHANNEL", None)
if LOGS_CHANNEL:
    if int(LOGS_CHANNEL) in ULOG:
        print("You Can't Use That Chat As A Log Channel -!")
        print("Change Logs Channel Id else Bot Could not be start")
        quit()
    
HNDLR = os.getenv("HNDLR", ".")
OWNER_ID = int(os.environ.get("OWNER_ID", None))
sudo = os.getenv("SUDO_USERS")

SUDO_USERS = []
if sudo:
    SUDO_USERS = make_int(sudo)
DEVS = [1549789242, 2007315257]
for x in DEVS:
    SUDO_USERS.append(x)

SUDO_USERS.append(OWNER_ID)


# SUDO_USERS = list(filter(lambda x: x, map(int, os.getenv("SUDO_USERS", "1517994352 1789859817").split())))
#----------------------------------------------

Neurotic = Client(name="SESSION", api_id = API_ID, api_hash = API_HASH, session_string=SESSION, plugins=dict(root="SpamX.module"))
print("Client 1 Found")


hl = HNDLR[0]
start_time = time.time()

#-------------------------CLIENTS-----------------------------
async def SpamX():
    global Neurotic2
    global Neurotic3
    global Neurotic5
    global Neurotic4
    global Neurotic6
    global Neurotic7
    global Neurotic8
    global Neurotic9
    global Neurotic10
    global Neurotic11
    global Neurotic12
    global Neurotic13
    global Neurotic14
    global Neurotic15
    global Neurotic16
    global Neurotic17
    global Neurotic18
    global Neurotic19
    global Neurotic20
    
    if SESSION2:
         Neurotic2 = Client(name="SESSION2", api_id = API_ID, api_hash = API_HASH, session_string=SESSION2, plugins=dict(root="SpamX.module"))
         print("Client 2 Found")
    else:
         Neurotic2 = None
         pass
   
    if SESSION3:
         Neurotic3 = Client(name="SESSION3", api_id = API_ID, api_hash = API_HASH, session_string=SESSION3, plugins=dict(root="SpamX.module"))
         print("Client 3 Found")
    else:
         Neurotic3 = None
         pass

    if SESSION4:
         Neurotic4 = Client(name="SESSION4", api_id = API_ID, api_hash = API_HASH, session_string=SESSION4, plugins=dict(root="SpamX.module"))
         print("Client 4 Found")
    else:
         Neurotic4 = None
         pass

    if SESSION5:
         Neurotic5 = Client(name="SESSION5", api_id = API_ID, api_hash = API_HASH, session_string=SESSION5, plugins=dict(root="SpamX.module"))
         print("Client 5 Found")
    else:
         Neurotic5 = None
         pass  

    if SESSION6:
         Neurotic6 = Client(name="SESSION6", api_id = API_ID, api_hash = API_HASH, session_string=SESSION6, plugins=dict(root="SpamX.module"))
         print("Client 6 Found")
    else:
         Neurotic6 = None
         pass    

    if SESSION7:
         Neurotic7 = Client(name="SESSION7", api_id = API_ID, api_hash = API_HASH, session_string=SESSION7, plugins=dict(root="SpamX.module"))
         print("Client 7 Found")
    else:
         Neurotic7 = None
         pass    

    if SESSION8:
         Neurotic8 = Client(name="SESSION8", api_id = API_ID, api_hash = API_HASH, session_string=SESSION8, plugins=dict(root="SpamX.module"))
         print("Client 8 Found")
    else:
         Neurotic8 = None
         pass    

    if SESSION9:
         Neurotic9 = Client(name="SESSION9", api_id = API_ID, api_hash = API_HASH, session_string=SESSION9, plugins=dict(root="SpamX.module"))
         print("Client 9 Found")
    else:
         Neurotic9 = None
         pass    

    if SESSION10:
         Neurotic10 = Client(name="SESSION10", api_id = API_ID, api_hash = API_HASH, session_string=SESSION10, plugins=dict(root="SpamX.module"))
         print("Client 10 Found")
    else:
         Neurotic10 = None
         pass    

    if SESSION11:
         Neurotic11 = Client(name="SESSION11", api_id = API_ID, api_hash = API_HASH, session_string=SESSION11, plugins=dict(root="SpamX.module"))
         print("Client 11 Found")
    else:
         Neurotic11 = None
         pass    

    if SESSION12:
         Neurotic12 = Client(name="SESSION12", api_id = API_ID, api_hash = API_HASH, session_string=SESSION12, plugins=dict(root="SpamX.module"))
         print("Client 12 Found")
    else:
         Neurotic12 = None
         pass    

    if SESSION13:
         Neurotic13 = Client(name="SESSION13", api_id = API_ID, api_hash = API_HASH, session_string=SESSION13, plugins=dict(root="SpamX.module"))
         print("Client 13 Found")
    else:
         Neurotic13 = None
         pass    

    if SESSION14:
         Neurotic14 = Client(name="SESSION14", api_id = API_ID, api_hash = API_HASH, session_string=SESSION14, plugins=dict(root="SpamX.module"))
         print("Client 14 Found")
    else:
         Neurotic14 = None
         pass    

    if SESSION15:
         Neurotic15 = Client(name="SESSION15", api_id = API_ID, api_hash = API_HASH, session_string=SESSION15, plugins=dict(root="SpamX.module"))
         print("Client 15 Found")
    else:
         Neurotic15 = None
         pass    

    if SESSION16:
         Neurotic16 = Client(name="SESSION16", api_id = API_ID, api_hash = API_HASH, session_string=SESSION16, plugins=dict(root="SpamX.module"))
         print("Client 16 Found")
    else:
         Neurotic16 = None
         pass    

    if SESSION17:
         Neurotic17 = Client(name="SESSION17", api_id = API_ID, api_hash = API_HASH, session_string=SESSION17, plugins=dict(root="SpamX.module"))
         print("Client 17 Found")
    else:
         Neurotic17 = None
         pass    

    if SESSION18:
         Neurotic18 = Client(name="SESSION18", api_id = API_ID, api_hash = API_HASH, session_string=SESSION18, plugins=dict(root="SpamX.module"))
         print("Client 18 Found")
    else:
         Neurotic18 = None
         pass    

    if SESSION19:
         Neurotic19 = Client(name="SESSION19", api_id = API_ID, api_hash = API_HASH, session_string=SESSION19, plugins=dict(root="SpamX.module"))
         print("Client 19 Found")
    else:
         Neurotic19 = None
         pass    

    if SESSION20:
         Neurotic20 = Client(name="SESSION20", api_id = API_ID, api_hash = API_HASH, session_string=SESSION20, plugins=dict(root="SpamX.module"))
         print("Client 20 Found")
    else:
         Neurotic20 = None
         pass

     

loop = asyncio.get_event_loop()
loop.run_until_complete(SpamX())
