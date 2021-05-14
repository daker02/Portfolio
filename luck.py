import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
from bs4 import BeautifulSoup

import time

# bot = commands.Bot(command_prefix='!')
bot = discord.Client()

@bot.event
async def on_ready():
    print('connection was succesful')
    print(bot.user.name)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('!오늘의운세'))

@bot.event
async def on_message(message):
    if message.content.startswith('!오늘의운세'):
        embed = discord.Embed(title="성별을 고르시오", description="남자 입니까?, 여자입니까?",color=0x00ff00)
        embed.add_field(name="남자\U0001F6B9", value="남자입니다.",inline=False)
        embed.add_field(name="여자\U0001F6BA", value="여자입니다.",inline=False)

        msg = await message.channel.send(embed = embed)
        await msg.add_reaction("\U0001F6B9")
        await msg.add_reaction("\U0001F6BA")

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot == 1: #봇이면 패스
        return None
    if str(reaction.emoji) == "\U0001F6B9":
        await reaction.message.channel.send(user.name + "님은 남자를 선택하였습니다")
        
        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')

        driver = webdriver.Chrome()
        url = 'https://www.naver.com'
        driver.get(url)
        action = ActionChains(driver)
        time.sleep(1)

        action.send_keys('오늘의운세').perform()
        driver.find_element_by_css_selector('.btn_submit').click()

        driver.execute_script('window.scrollTo(0, 900)')

        driver.find_element_by_css_selector('.srch_txt').send_keys('19970506')
        driver.find_element_by_css_selector('.img_btn').click()

        # driver.quit()

    if str(reaction.emoji) == "\U0001F6BA":
        await reaction.message.channel.send(user.name + "님은 여자를 선택하였습니다")

        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')

        driver = webdriver.Chrome()
        url = 'https://www.naver.com'
        driver.get(url)
        action = ActionChains(driver)
        time.sleep(1)

        action.send_keys('오늘의운세').perform()
        driver.find_element_by_css_selector('.btn_submit').click()

        driver.execute_script('window.scrollTo(0, 900)')

        driver.find_element_by_id(l_woman).click()

        driver.find_element_by_css_selector('.srch_txt').send_keys('19970506')
        driver.find_element_by_css_selector('.img_btn').click()

        driver.quit()

bot.run('ODM1ODE2NDM3ODU1NDIwNDY2.YIU8tw.NgIrjOrB5wqC8F44klggdjTYBJQ')