import logging
import discord
from discord.ext.commands import Bot
import asyncio
import random
import datetime

client = discord.Client()
bot = Bot("&")
logging.basicConfig(level=logging.INFO)
dash = "|------------------------------------------------|"

#client events
@client.event
async def on_ready():
    namelen = len(str(client.user.name))

    if namelen >= 14:
        spaces = 0
    else:
        spaces = 14-namelen

    print("| ",client.user.name,"functional |",' '*spaces)
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
    while not client.is_closed:
        when = random.randrange(0, 24 * 3600 * 7)
        when2 = random.randrange(0, 604800-when)

        '''
        Math to get exact time, because sleep only accepts arguments in seconds so
        hour, minute, and second is used to set a timedelta object, which is added 
        to the current day.  A small console feature
        '''

        d = 86400
        h = 3600
        ms = 60
        day = when/d
        day2 = (when2+when)/d
        hour = ((when%d)/h)
        hour2 = (((when2+when)%d)/h)
        minute = (((when%d)%h)/ms)
        minute2 = ((((when2+when)%d)%h)/ms)
        second = ((((when%d)%h)%ms)/ms)
        second2 = (((((when2+when)%d)%h)%ms)/ms)
        td = datetime.datetime.today()
        timewhen = datetime.timedelta(days=day,hours=hour,minutes=minute,seconds=second)
        timewhen2 = datetime.timedelta(days=day2,hours=hour2,minutes=minute2,seconds=second2)

        print("|  First image: ", td + timewhen, "     |")
        print("| Second image: ", td + timewhen2, "     |")
        print(dash)
        channel = client.get_all_channels()

        #coroutine execution
        await asyncio.sleep(when)
        client.send_message(channel, random.choice("os.listdir(PATH"))
        await asyncio.sleep(when2)
        client.send_message(channel, random.choice("os.listdir(PATH"))


client.loop.create_task(background_loop())
client.run('CLIENT HERE')
