from dhooks import Webhook
import discord
import time
#from rich import *
from rich.console import *



theme = Theme({"success": "green", "error": "red", "default" : "magenta"})

console = Console(theme=theme)

console.print (""" 

 _       ____________  __  ______  ____  __ __      _____ ____  ___    __  _____  _____________ 
| |     / / ____/ __ )/ / / / __ \/ __ \/ //_/     / ___// __ \/   |  /  |/  /  |/  / ____/ __ \
| | /| / / __/ / __  / /_/ / / / / / / / ,<        \__ \/ /_/ / /| | / /|_/ / /|_/ / __/ / /_/ /
| |/ |/ / /___/ /_/ / __  / /_/ / /_/ / /| |      ___/ / ____/ ___ |/ /  / / /  / / /___/ _, _/ 
|__/|__/_____/_____/_/ /_/\____/\____/_/ |_|     /____/_/   /_/  |_/_/  /_/_/  /_/_____/_/ |_|  
                                                                                                                                                                    
                                    made by: 0x7n
                                    github: 0x7n

""", style = "bold magenta")



webhookUrl = Webhook(input("enter webhook url: "))
embedTitle = input("enter the title of the embed: ")
embedMessage = input("enter message in the embed: ")
embedAuthor = input("enter the footer for the embed: ")
embedImage = input("enter url to image in the embed: ")
delay = float(input("delay: "))

embed = discord.Embed(
    title = embedTitle, description=embedMessage, colour=discord.Colour.random(), 
)
embed.set_image(url = embedImage)
embed.set_author(name=embedAuthor)

sent = 0

while True:
    webhookUrl.send(embed=embed)
    print("[+] sent embed to webhook [" + str(sent) + "]")
    time.sleep(delay)
    sent+=1