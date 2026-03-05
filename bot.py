import os
import asyncio
import discord
from discord.ext import commands
from discord import app_commands
import yt_dlp
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

queues = {}

# -------------------------
# YouTube audio helper
# -------------------------

def get_yt_audio(url):
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "extract_flat": "in_playlist"
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info.get("url")
        title = info.get("title")
        return audio_url, title

# -------------------------
# Commands
# -------------------------

@tree.command(name="join", description="Join your voice channel")
async def join(interaction: discord.Interaction):
    if not interaction.user.voice:
        await interaction.response.send_message("❌ You are not in a voice channel!")
        return

    channel = interaction.user.voice.channel
    vc = await channel.connect()
    await interaction.response.send_message(f"✅ Connected to {channel.name}")

@tree.command(name="leave", description="Leave voice channel")
async def leave(interaction: discord.Interaction):
    if interaction.guild.voice_client:
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("✅ Disconnected")
    else:
        await interaction.response.send_message("❌ I'm not connected to a voice channel!")

@tree.command(name="play", description="Play a YouTube URL")
@app_commands.describe(url="YouTube video URL")
async def play(interaction: discord.Interaction, url: str):
    if not interaction.guild.voice_client:
        if not interaction.user.voice:
            await interaction.response.send_message("❌ You are not in a voice channel!")
            return
        await interaction.user.voice.channel.connect()

    vc = interaction.guild.voice_client
    audio_url, title = get_yt_audio(url)

    if interaction.guild.id not in queues:
        queues[interaction.guild.id] = []
    queues[interaction.guild.id].append((audio_url, title))

    await interaction.response.send_message(f"🎵 Queued: {title}")

    if not vc.is_playing():
        await play_next(interaction.guild.id, vc)

async def play_next(guild_id, vc):
    if queues.get(guild_id):
        audio_url, title = queues[guild_id].pop(0)
        source = discord.FFmpegPCMAudio(audio_url, options="-vn")
        vc.play(source, after=lambda e: asyncio.run_coroutine_threadsafe(play_next(guild_id, vc), bot.loop))
        channel = vc.channel
        await channel.send(f"🎶 Now playing: {title}")

# -------------------------
# Bot events
# -------------------------

@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f"Logged in as {bot.user}!")
    print("Command tree synced!")

bot.run(TOKEN)
