import logging
import discord
from discord.ext.commands import Bot
import asyncio
import random
import datetime
import os

client = discord.Client()
bot = Bot("&")
logging.basicConfig(level=logging.INFO)

dash = "|------------------------------------------------|"


file = input("Enter the folder you want to use: ")
if not os.path.exists(file):
    file = input("Not a valid path.  Try again: ")

frequency = int(input("How many times a week should the bot post (1-10): "))
if frequency not in range(0, 10):
    frequency = input("That is not a valid input, please enter a number (1-10): ")

#client events
@client.event
async def on_ready():
    
    namelen = len(str(client.user.name))

    if namelen >= 14:
        spaces = 0
    else:
        spaces = namelen - 14

    print("| ",client.user.name,": Live     |",' '*spaces)
    print("|  ID: ",client.user.id,"  |")
    print("|____________________________|")

@client.event
async def on_message(message):
    if message.content == "TRIGGER MESSAGE":
        await client.send_message(message.channel, "BOT RESPONSE")

#randomizer, time output formatting
async def background_loop():
    await client.wait_until_ready()
    print("____________________")
    print("| Coroutine active |")
    print(dash)
    while True:
        times = sorted([random.randrange(1,604801,1) for _ in range(10)])

        '''
        Math to get exact time, because sleep only accepts arguments in 
        seconds so the day, hour, minute, and second that that range 
        represents is used to set a timedelta object, which is added to 
        the current day.  Run through a loop for frequency
        '''

        def time_format(when):
            d = 86400
            h = 3600
            ms = 60
            day = when/d
            hour = ((when%d)/h)
            minute = (((when%d)%h)/ms)
            second = ((((when%d)%h)%ms)/ms)
            td = datetime.datetime.today()
            timewhen = datetime.timedelta(days=day, hours=hour, minutes=minute, seconds=second)
            return td + timewhen

        # coroutine execution
        for x in range(0, frequency):
            print("| Image ", x+1, ": ", time_format(times[x]), "        |")
            print(dash)

        while time_format(times[x]) > datetime.datetime.today():
            await asyncio.sleep(1)
            client.send_message(channel, random.choice(os.listdir("{}".format(file))))



channel = client.get_all_channels()
client.loop.create_task(background_loop())
client.run(TOKEN)
