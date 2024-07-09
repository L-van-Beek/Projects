# first, we need to install the library (in terminal: python3 -m pip install -U discord.py)
# then, creating a connection to Discord by creating an instance of Client - object that represents a connection to Discord. 
# A client handles events, tracks state, interacts with Discord APIs. 
import discord
import random 
from random import choice 
import json 
import requests

TOKEN = ('hidden for privacy reasons') 
GUILD = ('same here') 

intents = discord.Intents.default()
intents.message_content = True   

def get_meme():
    answer = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(answer.text)
    return json_data['https://meme-api.com/gimme']

brooklyn_99_quotes = ['I am the human form of the 💯 emoji.', 'Bingpot!', 'Cool. Cool cool cool cool cool cool cool' , 'no doubt no doubt no doubt no doubt.']

class MyClient(discord.Client):
    async def on_read(self):
        print(f'Logged on as {self.user}, (•◡•) /')
        
    async def on_message(self, message):
        if message.author == client.user:  # this line of code makes sure bot is not interacting with itself 
            return
        
        if message.content == '99!':
            response = random.choice(brooklyn_99_quotes, 1)
            await message.channel.send(response)
            
        if 'happy birthday' in message.content.lower():
            await message.channel.send('Happy Birthday! 🎈🎉')

        if message.author == self.user:
            return
             
        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
        elif message.content == 'raise-exception':
            raise discord.DiscordException
    
    async def on_error(event, *args, **kwargs):
        with open('err.log', 'a') as f:
            if event == 'on_message':
                f.write(f'Unhandled message: {args[0]}\n')
            else:
                raise

client = MyClient(intents=intents)
client.run('hidden') # client.run runs my Client using the bot's token
