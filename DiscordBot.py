import discord
from discord.ext import commands,tasks
import psutil

intent = discord.Intents.default()
client = discord.Client(intents=intent)

TOKEN = 'Add DiscordBot TOKEN'
# SREVER_PATH = ''
# HOME_DIRECTORY = ''
CHANNEL_ID = 0123456789 # Rewrite Discord channel ID

global serverStatus
global memoryAlertSend

serverStatus = "PalServer.exe" in (p.name() for p in psutil.process_iter())
memoryAlertSend = False

@tasks.loop(seconds=5)
async def check_status():
    global serverStatus
    global memoryAlertSend
    memoryUsage = psutil.virtual_memory().percent
    if "PalServer.exe" in (p.name() for p in psutil.process_iter()) and not serverStatus:
        serverStatus = True
        Launch_embed = discord.Embed(
            title="サーバーが起動しました",
            color=0x00ff00, # 緑
        )
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(embed=Launch_embed)
    elif not "PalServer.exe" in (p.name() for p in psutil.process_iter()) and serverStatus:
        serverStatus = False
        ShoudDown_embed = discord.Embed(
            title="サーバーが停止しました",
            color=0xff0000, # 赤
        )
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(embed=ShoudDown_embed)

    if memoryUsage >= 80 and not memoryAlertSend:
        memoryAlertSend = True
        Alert_embed = discord.Embed(
            title="サーバーのメモリ使用量が80%を超えました",
            color=0xffff00, # 黄
            description="サーバーの状態を確認することを推奨します",
        )
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(embed=Alert_embed)
    elif memoryUsage < 80 and memoryAlertSend:
        memoryAlertSend = False

@client.event
async def on_ready():
    global serverStatus
    global memoryAlertSend
    print('PalServer Launched!')
    BotLaunch = discord.Embed(
        title="Botが起動しました",
        color=0x00ff00 if serverStatus else 0xffff00, # 緑(サーバー起動中), 黄色(サーバー停止中)
        description="サーバーは起動中です" if serverStatus else "サーバーは停止中です"
    )
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(embed=BotLaunch)
    check_status.start()

client.run(TOKEN)
