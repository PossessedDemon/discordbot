from typing import List

import discord
import asyncio
import unicodedata as uc

f = open(r"C:\Users\HP\Desktop\DiscordBot\bottoken.txt", "r")
client = discord.Client()

#["cosplayer","ghost","house wife","youtuber","fast food cook","internet troll","twitch streamer","teacher","police officer,"developer","dank memer developer,","politician","scientist","dictator"]
@client.event
async def on_message(message):
    pingables = ["@everyone", "@here",""]
    dankmemerlist = [
        '''ahhhhh the fish is too strong and your line is at risk to break! quick, type the phrase below in the next 10 seconds
Type ''',
        '''**Work for Dictator** - Retype - Retype the following phrase below.
Type ''']
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', ' ']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
    placevalue = 0
    value = 0
    #sample code
    if message.content.startswith('hello'):
        await message.channel.send("this is template code lol")
    #dick ping
    if message.content.startswith("m!ping"):
        for i in message.content:
            if not i.isdigit():
                continue
            elif i.isdigit():
                await message.channel.send(pingables[int(i)])

    if message.mention_everyone == True:
        if message.author.id == 715229742131052618:
            await message.channel.purge(limit=2, check=None, before=None, after=None, around=None, oldest_first=False, bulk=True)
            if message.channel.id == 721526844985311263:
                await message.channel.purge(limit=1, check=None, before=None, after=None, around=None, oldest_first=False, bulk=True)

    if message.content.startswith("m!ship"):
        if " // " not in message.content:
            await message.channel.send("bruh use ' // ' to differentiate the ships dummy")
        else:
            part1 = message.content.replace(" // ", "")
            part2 = part1.replace("m!ship", "")
            for char in part2:
                longname = uc.name(char)
                while longname[placevalue] != alphabet[placevalue]:
                    placevalue += 1
                if longname[placevalue] == alphabet[placevalue]:
                    value += numbers[placevalue]
                    placevalue = 0
                if value > 100:
                    value -= 101
            await message.channel.send(f"That ship was... interesting. But I calculated it and it has a value of {value + 13}")

    #halted for some time
    '''   if int(message.author.id) == 498917718884483103:
        if dankmemerlist[0] in message.content():
            await message.channel.send("step 1 done")
            for i in message.content:
                while i != "`":
                    placevalue += 1
                if i == "`":
                    await message.channel.send("step 2 done")
                    onemorestep = message.conten[:placevalue]
            printthisout = message.content.replace(onemorestep, "")
            await message.channel.send(printthisout)


        elif dankmemerlist[1] in message.content():
            for num in range(len(message.content)):
                while message.content[num] != "`":
                    message.channel.send("not it yet chief")
                if message.content[num] == "`":
                    settingup = message.content[:num]
                    findinvis = message.content.replace(settingup, "")
                    dankmemerprint = findinvis.replace("", "")
                    await message.channel.send(dankmemerprint)'''
client.run(f.read())
