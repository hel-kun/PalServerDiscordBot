import discord
from discord.ext import tasks
from discord import app_commands
import psutil, time, subprocess,os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client(
    intents=discord.Intents.default(),
    activity=discord.Game("PalServer")
)
tree = app_commands.CommandTree(client)

TOKEN = os.getenv("TOKEN")
SERVER_PATH = os.getenv("SERVER_PATH")
# HOME_PATH = os.getenv("HOME_PATH")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

serverStatus = "PalServer.exe" in (p.name() for p in psutil.process_iter())
memoryAlertSend = False
last_notification_time = 0

@tasks.loop(seconds=5)
async def check_status():
    global serverStatus
    global memoryAlertSend
    global last_notification_time
    memoryUsage = psutil.virtual_memory().percent
    current_time = time.time()
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
        last_notification_time = current_time
        channel = client.get_channel(CHANNEL_ID)
        await channel.send("<@941988870730420244>",embed=Alert_embed)
    elif (current_time - last_notification_time) >= 1800 and memoryAlertSend:
        memoryAlertSend = False

@tree.command(name="check_server", description="現在サーバーが起動しているかを調べます")
async def check_server(interaction: discord.Interaction):
    serverStatus = "PalServer.exe" in (p.name() for p in psutil.process_iter())
    SeachServer_embed = discord.Embed(
        title="サーバーは起動中です" if serverStatus else "サーバーは停止中です",
        color=0x00ff00 if serverStatus else 0xff0000 # 緑(サーバー起動中), 黄色(サーバー停止中)
    )
    await interaction.response.send_message(embed=SeachServer_embed)

@tree.command(name="check_memory", description="現在のサーバーのメモリ使用量を調べます")
async def check_memory(interaction: discord.Interaction):
    memoryUsage = psutil.virtual_memory().percent
    SeachMemory_embed = discord.Embed(
        title=f"現在のメモリ使用量は{memoryUsage}%です",
        color=0x0000ff
    )
    await interaction.response.send_message(embed=SeachMemory_embed)

@tree.command(name="start_server", description="PalServer.exeを起動します")
async def start_server(interaction: discord.Interaction):
    global SERVER_PATH
    try:
        subprocess.run(["start", SERVER_PATH], shell=True)
        ServerStart_embed = discord.Embed(
            title="PalServer.exeを起動します",
            color=0xffff00
        )
        await interaction.response.send_message(embed=ServerStart_embed)
    except Exception as e:
        ServerStartError_embed= discord.Embed(
            title="PalServer.exeを起動できませんでした",
            description=f"Eroor: {str(e)}",
            color=0xff0000
        )
        await interaction.response.send_message(embed=ServerStartError_embed)

@tree.command(name="stop_server", description="palServer.exeを停止します")
async def stop_server(interaction: discord.Interaction):
    global SERVER_PATH
    try:
        subprocess.run(["taskkill", "/IM", "PalServer-Win64-Test-Cmd.exe", "/F"], shell=True)
        ServerStop_embed = discord.Embed(
            title="PalServer.exeを停止します",
            color=0xffff00
        )
        await interaction.response.send_message(embed=ServerStop_embed)
    except Exception as e:
        ServerStopError_embed= discord.Embed(
            title="PalServer.exeを停止できませんでした",
            description=f"Eroor: {str(e)}",
            color=0xff0000
        )
        await interaction.response.send_message(embed=ServerStopError_embed)

@client.event
async def on_ready():
    global serverStatus
    global memoryAlertSend
    global last_notification_time
    print('PalServer Launched!')
    await tree.sync()
    BotLaunch = discord.Embed(
        title="Botが起動しました",
        color=0x00ff00 if serverStatus else 0xffff00, # 緑(サーバー起動中), 黄色(サーバー停止中)
        description="サーバーは起動中です" if serverStatus else "サーバーは停止中です"
    )
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(embed=BotLaunch)
    check_status.start()

client.run(TOKEN)