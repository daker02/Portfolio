import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
import time
import asyncio
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio

bot = commands.Bot(command_prefix='!')
client = discord.Client()

user = [] #유저가 입력한 노래
musictitle = [] #노래제목
song_queue = [] #노래링크
musicnow = [] # 현재 출력되는 노래

userF = []
userFlist = []
allplaylist = []

number = 1

def title(msg):
    global music

    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    chromedriver_dir = r"G:\Microsoft VS Code\discordbot\chromedriver.exe"
    driver = webdriver.Chrome(chromedriver_dir, options= options)
    driver.get("https://www.youtube.com/results?search_query=" + msg)
    source = driver.page_source
    bs = bs4.BeautifulSoup(source, 'lxml')
    entire = bs.find_all('a', {'id': 'video-title'})
    entireNum = entire[0]
    music = entireNum.text.strip()

    musictitle.append(music)
    musicnow.append(music)
    test1 = entireNum.get('href')
    url = 'https://www.youtube.com' + test1
    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
    URL = info['formats'][0]['url']

    driver.quit()

    return music, URL

def play(ctx):
    global vc
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    URL = song_queue[0]
    del musicnow[0]
    del musictitle[0]
    del song_queue[0]
    vc = get(bot.voice_clients, guild=ctx.guild)
    if not vc.is_playing():
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: play_next(ctx))

def play_next(ctx):
    if len(musicnow) - len(user) >= 2:
        for i in range(len(musicnow) - len(user) - 1):
            del musicnow[0]
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    if len(user) >= 1:
        if not vc.is_playing():
            del musicnow[0]
            URL = song_queue[0]
            del user[0]
            del musictitle[0]
            del song_queue[0]
            vc.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: play_next(ctx))

def load_chrome_driver():

    options = webdriver.ChromeOptions()

    options.binary_location = os.getenv('GOOGLE_CHROME_BIN')

    options.add_argument('--headless')
    # options.add_argument('--disable-gqu')
    options.add_argument('--no-sandbox')

    return webdriver.Chrome(executable_path=str(os.environ.get('CHROME_EXECUTABLE_PATH')),chrome_options=options)

def again(ctx, url):
    global number
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    if number:
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        if not vc.is_playing():
            vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after=lambda e: again(ctx, url))

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('음악 연구'))

@bot.command()
async def join(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("채널에 유저가 접속에있지 않네요..")

@bot.command()
async def leave(ctx):
    try:
        await vc.disconnect()
    except:
        await ctx.send("이미 그 채널에 속해있지 않아요.")

@bot.command()
async def command(ctx):
    await ctx.send(embed = discord.Embed(title='도움말', description="""
\n!command :
You can view all commands.
\n!join :
Make dkrbot join your current voice channel.
\n!leave :
Make dkrbot leave the current voice channel.
\n!play :
Play music from the given URL,Search for a track on YouTube.
\n!stop :
Stop the player and clear the playlist. Reserved for moderators.
!skip :
Remove the currently playing track from the queue.
!pause :
Display the queue of the current tracks in the playlist.
!resume :
Resumes paused.
\n!song :
Display the currently playing track.
\n!loop :
Toggles looping for the current playing song.
\n!queue :
Shows the first page of the queue.
!clear :
Clears the whole queue.
\n!add :
Add song to queue.
!remove :
Removes a certain entry from the queue.""", color=0x00ff00))

# @bot.command()
# async def uplay(ctx, *, url):
#     YDL_OPTIONS = {'format':'bestaudio','noplaylist':'True'}
#     FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}

#     if not vc.is_playing():
#         with YoutubeDL(YDL_OPTIONS) as ydl:
#             info = ydl.extract_info(url, download=False)
#         URL = info['formats'][0]['url']
#         vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
#         await ctx.send(embed = discord.Embed(title="노래 재생", description="현재" + url + "을(를) 재생하고 있습니다.", color=0x00ff00))
#     else:
#         await ctx.send("노래가 이미 재생되고 있습니다!")

@bot.command()
async def play(ctx, *, msg):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("채널에 유저가 접속에있지 않네요..")

    if not vc.is_playing():

        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        global entireText
        YDL_OPTIONS = {'format':'bestaudio','noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}

        chromedriver_dir = "G:\Microsoft VS Code\discordbot\chromedriver.exe"
        driver = webdriver.Chrome(chromedriver_dir, options= options)
        driver.get("http://www.youtube.com/results?search_query=" + msg)
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com' + musicurl

        driver.quit()

        musicnow.insert(0, entireText)

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title="노래 재생", description="현재 " + musicnow[0] + "을(를) 재생하고 있습니다.", color=0x00ff00))
        vc.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after = lambda e:play_next(ctx))
    elif not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title="노래 재생", description="현재 " + musicnow[0] + "을(를) 재생하고 있습니다.", color=0x00ff00))
        vc.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after = lambda e:play_next(ctx))
    else:
        user.append(msg)
        result, URLTEST = title(msg)
        song_queue.append(URLTEST)
        await ctx.send(embed = discord.Embed(title="노래추가", description= result + "를 재생목록에 추가 했습니다.", color=0x00ff00))
        vc.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), after = lambda e:play_next(ctx))

@bot.command()
async def pause(ctx):
    if vc.is_playing():
        vc.pause()
        await ctx.send(embed = discord.Embed(title="일시정지", description= musicnow[0] + "을(를) 일시정지 했습니다.", color=0x00ff00))
    else:
        await ctx.send("지금 노래가 재생되지 않네요.")

@bot.command()
async def resume(ctx):
    try:
        vc.resume()
    except:
        await ctx.send("지금 노래가 재생되지 않네요.")

@bot.command()
async def stop(ctx):
    if vc.is_playing():
        vc.stop()
        global number
        number = 0
        await ctx.send(embed = discord.Embed(title="노래끄기", description= musicnow[0] + "을(를) 종료했습니다.", color=0x00ff00))
    else:
        await ctx.send("지금 노래가 재생되지 않네요.")

@bot.command()
async def skip(ctx):
    if len(user) >= 0:
        if vc.is_playing():
            vc.stop()
            global number
            number = 0
            await ctx.send(embed = discord.Embed(title="스킵", description= musicnow[0] + "을(를) 스킵합니다.", color=0x00ff00))
        else:
            await ctx.send("스킵할 노래가 없습니다.")
    else:
        await ctx.send("목록에 노래가 없습니다.")

@bot.command()
async def song(ctx):
    if not vc.is_playing():
        await ctx.send("지금 노래가 재생되지 않네요..")
    else:
        await ctx.send(embed = discord.Embed(title ="지금노래", description ="현재 " + musicnow[0] + "을(를) 재생하고 있습니다.", color=0x00ff00))

@bot.command()
async def loop(ctx, *, msg):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
    except:
        try:
            await vc.move_to(ctx.message.voice.channel)
        except:
            pass

    global entireText
    global number
    number = 1
    YDL_OPTIONS = {'format':'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options':'-vn'}
    
    if len(musicnow) - len(user) >= 1:
        for i in range(len(musicnow) - len(user)):
            del musicnow[0]

    driver = load_chrome_driver()
    driver.get("https://youtube.com/results?search_query=" + msg)
    source = driver.page_source
    bs = bs4.BeautifulSoup(source, 'lxml')
    entire = bs.find_all('a', {'id':'video-title'})
    entireNum = entire[0]
    entireText = entireNum.text.strip()
    musicnow.insert(0, entireText)
    test1 = entireNum.get('href')
    url = 'https://youtube.com' + test1
    await ctx.send(embed = discord.Embed(title="반복재생", description="현재 " + musicnow[0] + "을(를) 반복재생하고 있습니다.", color=0x00ff00))
    again(ctx, url)

@bot.command()
async def add(ctx, *, msg):
    user.append(msg)
    result, URLTEST = title(msg)
    song_queue.append(URLTEST)
    await ctx.send(result + "를 재생목록에 추가 했습니다.")

@bot.command()
async def remove(ctx, *, number):
    try:
        ex = len(musicnow) - len(user)
        del user[int(number) - 1]
        del musictitle[int(number) - 1]
        del song_queue[int(number) - 1]
        del musicnow[int(number) - 1 + ex]

        await ctx.send("대기열이 정상적으로 삭제 되었습니다.")
    except:
        if len(list) == 0:
            await ctx.send("대기열에 노래가 없어 삭제할 수 없습니다.")
        else:
            if len(list) < int(number):
                await ctx.send("숫자의 범위가 목록개수를 벗어났습니다.")
            else:
                await ctx.send("숫자를 입력해주세요.")
    
@bot.command()
async def queue(ctx):
    if len(musictitle) == 0:
        await ctx.send("아직 아무 노래도 등록되지 않았습니다.")
    else:
        global Text
        Text = ""
        for i in range(len(musictitle)):
            Text = Text + "\n" + str(i + 1) + ". " + str(musictitle[i])

        await ctx.send(embed = discord.Embed(title = "노래 목록", description = Text.strip(), color=0x00ff00))

@bot.command()
async def clear(ctx):
    try:
        ex = len(musicnow) - len(user)
        del user[:]
        del musictitle[:]
        del song_queue[:]
        while True:
            try:
                del musicnow[ex]
            except:
                break
        await ctx.send(embed = discord.Embed(title="목록 초기화", description="목록이 정상적으로 초기화 되었습니다.", color=0x00ff00))
    except:
        await ctx.send("아직 아무노래도 등록하지 않았습니다.")
        
bot.run('ODMyNjM4ODAzMTA0NzU5ODM5.YHmtUA._TtEAojLoVcEYP0az21W-N5bcBA')