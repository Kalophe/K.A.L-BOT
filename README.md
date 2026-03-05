# Kal_Bot 🎵

A private Discord music bot for your server.  
Play YouTube songs directly in voice channels using **Python 3.10+**.  

> This bot is designed for personal/private use. `.env` and `venv` are ignored for security.

---

## Features

- Join your voice channel automatically
- Play songs from YouTube (search or full URL)
- Queue multiple songs
- Show “now playing” messages
- Works out-of-the-box on macOS, Linux, and Windows

---

## Requirements

- Python 3.10 or higher
- `ffmpeg` installed and accessible in your PATH
- A Discord bot token

---

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/Kalophe/K.A.L-BOT.git
cd Kal_Bot
```
2.	**Create a .env file:**

Copy the example and add your bot token and guild ID:

```bash
cp .env.example .env
```

Edit .env with your credentials:

```bash
TOKEN=YOUR_BOT_TOKEN_HERE
GUILD_ID=YOUR_GUILD_ID_HERE
```

3.	**Run the bot using the included script:**

```bash
./run.sh
```

> The script automatically creates a virtual environment (venv), installs dependencies, and runs the bot.

---

## Commands

	/play <song> – Play a song from YouTube
	/skip – Skip the current song
	/queue – Show the current queue
	/remove <position> – Remove a song from the queue

> Commands are private to your server by default.

---

## Dependencies

Listed in requirements.txt:

- discord.py[voice] – Discord bot framework with voice support
- yt-dlp – YouTube downloader for streaming
- python-dotenv – Load .env variables
- PyNaCl – Required for Discord voice

Install manually if needed:

```bash
python3 -m pip install -r requirements.txt
```

---
## License

This project is licensed under the MIT License.

- Free to use, modify, and share
- Commercial use is **not allowed**
- Attribution required
