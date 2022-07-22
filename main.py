from asyncio.windows_events import NULL
from http import client
from msilib.schema import Component
import sys
import asyncio
from traceback import print_tb
from turtle import title
import discord
from requests import post, get
import requests
import discord_ui
from os import name as os_name, system
from discord_ui import UI, LinkButton, Button
from discord import Webhook, RequestsWebhookAdapter, embeds, Embed
import discord_webhook
from discord_webhook import DiscordWebhook, DiscordEmbed
import json
from discord.ext import commands
from unblacklister import uniqueId, referentt, assetId, scriptguilz
import os
import secrets
import random
from ad import advertise
from keep_alive import keep_alive
import codecs
import lxml.etree
from xml.dom import minidom
from xml.etree import ElementTree as etree
import discord_buttons_plugin
from discord_buttons_plugin import *
from time import sleep
import requests, base64, random, string
import itertools
bot = commands.Bot(command_prefix=".") #prefix for command

buttons = ButtonsClient(bot)
gamenames = [
  'silentpedro.mp4',
  'Due to an exploit, placing blocks has been disabled.',
  'OOMPALOOMPA.avi',
        'PRAISE OUR LORD AND SAVIOR, DONKEH',
        'Placing blocks is now disabled due to an exploit',
        'ROBLOX IS BETTER',
        'OwO What is this?',
        'Remember to be friendly!',
        'Si vis pacem, para bellum.',
        'Worlds Best Cup of Coffee!',
        'silentpedro.mp4',
        'u w0t m9?',
        'looking for moderators apply now!',
        'Version 6.9.42',
        'succulent hair',
]
"""
Hi :3

My name is Aimee. I'm an aspiring Python and LuaU developer. 
Please don't ask me why I made this bot. I just wanted to make a bot that I could use to make games.

Note: Copyrighted content is not allowed on this bot. If you're uploading content that you do not own, the content will be deleted nearly immediately. UPLOAD YOUR OWN GAMES!!

Please follow Roblox TOS when using this. I am not responsibile for any misuse of this bot.

If you find any bugs, and know how to fix them, please make a pull request. I'd greatly appreciate it. Same for optimizations (ie: automatic generation of captcha tokens)

Thanks :^)

You are allowed to use this bot for industrial/commercial purposes, but you must be able to provide a link to the source code.

Feel free to contact me at million@aimeee.xyz or Million1156#0001



"""
hereweare = [
  'fdsakjsafdkjafsdkj',
  'Sdsfjksadfkjkjdsafkjsadfkj899889skjdf',
  'jfskdksdfakjfadskjsd94893494',
  '[67898765tyghjhuyghj',
  '67yujkjiuy7t6789awe990I09I0R9GISD09GI09FISDG09SIDOBVFJOSIDJU89479873295472937498724389DFJHKASJFASJHFOIUHJAOIFSDJASFIJAFSDFASF',
  'mamamsmmsamksaksa9sa98as98s9a8',
  'asjkaskjasjkkjaskjaskji92949294942',
  'asklsalk9as98sa98sa8989as89s8a9',
  'sa989sa89sa89as99sa9as9sa989as',
  'mamamams98as8989s89sa89as98s9a',
  'bananblexdandxaviontopnmfmfmfmff8489498489',
  'fckworldhistorybrooooooooooooooooo',
  'ihaterobloxadminsxdsocooccclcllcocolcoclccococlclclclcl', # Random strings used to change ScriptGuid
]
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='Aimee is cool', url='https://www.twitch.tv/')) # You can change "Streaming" to "Playing", "Watching", or "Listening", to change the status of the bot. Only recommended if you know what you're doing.
                                                      #          ^ Change this if you'd like to change the status of the bot (https://uploadi.ng/znonBVEn)

def webhook(gameident):
    print("Starting Webhook")



fila = 'b.rbxlx'

doc = lxml.etree.parse(fila)
def UIZ():
    print('UniqueId Unpatched')
    for el in doc.xpath("//UniqueId[@name='UniqueId']"):
        el.text = f'F9FDF9DGJFGIFDIifdgifdgifdghfd80fdgh0gfdhfdg0ofdghfdgofhdguo4g3huo43hofglhol93prewewriewroptretirpe{secrets.token_hex(random.randrange(200, 500))}'
    doc.write(fila)
        # A UniqueId is, well, a unique identifier for an entire file. Since it is unique, Roblox is able to tell if you're constantly uploading the same script/game. We don't want this to happen, so we need to change it every time.

def REF():
    print('Referent Unpatched')
    for el in doc.xpath("//Item[@referent]"):
        string = ''.join(random.choice('LOL') for i in range(random.randrange(15, 30)))
        el.attrib['referent'] = f'ewrewrewruerwewropiewyrpoewre08ryr803h34fsuhdsfudsfdfsjbjfdg540345y8034hdsogfikhgfndjk435453{string}'
    doc.write(fila)
        # A Referent is a unique identifier for a referrer. Since it is unique, Roblox is able to tell if you're constantly uploading the same script/game. We don't want this to happen, so we need to change it every time.

def AI():
    print('AssetId Unpatched')
    for el in doc.xpath("//int64[@name='SourceAssetId']"):
        el.text = f'432j43erwujewhewuoerhoeuwhreoudfofdghofdghgfdolfdgjnehewrohdfsoohfgoddhfosdhodufhdf8043h05hodhfdoghnjlk{secrets.token_hex(random.randrange(100, 200))}'
            # A AssetId is a unique identifier for a Asset. Since it is unique, Roblox is able to tell if you're constantly uploading the same script/game. We don't want this to happen, so we need to change it every time.

    doc.write(fila)
def SG(): 
    print('ok')
    for el in doc.xpath("//string[@name='ScriptGuid']"):
        el.text = '{'f'{random.choice(hereweare)}''-fdggfduofhdgfgodhfgdohdfgo0h4reoretotreoutrewqepfgdjnbmcvcxnvcxucoivuioboubcvxkjbcxvoucxvhvc09x7cvxdfvbiebwpjbpdfpijdfsp654-'f'{random.choice(hereweare)}''-sunshindlaskadskldasklslaade5995}' # Change the file's ScriptGuid to a random string. This is a security measure to prevent Roblox from detecting the file.
    # A ScriptGuid is a unique identifier for a script. Since it is unique, Roblox is able to tell if you're constantly uploading the same script/game. We don't want this to happen, so we need to change it every time.
    doc.write(fila)



def main(cookie):
   # fp = open('og.rbxlx', 't')
   # fp.write('ok')
  #  fp.close()
    
    AI()
    SG()
    REF()
    UIZ()
    
    uniqueId()
    referentt()
    assetId()
    scriptguilz()
    
    token = post("https://auth.roblox.com/v2/logout", 
                 cookies={
                     ".ROBLOSECURITY": cookie
                 }).headers['X-CSRF-TOKEN']
    userId = requests.get("https://users.roblox.com/v1/users/authenticated",
                          headers={
                              'x-csrf-token': token,
                              'User-Agent': 'Roblox',
                                "Connection": "keep-alive"
                          },
                          cookies={
                              '.ROBLOSECURITY': cookie # Does the patching and Asset Uploading (it's supposed to avoid detection but it doesn't :( )
                          }).json()["id"]
    print(f" [DATA] {userId} - UserID")
    gameId = requests.get("https://inventory.roblox.com/v2/users/" +
                          str(userId) + "/inventory/9?limit=10&sortOrder=Asc",
                          headers={
                              'x-csrf-token': token,
                              'User-Agent': 'Roblox'
                          },
                          cookies={
                              '.ROBLOSECURITY': cookie
                          }).json()["data"][0]["assetId"]
    print(f" [DATA] {gameId} - GameID")
    
    N = 2 # <-- This is important, don't remove this
    
    
    myfiles = open("b.rbxlx", "rb").read() # Acknowledge the file that we're going to upload
    unvid = get(
        "https://api.roblox.com/universes/get-universe-containing-place?placeid="
        + str(gameId)).json()["UniverseId"]
    print(f" [DATA] {unvid} - UniverseID")
    url = f"https://data.roblox.com/Data/Upload.ashx?assetid={str(gameId)}"

    url2 = f"https://develop.roblox.com/v2/universes/{str(unvid)}/configuration"

    avatartype = "MorphToR6"
    allowprivateservers = True # Do we want to allow private servers?

    gamedatao = { # Our specific options we want for the game. This can be changed to anything you'd like, but I recommend keeping everything but the description and the name the same.
        "name": random.choice(gamenames) ,
        "description": """NEW UPDATE 👀👀👀👀👀👀
        INCLUDES:
        - New Roblox Studio ✅
        - Better optimization 🏃
        - The world seems to be changing.. 🤔⚫
        
        Join the Schwifty Studios Group for 15 free levels and an exclusive pet :D""",
        "universeAvatarType": avatartype,
        "universeAnimationType": "Standard",
        "maxPlayerCount": 50,
        "allowPrivateServers": allowprivateservers, # Uses the constant above to determine if we want private servers or not.
        "privateServerPrice": 0, # If yes, then how much? (0 = free, minimum paid = 25rbx)
        "permissions": {
            "IsThirdPartyTeleportAllowed": True,
            "IsThirdPartyPurchaseAllowed": True
        }
    }
    gameDump = json.dumps(gamedatao)
    gamestats = requests.patch(
        url2,
        headers={
            'Content-Type': 'application/json',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'x-csrf-token': token
        },
        cookies={'.ROBLOSECURITY': cookie},
        data=gameDump)
    gameData2 = {
        "maxPlayerCount": 55,
    }
    gamestat = requests.patch(
        url2,
        headers={
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36', # This is used to check if the game actually successfully uploaded
            'x-csrf-token': token
        },
        cookies={'.ROBLOSECURITY': cookie},
        data=gameData2)
    print(f" [DATA] {gamestat.status_code} - Successfull upload") # This is where we upload the actual game, using Roblox's official headers (so they think it was uploaded from a roblox server)
    upload = post(url,
                  headers={
                      'Content-Type': 'application/xml',
                      'User-Agent': 'Roblox', 
                      'x-csrf-token': token
                  },
                  cookies={'.ROBLOSECURITY': cookie},
                  data=myfiles)  
    if upload.status_code == 400:
       print("works") # If the upload is successful, then we tell the console it worked.
       webhook(gameId)

    global link
    link =  gameId

"""
The code below is how the headers are passed (this way roblox knows what we're doing, the account name, our UA, etc)
"""
def captchatoken(token):
    print("Starting.")
    headers = {
    'authority': 'auth.roblox.com',
    'dnt': '1',
    'x-csrf-token': requests.post("https://auth.roblox.com/v2/login").headers["x-csrf-token"],
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'accept': 'application/json, text/plain, */*', 
    }

    username = 'q'.join(random.choice(string.ascii_letters) for i in range(8))
    
    tokens = base64.b64decode(token).decode('utf-8').split(',')
    data = {
    "username":username, # The random username(s) we generated
    "password":"122121212ddd", # You can set this to whatever you'd like, preferably a strong password so your game doesn't get hijacked
    "birthday":"01 Oct 1999", # The birthday of the account, this can be anything as long as you follow the format (DD MM YYYY)
    "gender":2, # Boy or girl? (roblox is sexist omgomg)
    "isTosAgreementBoxChecked":True, # Have we agreed to the TOS? 
    "context":"MultiverseSignupForm", # Considering the data and header(s) that we have, what are we ACTUALLY doing? This header determines that.
    "referralData":None, # ie: did the user click on a facebook link to signup (because we didn't, we set it to None)
    "displayAvatarV2":False, 
    "displayContextV2":False,
    "captchaId":tokens[0],
    "captchaToken":tokens[1], 
    "captchaProvider":"PROVIDER_ARKOSE_LABS", # Since SignUp uses Arkose Labs's Captcha (FunCaptcha), we have to declare that they are the provider
    "agreementIds":['54d8a8f0-d9c8-4cf3-bd26-0cbf8af0bba3','848d8d8f-0e33-4176-bcd9-aa4e22ae7905'] #agreement ids, dont know what they are but roblox says they are important
  
    }

    response = requests.post('https://auth.roblox.com/v2/signup', headers=headers, json=data)
    print(response)
    print(username)
    try:
       cookiez = response.cookies[".ROBLOSECURITY"]
       print()
      # print(f'login: {username}:{username[::-1]}')
       print(f'\nCookie:\n{cookiez}')
       main(cookiez)
    except:
       print("Failed to create account.")
       pass
@bot.command()
@commands.has_permissions(administrator=True) 
async def file(ctx):
    if ctx.author == bot.user: 
        return
    print("File Upload Mode Initiated")
    embed = discord.Embed(
            title = "Please Insert a Valid File",
        )
    embed.set_footer(text='Aimee was here')
    sent = await ctx.send(embed=embed) 
    #discontinued0
@bot.command()
@commands.has_permissions(administrator=True) 
async def upload(ctx):
    if ctx.author == bot.user: 
        return
    await ctx.send("Insert a valid captcha token to upload.") # Uploads the game and creates an account using a FunCaptcha token (FYI: you can grab a token here: https://roblox-captcha-v2.herokuapp.com/ ) 
    tokenz = await bot.wait_for("message") # Wait until the user inputs the captcha token.
    captchatoken(tokenz.content) # Use the captchatoken function to create an account and upload the game.
@bot.command()
@commands.has_permissions(administrator=True) 
async def game(ctx):  # Uploads the game using the .ROBLOSECURITY cookie from the user
  if ctx.author == bot.user:
    return
  embed = discord.Embed(
            title = "Please Insert a Valid Cookie",
        )
  embed.set_footer(text='Aimee was here')

  sent = await ctx.send(embed=embed)  
  cookieinput = await bot.wait_for("message")
  if '_|WARNING' in cookieinput.content: # Is this valid? If it is, then let them know.
         embed = discord.Embed(
            title = "Valid Cookie...",
        )
         embed.set_footer(text='Aimee was here')

  else:
     await ctx.send("Invalid Cookie") # If it is not, then tell them.
     return
  sent = await ctx.send(embed=embed) 
  await ctx.send("Successfully Uploaded Game") # Let them know that the game has been uploaded, but not before it actually uploads.
  main(cookieinput.content)
  await buttons.send(
		content = "Game-Link Below",
		embed = None,
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					style = ButtonType().Link,
					label = "Game-Link",
					url = f"https://www.roblox.com/games/{link}/" # When we upload, make a discord button (like this: https://uploadi.ng/hJjHLwY8 ) that links to the game.
				)
			])
		]
	)
@bot.command()
@commands.has_permissions(administrator=True) 
async def a(ctx):
    embed = discord.Embed(title="Success upload", color=0xdd1c1c, description="click the button to open link")
    embed.set_footer(text="this part took like an hour fucking discord api today 😭😭😭")
    await buttons.send(
		content = " ",
		embed = embed,
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(
					style = ButtonType().Link,
					label = "Game-Link",
					url = f"https://www.roblox.com/games/{link}/"
				)
			])
		]
	)
    await ctx.message.delete()
keep_alive()
bot.run('OTkzNjE4MjI3MzQxMDM3Njk4.GpsFmh.MiCfk8Rkqv8Zq-_tZsZO5p8FDN-zD4SiT2G69Y')
