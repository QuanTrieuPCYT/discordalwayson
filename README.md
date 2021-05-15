# DiscordAlwaysOn
Some python files use discord.py to make your account online 24/7!
With custom status support. Easy to install and customize as long as you know Python.
## Installation
1. Clone this project
```bash
git clone https://github.com/QuanTrieuPCYT/discordalwayson
```
2. Edit main.py
You can use notepad or whatever you like. Replace your Discord token with "YOUR TOKEN", your preferred activity type and its content.
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
3. Run main.py
```
python main.py
```
Or you can just double click the file.
5. Enjoy :)
## Credit
<a href="https://github.com/Nekos-life/nekos-dot-life">Nekos.life</a> and <a href="https://www.npmjs.com/package/lolis.life">Lolis.life</a> for Images gallery.
<a href="https://www.facebook.com/thewholesomesquad">Wholesome Squad</a> for inspiring me
## License
This project is licensed under the GNU General Public License v3.0 License - see the [LICENSE](LICENSE) file
