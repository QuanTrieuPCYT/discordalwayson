# DiscordAlwaysOn
Some python files use discord.py to make your account online 24/7!
Currently running that same stuff on my Raspberry Pi 4 server!
With custom status support. Easy to install and customize as long as you have basic knowledge about using and working with terminal/Windows cmd.
## Installation
1. Clone this project
```bash
git clone https://github.com/QuanTrieuPCYT/discordalwayson
```
2. Install Python (we want python3 🐧)
Windows please head to <a href="https://www.python.org/downloads/windows">python.org</a>.
macOS also <a href="https://www.python.org/downloads/mac-osx">python.org</a>
Ubuntu/Debian do:
```
sudo apt install python3
```
Other Linux distros go figure them out by yourself.
3. Edit main.py
You can use notepad or any text editor that you like. Replace your Discord token with "YOUR TOKEN", your preferred activity type and its content.
Activity types available:
```
# Setting `Playing ` status
await bot.change_presence(activity=discord.Game(name="Minecraft"))

# Setting `Streaming ` status
await bot.change_presence(activity=discord.Streaming(name="My Stream", url=stream_url))

# Setting `Listening ` status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Setting `Watching ` status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="henta- ah wait youtube"))
```
4. Install discord.py library
```
pip3 install discord.py
```
5. Run main.py
```
python main.py
```
6. Enjoy :)
## Note for people who use Replit
Add the followings right on top of `client.run(os.getenv("YOUR TOKEN"), bot=False)`
```
keep_alive.keep_alive()
```
And you can head to keep_alive.py to edit your Replit site's content (edit `your_site_content`)

## Credit
@ItzTheLT for the code!
