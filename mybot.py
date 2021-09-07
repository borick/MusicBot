import discord
from discord.ext import commands

client = discord.Client()
# 145581656793677824 == my id

general_role = 881282023069736990
general_channel = 881179327755083786


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    crypto_signals = client.get_channel(882023206075133982)  # 882023206075133982 == CryptoSignals channel
    general = client.get_channel(881179327755083786)

    print(message)

    if isinstance(message.channel, discord.DMChannel):
        print("Message received")
        if message.author.id == 199021357516849153 or message.author.id == 145581656793677824:
            await crypto_signals.send(message.content)

    if message.type == discord.MessageType.new_member:
        print("New member joined")
        var = discord.utils.get(message.guild.roles, id=general_role)
        member = message.author
        await member.add_roles(var)
        import time
        time.sleep(2)
        await general.send("Hey <@{}>, welcome to Here and Now! Thanks for joining!!!".format(message.author.id))


client.run('ODgyNjQ5NjgyNDM2ODMzMzYw.YS-dkw.BD2EoZhXIKtdATC9G4o-V__Srk0')
