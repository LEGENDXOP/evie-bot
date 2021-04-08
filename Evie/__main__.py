from sys import argv, exit
from Evie import xbot
from Evie import TOKEN

import Evie.events

try:
    xbot.start(bot_token=TOKEN)
except Exception:
    print("Bot Token Invalid")
    exit(1)

if len(argv) not in (1, 3, 4):
    xbot.disconnect()
else:
    xbot.run_until_disconnected()

