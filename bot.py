# Work with Python 3.6
import discord

BOT_PREFIX = "~"
TOKEN = 'NTQ4MjI2OTgxODM4MzIzNzMy.D1CR-Q.ImarYNXf_nDBFsUB-2dQqX5KndE'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
