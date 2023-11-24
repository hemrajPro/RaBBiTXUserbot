import time
from bunny import bunny
from config import HANDLER
from bunny.utils import *
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
import asyncio
from typing import Callable
hl = HANDLER
startTime = time.time()
COMMANDS_HELP = {}
class Help:
    def __init__(self):
        self.handlers = {}

    def add_handler(
        self,
        header: str,
        *args: Callable,
        overwrite: bool = False
    ):
        txt: str = capsify(f"{header} help")
        txt += "\n\n"
        for x in args:
            if not x.__doc__:
                continue
            txt += "♦️ " + capsify_parts(x.__doc__.replace("{hl}", hl))
            txt += "\n\n"
        if not overwrite:
            if header in self.handlers:
                self.handlers[header] += "\n\n" + txt
            else:
                self.handlers[header] = txt
        else:
            self.handlers[header] = txt            
    def get_handler(self, header: str) -> str:
        text: str = self.handlers.get(header, "")
        return text
    def build_markup(dic: dict) -> IKM:
        return build_help_markup(dic)
help_object: Help = Help()
def add_command(command, help):
    global COMMANDS_HELP
    COMMANDS_HELP[command] = help
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time
def build_help_markup(set):
    le = len(set)
    rows = le // 3
    rows += 1
    rem = le % 3
    buttons = []
    y = []
    a = 0
    filled = 0
    for each in set:
        x = IKB(each, callback_data=each.lower())
        y.append(x)
        a += 1
        if a == 3:
            buttons.append(y)
            filled += 1
            a = 0
            y = []
        if filled == (rows - 1):
            if list(set).index(each) == (le - 1):
                buttons.append(y)
                y = []
    final = IKM(buttons)
    return final
async def load_info():
    global me
    me = await BUNNY.get_me()
async def my_info():
    return me
async def main():
    await load_info()
asyncio.run(main())