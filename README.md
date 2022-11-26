# DiscordAlwaysOn
## Some python files use discord.py to make your account online 24/7!
Custom status support. Easy to install and customize as long as you have basic knowledge about using and working with Command Prompt/*NIX terminals.
## Installation
### Step 1. Clone this project
```bash
git clone https://github.com/QuanTrieuPCYT/discordalwayson
```
### Step 2. Install Python

You can get binaries for macOS and Windows <a href="https://www.python.org/downloads">here</a>.

Debian distros please do:
```bash
sudo apt install python3
```

You need to figure out the way to install Python if your OS is not included here (should be easy)

### Step 3. Edit main.py

You can use notepad or any text editor that you like. Replace your Discord token with "YOUR TOKEN", your preferred activity type and its content.

Activity types available:
```python
# Setting `Playing ` status
await bot.change_presence(activity=discord.Game(name="Minecraft"))

# Setting `Streaming ` status
await bot.change_presence(activity=discord.Streaming(name="My Stream", url=stream_url))

# Setting `Listening ` status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Setting `Watching ` status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="henta- ah wait youtube"))
```
### Step 4. Install discord.py library
```bash
pip3 install discord.py
```
### Step 5. Run main.py
```bash
python main.py
```
### Step 6. Enjoy :)
## Small note for people who use Replit
Add the following line to the top of `client.run(os.getenv("YOUR TOKEN"), bot=False)`
```python
keep_alive.keep_alive()
```
And you can head to keep_alive.py to edit your Replit site's content (edit `your_site_content`)

## Credit
<a href="https://github.com/ltln">@TheLT</a> for the code!
