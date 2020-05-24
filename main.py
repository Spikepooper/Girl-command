import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'girl':
            await message.channel.send('Oh wait are you a female? Oh no sorry I wouldnt have bullied you if I had known that. Hey what do you say we meet up irl and I can get you a couple drinks at the bar?')
 

client = MyClient()
token = os.getenv("DISCORD_TOKEN")
client.run(token)