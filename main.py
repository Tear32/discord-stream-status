import          discord
import          logging
import          os
import          json
import          asyncio
import          discord.state
import          time


from colorama           import Fore, init
from discord.ext        import commands
from ctypes             import windll


init(autoreset=True)

# Console colors
red = Fore.RED
white = Fore.WHITE
pink = Fore.LIGHTMAGENTA_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
blue = Fore.BLUE

with open("config.json") as f:
    config = json.load(f)

token = config['token']
streamname = config['streamname']
streamlink = config['streamlink']


def setwindowtitle(title):
    windll.kernel32.SetConsoleTitleW(title)

def setup():
    windll.kernel32.SetConsoleTitleW(f"selftear")
    os.system("echo off")
    os.system("pip install colorama requests logging asyncio discord.py-self")
    os.system("cls")



logging.getLogger('discord').setLevel(logging.CRITICAL)
logging.getLogger('discord.http').setLevel(logging.CRITICAL)
class ColoredFormatter(logging.Formatter):
    def format(self, record):
        levelname = record.levelname
        if levelname == 'ERROR':
            levelname = f"{red}[ERROR]{white}"
        elif levelname == 'WARNING':
            levelname = f"{magenta}[WARNING]{white}"
        elif levelname == 'INFO':
            levelname = f"{pink}[INFO]{white}"
        elif levelname == 'DEBUG':
            levelname = f"{white}[DEBUG]{white}"
        else:
            levelname = f"{white}[{levelname}]{white}"
        record.levelname = levelname
        return super().format(record)

formatter = ColoredFormatter('%(asctime)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)  


tear = commands.Bot(command_prefix="?", self_bot=True)



def mainlogo():
    print(rf"""
{magenta}  __                         ______________                .__   ________.           __   
{pink}_/  |_  ____ _____ _______  /  |  \______  \   ______ ____ |  |_/ ____\_ |__   _____/  |_ 
{magenta}\   __\/ __ \\__  \\_  __ \/   |  |_  /    /  /  ___// __ \|  |\   __\ | __ \ /  _ \   __\
{pink} |  | \  ___/ / __ \|  | \/    ^   / /    /   \___ \\  ___/|  |_|  |   | \_\ (  <_> )  |  
{magenta} |__|  \___  >____  /__|  \____   | /____/   /____  >\___  >____/__|   |___  /\____/|__|  
{pink}           \/     \/           |__|               \/     \/                \/             
                {lightblue} Selfbot made by @tear47 {red} dc: @tear47 {lightblue} t.me/sameoldways

""")


async def startup():
    print("Installing required libraries...")
    os.system("pip install asyncio discord.py-self colorama logging")
    os.system("cls")
    mainlogo()
    print(f"""
{white} loading {lightblue}tear47's {magenta}streaming utility
""")
    time.sleep(1)
    if token == "":
        input(f"{red}[ERROR]{white} Please enter a token...")
        return
    if streamname == "": 
        input(f"{red}[ERROR]{white} Please enter a stream name...")
        return
    if streamlink == "": 
        input(f"{red}[ERROR]{white} Please enter a stream link...")
        return
    
    os.system("CLS")

@tear.event
async def on_ready():
    try:
        startup()

        os.system("cls")
        setwindowtitle("tear47 selfbot")
        relationships = await tear.fetch_relationships()
        guilds = len(tear.guilds)
        mainlogo()
        print(f"{pink}------------------------------")
        print(f"{pink}| {magenta}Logged in as: {tear.user.name}#{tear.user.discriminator}")
        print(f"{pink}| {magenta}Friends: {len(relationships)}")
        print(f"{pink}| {magenta}Servers: {guilds}")
        print(f"{pink}------------------------------")
        print(rf"""
        
        {white} set streaming status as: {pink} {streamname}(name), twitch.tv/{streamlink} (link)
        """)
        await tear.change_presence(activity=discord.Streaming(name=streamname, url=f"https://www.twitch.tv/{streamlink}"), afk=False, edit_settings=False)
    except Exception as e:
        logging.error("An error occurred in on_ready", exc_info=True)  



tear.run(token)

