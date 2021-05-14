import discord
import asyncio
import random

client = discord.Client()

token = "ODMzOTUzNTI1NTA3MDMxMDcy.YH51vg.kgS72mkoN4AL7SF5Wn8GJ--_fTw"

@client.event
async def on_ready():

    print(client.user.name)
    print('봇 시작됨')
    game = discord.Game('Lv.1')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "안녕":
        await message.channel.send("안녕하세요")

    if message.content == "!임베드":
        em = discord.Embed(title="임베드 이미지", description="[아이콘](https://media.istockphoto.com/vectors/initial-dk-letter-logo-design-vector-with-gold-and-silver-color-dk-vector-id1207787013?k=6&m=1207787013&s=170667a&w=0&h=nusI0MvxSSIIbr2Yf-qDz5IbxdDk0uRbpNCwnZ9pj8M=)", color=0x00ff00)
        em.set_thumbnail(url=message.author.avatar_url)
        em.set_footer(text="아이콘", icon_url="https://media.istockphoto.com/vectors/initial-dk-letter-logo-design-vector-with-gold-and-silver-color-dk-vector-id1207787013?k=6&m=1207787013&s=170667a&w=0&h=nusI0MvxSSIIbr2Yf-qDz5IbxdDk0uRbpNCwnZ9pj8M=")
        await message.channel.send(embed=em)

    if message.content == "!밥":
        ran = random.randint(0,2)
        if ran == 0:
            d = "굶어"
        if ran == 1:
            d = "라면"
        if ran == 2:
            d = "김치찌개"
        await message.channel.send(d)

client.run(token)