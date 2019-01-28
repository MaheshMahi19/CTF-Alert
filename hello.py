import json
import discord
from discord.ext import commands
from discord.ext.commands import Bot
global x
x = {}
client = commands.Bot(command_prefix="'")
@client.event
async def on_ready():
    print("I am ready for CTF's")

@client.command(pass_context=True)
async def addctf(ctx,ctfname:str,date:int,month:str,url:str,*,desc):
    server = ctx.message.server
    if ctfname in x:
        await client.say("CTF is already in List\n If you want to edit use 'edit command")
        return
    x[ctfname] = {"url":url,"date":date,"month":month,"desc":desc,"challs":{}}
    await client.say("CTF has been Added")
    print(x)
@client.command(pass_context=True)
async def editctf(ctx,ctfname:str,date:int,month:int,url:str,*,ndesc:str):
    if ctfname in x:
        x[ctfname] = {"url":url,"date":date,"month":month,"desc":ndesc}
        await client.say("CTF has been Updated")
        print(x)
    else:
        await client.say("Not found any Related CTF")
@client.command(pass_context=True)
async def ctf(ctx,count:int):
    for i in range(count):
        y = x.keys()
        y = list(y)
        xc = x[y[i]]
        em = discord.Embed(title=f"A short info About {y[i]}",colour=discord.Colour.red())
        em.add_field(name="Date and month of CTF challenge",value="%s/%s/2019"%(xc["date"],xc["month"]))
        em.add_field(name="Link for the CTF",value=f"[{y[i].upper()}](https://{xc['url']})")
        em.add_field(name="Description",value="%s"%(xc["desc"]))
        await client.say(embed=em)

@client.command(pass_context=True)
async def addchall(ctx,ctfname,points:int,*,chall:str):
    if ctfname in x:
        y = x[ctfname]["challs"]
        if chall in y:
            await client.say("Challenge is Already inserted")
            return
        y[chall] = {"points":points}
        await client.say(f"Challenge has been added to {ctfname}")
        print(x)
    else:
        await client.say("Nothing is there to add Challenge")
@client.command(pass_context=True)
async def challs(ctx,ctfname):
    if ctfname not in x:
        await client.say("No CTF named to show Challenges")
        return
    challs = x[ctfname]["challs"]
    em = discord.Embed(title="Challenge Name",description="Points of Challenge")
    for i,j in challs.items():
        em.add_field(name=i,value=j["points"])
    await client.say(embed=em)
client.remove_command("help")
@client.command(pass_context=True)
async def help(ctx):
    em = discord.Embed()
    em.add_field(name="Adding a CTF challenge",value="'addctf <ctfname> <date> <month> <link> <description>",inline=False)
    em.add_field(name="Edit a CTF challenge",value="'editctf <ctfname> <date> <month> <link> <description>",inline=False)
    em.add_field(name="To check CTF's",value="'ctf <number>",inline=False)
    em.add_field(name="Add challenge to a CTF",value="'addchall <ctfname> <points> <challenge Name>",inline=False)
    em.add_field(name="To check Challenges in a CTF",value="'challs <ctfname>",inline=False)
    await client.say(embed=em)
@client.command(pass_context=True)
async def total(ctx):
    await client.say(f"Its the Present list **{x}**")
   
@client.command(pass_context=True)
async def remove(ctx,ctfname:str):
    if ctfname in x:
        del x[ctfname]
        await client.say("CTF has been deleted successfully")
    else:
        await client.say("No CTF is there")
    
client.run("NTM5NDc2MzI4NjIyMzI1ODEy.DzC6Cg.e4h5RCju908JpSU7Hf9JLXpQYH8")
print(x)    
