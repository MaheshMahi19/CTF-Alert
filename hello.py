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
async def addctf(ctx,ctfname:str,date:str,url:str,*,desc):
    server = ctx.message.server
    if ctfname in x:
        await client.say("CTF is already in List\n If you want to edit use 'edit command")
        return
    x[ctfname] = {"url":url,"date":date,"desc":desc,"challs":{}}
    await client.say("CTF has been Added")
    print(x)
@client.command(pass_context=True)
async def editctf(ctx,ctfname:str,date:str,url:str,*,ndesc:str):
    if ctfname in x:
        x[ctfname] = {"url":url,"date":date,"desc":ndesc}
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
        em.add_field(name="Date and month of CTF challenge",value="%s  2019"%(xc["date"]))
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
        

@client.command(pass_context=True)
async def poll(ctx,*,ptitle):
    em=discord.Embed(description=ptitle)
    x = await client.say(embed=em)
    await client.add_reaction(x,emoji="✅")
    await client.add_reaction(x,emoji="❌")

@client.command(pass_context=True)
async def events(ctx,limit:int):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    url = f"https://ctftime.org/api/v1/events/?limit={limit}"
    print(url)
    req = requests.get(url=url,headers=headers)
    res = json.loads(req.content.decode('utf-8'))
    for i in res:
        orgs = i["organizers"][0]["name"]
        on = i["onsite"]
        desc = i["description"]
        titl = i["title"]
        ctfurl = i["ctftime_url"]
        time,days = (i["duration"]["hours"],i["duration"]["days"])
        part = i["participants"]
        logo = i["logo"]
        finish = i["finish"]
        finish = finish.replace("T","")
        finish = finish.replace("+00:00","")
        start = i["start"]
        start = start.replace("T","")
        start = start.replace("+00:00","")
        em = discord.Embed(title=orgs,description=desc,colour=1432433)
        em.add_field(name="CTF official URL",value=ctfurl,inline=False)
        em.add_field(name="CTF Title",value=titl,inline=False)
        em.add_field(name="Time to CTF",value="%s days and %s hours"%(days,time),inline=False)
        em.add_field(name="Current Participants",value=part,inline=False)
        em.add_field(name="Is it online",value=on,inline=False)
        em.add_field(name="Start Time of CTF(UTC)",value=start,inline=False)
        em.add_field(name="End time of CTF(UTC)",value=finish,inline=False)
        em.set_thumbnail(url=logo)
        await client.say(embed=em)
@client.command(pass_context=True)
async def past(ctx,limit:int,year:int,month:int,date:int):
    from datetime import datetime
    ts = datetime(year,month,date).timestamp()
    ts = int(ts)
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    url = f"https://ctftime.org/api/v1/events/?limit={limit}&start={ts}"
    print(url)
    req = requests.get(url=url,headers=headers)
    res = json.loads(req.content.decode('utf-8'))
    print(res)
    try:
        for i in res: 
            orgs = i["organizers"][0]["name"]
            on = i["onsite"]
            desc = i["description"]
            titl = i["title"]
            ctfurl = i["ctftime_url"]
            time,days = (i["duration"]["hours"],i["duration"]["days"])
            part = i["participants"]
            logo = i["logo"]
            finish = i["finish"]
            finish = finish.replace("T","")
            finish = finish.replace("+00:00","")
            start = i["start"]
            start = start.replace("T","")
            start = start.replace("+00:00","")
            em = discord.Embed(title=orgs,description=desc,colour=1432433)
            em.add_field(name="CTF official URL",value=ctfurl,inline=False)
            em.add_field(name="CTF Title",value=titl,inline=False)
            em.add_field(name="Time to CTF",value="%s days and %s hours"%(days,time),inline=False)
            em.add_field(name="Current Participants",value=part,inline=False)
            em.add_field(name="Is it online",value=on,inline=False)
            em.add_field(name="Start Time of CTF(UTC)",value=start,inline=False)
            em.add_field(name="End time of CTF(UTC)",value=finish,inline=False)
            em.set_thumbnail(url=logo)
            await client.say(embed=em)
    except:
        await client.say("Its an Error")
        
client.run("NTM5NDc2MzI4NjIyMzI1ODEy.DzC6Cg.e4h5RCju908JpSU7Hf9JLXpQYH8")
print(x)    
