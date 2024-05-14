import sys
from selenium import webdriver
import selenium      
from selenium.webdriver.chrome.options import Options
chrome_options = Options()


from dotenv import load_dotenv
load_dotenv()
import os
ws_username = os.getenv("ws_username")
ws_password = os.getenv("ws_password")
qbt_username = os.getenv("qbt_username")
qbt_password = os.getenv("qbt_password")
qbt_host = os.getenv("qbt_host")
qbt_port = os.getenv("qbt_port")
bot_token = os.getenv("bot_token")
discord_userid = os.getenv("discord_userid")
aquiredPort = 0

# For using sleep function because selenium  
# works only when the all the elements of the  
# page is loaded. 
import time  

import qbittorrentapi

import discord
intents = discord.Intents.default()
intents.message_content = True

discordclient = discord.Client(intents=intents)

@discordclient.event
async def on_ready():
    print(f'We have logged in as {discordclient.user}')
    user = await discordclient.fetch_user(discord_userid)

    # Send the acquired port value as a DM
    await user.send("New Port: " + str(aquiredPort))
    sys.exit()


#Required for running chromedriver headless
chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless") #Disable to view chrome
print("Running Chrome Headless")
from selenium.webdriver.common.keys import Keys  
  
# Creating an instance webdriver 
browser = webdriver.Chrome(options=chrome_options)  
browser.get('https://www.windscribe.com/login') 
time.sleep(2) 
  
print("Login to Windscribe") 
  
user = browser.find_element("xpath", '//*[@id="username"]') 
  
user.send_keys(ws_username) 
  
passw = browser.find_element("xpath", '//*[@id="pass"]') 
  
passw.send_keys(ws_password)
passw.submit()

print("Login Successful") 

time.sleep(5) 
browser.get('https://windscribe.com')
time.sleep(5)
browser.get('https://windscribe.com/myaccount#porteph')
print("Load Request Ephemeral Port Page")
time.sleep(5)

print("")
delPort = browser.find_element("xpath", '//*[@id="request-port-cont"]/button')
delPort.click()
print("Delete Port")
time.sleep(5)

reqMatchPort = browser.find_element("xpath", '//*[@id="request-port-cont"]/button[2]')
reqMatchPort.click()
print("Request New Port")
time.sleep(5)

port = browser.find_element("xpath", '//div[@id="epf-port-info"]//span[1]')

        
print("New Port: " + port.text)
aquiredPort = port.text
  
# closing the browser 
browser.close()

# instantiate a Client using the appropriate WebUI configuration
client = qbittorrentapi.Client(host=qbt_host, port=qbt_port, username=qbt_username, password=qbt_password)
# the Client will automatically acquire/maintain a logged in state in line with any request.
# therefore, this is not necessary; however, you many want to test the provided login credentials.
try:
    client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
    print(e)

# display qBittorrent info
# print(f'qBittorrent: {client.app.version}')
# print(f'qBittorrent Web API: {client.app.web_api_version}')

#Set qBittorrent listening port
prefs = client.application.preferences
prefs['listen_port'] = aquiredPort
client.app.preferences = prefs
print("Set qBittorrent listening port to " + aquiredPort)

#Send update to discord
if (discord_userid != ""):
    discordclient.run(bot_token)
else:
    sys.exit()