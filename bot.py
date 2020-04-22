import discord
import random
import asyncio
from itertools import cycle
import datetime
from datetime import timezone, tzinfo, timedelta
from discord.ext import commands


#Massi's Id number
async def is_owner(ctx):
    return ctx.author.id == 261032113770463232

#Steven Id number
async def is_steven(ctx):
    return ctx.author.id == 474824764066627585

#the default status for the bot
statusreset = "Fucking Coding Bois"

#the prefix for the bot
client = commands.Bot(command_prefix = '.')
client.remove_command('help')

#runs on the commencement of the bot
@client.event
async def on_ready():
    AdminChat =  "admin"
    games = discord.Game(statusreset)
    await client.change_presence(activity=games)
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='Mid Ground')
    print(f'{member} has joined Steven the Cranker')
    await member.add_roles(role)

@client.event
async def on_member_remove(member):
    print(f'{member} is a dickhead')

#Ping Command
@client.command()
async def ping(ctx):
    
    embed = discord.Embed(
    colour = discord.Colour.light_grey()
    )
    pingms = round(client.latency*100)
    embed.add_field(name="Pong!", value=f"{round(client.latency*100)}ms :ping_pong:", inline=False)
    await ctx.send(embed=embed)
    print ("Ping command used")

#8 Ball Command
@client.command(aliases=['8ball', 'test'])
async def ball8(ctx, *, question):
    if question == "is steven bi?":
        response = ['Yes',
                     'Most certainly',
                     'Of course',
                     'Certainly',
                     'Fuck yes',
                     'Why wouldnt he be?']
        channel= ctx.message.channel
        embed = discord.Embed(
        title = '8 Ball',
        colour = discord.Colour.light_grey()
        )
        embed.add_field(name='Question:', value=question, inline=False)
        embed.add_field(name='Answer:', value=random.choice(response), inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/700303754099949668/701664183103520778/1200px-8-Ball_Pool.png')
        await ctx.send(embed=embed)
        print ("8 Ball command used")
    else:
        responses = ['it is certain.',
                 'it will happen',
                 'it might happen',
                 'without a doubt',
                 'yes',
                 'most likely',
                 'my reply is no',
                 'my sources say no',
                 'very doubtful',
                 'cannot decide right now']
        channel= ctx.message.channel
        embed = discord.Embed(
        title = '8 Ball',
        colour = discord.Colour.light_grey()
        )
        embed.add_field(name='Question:', value=question, inline=False)
        embed.add_field(name='Answer:', value=random.choice(responses), inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/700303754099949668/701664183103520778/1200px-8-Ball_Pool.png')
        await ctx.send(embed=embed)
        print ("8 Ball command used")
        

#Clear Command
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)
    await asyncio.sleep(1)
    embed = discord.Embed(
    title = 'Message Clearing',
    colour = discord.Colour.light_grey()
    )
    embed.add_field(name='The Billion Bot just cleared:', value=f'{amount} messages', inline=False)
    await ctx.send(embed=embed)
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)

#Embed Command
@client.command()
async def embed(ctx, *, msg):
    channel= ctx.message.channel
    embed = discord.Embed(
        title = msg,
        colour = discord.Colour.light_grey()
        )
    await ctx.send(embed=embed)
    print ("Embed command used")

#Status Change Command
@client.command()
@commands.check(is_owner)
async def status(ctx, *, game):
    if game == "reset":
        games = discord.Game(statusreset)
        await client.change_presence(activity=games)
        print ("Bot Status changed to " + statusreset)
        embed = discord.Embed(
        title = 'Status Rest',
        colour = discord.Colour.light_grey()
        )
        embed.add_field(name='Status was reset to:', value=statusreset, inline=False)
        await ctx.send(embed=embed)
    else:
        games = discord.Game(game)
        await client.change_presence(activity=games)
        print ("Bot Status changed to " + game)
        channel= ctx.message.channel
        embed = discord.Embed(
        title = 'Status Change',
        colour = discord.Colour.light_grey()
        )
        embed.add_field(name='Status was changed to:', value=game, inline=False)
        await ctx.send(embed=embed)

#Shutdown Command
@client.command(pass_context=True)
@commands.check(is_owner)
async def shutdown(ctx, amount=1):
        if str(ctx.message.channel.id) =="701690855202881557":
            await ctx.channel.purge(limit=amount)
            await ctx.send("**Starting Shutdown Sequence**")
            print("Shutting Down")
            await asyncio.sleep(1)
            await ctx.channel.purge(limit=amount)
            await ctx.send("**5**")
            await asyncio.sleep(1)
            await ctx.channel.purge(limit=amount)
            await ctx.send("**4**")
            await asyncio.sleep(1)
            await ctx.channel.purge(limit=amount)
            await ctx.send("**3**")
            await asyncio.sleep(1)
            await ctx.channel.purge(limit=amount)
            await ctx.send("**2**")
            await asyncio.sleep(1)
            await ctx.channel.purge(limit=amount)
            await ctx.send("**1**")
            await asyncio.sleep(1)
            await ctx.channel.purge(limit=amount)
            await ctx.send("**Shutting Down**")
            await asyncio.sleep(5)
            await ctx.channel.purge(limit=amount)
            t = datetime.datetime.now()
            embed = discord.Embed(
            title = 'Shutdown',
            colour = discord.Colour.light_grey()
            )
            day = (t.strftime('**%A %d %B %Y**'))
            time = (t.strftime('%I hr %M min %S secs %p'))
            embed.add_field(name=day, value=time, inline=False)
            await ctx.send(embed=embed)
            await client.close()
        else:
            await ctx.channel.purge(limit=amount)
            embed = discord.Embed(
            title = 'Shutdown Failiure',
            colour = discord.Colour.light_grey()
            )
            embed.add_field(name="Wrong Text Chat", value="In order to shutdown the bot, you need to be in the Admin chat", inline=False)
            print("Someone attempted to shutdown the Bot in the wrong chat")
            await ctx.send(embed=embed)


#Time Command
@client.command()
async def time(ctx):
    channel= ctx.message.channel
    embed = discord.Embed(
    title = 'Current Time',
    colour = discord.Colour.light_grey()
    )
    t = datetime.datetime.now()
    days = (t.strftime('**%A %d %B %Y**'))
    times = (t.strftime('%I hr %M min %S secs %p'))
    embed.add_field(name=days, value=times, inline=False)
    await ctx.send(embed=embed)


#Profile Command
@client.command()
async def profile(ctx, member : discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="Identification:", value=member.id, inline=False)
    embed.add_field(name="Discord Name", value = member.display_name, inline=False)
    embed.add_field(name=f"roles ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)
    await ctx.send(embed=embed)

#Help Command
@client.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.light_grey(),
        title = "Help Command"
        )
    embed.add_field(name = "**Ping**", value="Sends back a Ping Pong paddle and your latency", inline = False)
    embed.add_field(name = "**Time**", value="Sends the current time, date and year", inline = False)
    embed.add_field(name = "**Ball8**", value="Answers any quesion with the Truth and only the truth", inline = False)
    embed.add_field(name = "**Embed**", value="Embeds the message that you state after the command", inline = False)
    embed.add_field(name = "**Profile**", value="Shows information about the mentioned user", inline = False)
    await ctx.send(embed=embed)
    print("Help command used")

#Admin Help Command
@client.command()
@commands.has_role("Admin") 
async def admin(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.light_grey(),
        title = "Help Command"
        )
    embed.add_field(name = "**Clear**", value="Clears the amount of messages that is states after the command", inline = False)
    embed.add_field(name = "**Status**", value="Chnages what the bot is 'playing' under the bots name", inline = False)
    embed.add_field(name = "**Ban**", value="Bans a user from the server", inline = False)
    embed.add_field(name = "**Shutdown**", value="Gives a countdown to the shutting down of the bot", inline = False)
    await ctx.send(embed=embed)
    print("Admin Help command used")

#Kick Command
@client.command()
async def kick(ctx, member: discord.Member = None, *, reason="No Reason"):
    await member.kick(reason=reason)
    embed = discord.Embed(
    title = 'Kicked User',
    colour = discord.Colour.light_grey()
    )
    embed.add_field(name=(f"{member} was kicked for:"), value=reason, inline=False)
    await ctx.send(embed=embed)
    print (f"{member} was kicked for {reason}")

#Ban Command
@client.command()
async def ban(ctx, member: discord.Member = None, *, reason="No Reason"):
    await member.ban(reason=reason)
    embed = discord.Embed(
    title = 'Banned User',
    colour = discord.Colour.light_grey()
    )
    embed.add_field(name=(f"{member} was banned for:"), value=reason, inline=False)
    await ctx.send(embed=embed)
    print (f"{member} was banned for {reason}")

#Dice command
@client.command()
async def dice(ctx):
    dice = ['4','6','1','2','5','3','1','5','3','2','4','6','2','1','6','3','4','6','1','2']
    diceroll = random.choice(dice)
    print(f"Dice command used and rolled a {diceroll}")
    if diceroll == '1':
        embed = discord.Embed(
        title = 'Dice Roll',
        colour = discord.Colour.light_grey()
        )
        embed.add_field(name=("The dice rolled"), value=("**1**"), inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/700589461829845072/702326962768576592/unknown.png')
        await ctx.send(embed=embed)
    if diceroll == '2':
        embed = discord.Embed(
        title = 'Dice Roll',
        colour = discord.Colour.light_grey()
        )
        embed.add_field(name=("The dice rolled"), value=("**2**"), inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/700589461829845072/702327030406053939/unknown.png')
        await ctx.send(embed=embed)
    if diceroll == '3':
        embed = discord.Embed(
        title = 'Dice Roll',
        colour = discord.Colour.light_grey()
        )
        embed.add_field(name=("The dice rolled"), value=("**3**"), inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/700589461829845072/702327091479314552/unknown.png')
        await ctx.send(embed=embed)
    if diceroll == '4':
        embed = discord.Embed(
        title = 'Dice Roll',
        colour = discord.Colour.light_grey()
        )
        embed.add_field(name=("The dice rolled"), value=("**4**"), inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/700589461829845072/702327165768826981/unknown.png')
        await ctx.send(embed=embed)
    if diceroll == '5':
        embed = discord.Embed(
        title = 'Dice Roll',
        colour = discord.Colour.light_grey()
        )
        embed.add_field(name=("The dice rolled"), value=("**5**"), inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/700589461829845072/702327202586296340/unknown.png')
        await ctx.send(embed=embed)
    if diceroll == '6':
        embed = discord.Embed(
        title = 'Dice Roll',
        colour = discord.Colour.light_grey()
        )
        embed.add_field(name=("The dice rolled"), value=("**6**"), inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/700589461829845072/702327248144957440/unknown.png')
        await ctx.send(embed=embed)

#Rock Paper Scissors
@client.command()
async def rps(ctx, selection="None"):
    if selection == "None":
        embed = discord.Embed(
        title = "Rock Paper Scissors",
        colour = discord.Colour.light_grey()
        )
        embed.add_field(name="Failed Attempt at Rock Paper Scissors", value="In order to play Rock Paper Scissors, you need to decide what you select")
        await ctx.send(embed=embed)

    else:
        rpsdecision = ['paper','rock','scissors','paper', 'scissors','paper', 'rock','rock','scissors','rock','scissors']
        rps = random.choice(rpsdecision)
        if selection == 'rock':
            if str(ctx.message.author.id) =="474824764066627585":
                embed = discord.Embed(
                title = "Rock Paper Scissors",
                colour = discord.Colour.light_grey()
                )
                embed.add_field(name="You Selected **Rock** <:3217_rock:702334613682389002>", value="I Choose **Paper** 📰")
                embed.add_field(name="I **Win**",value="🤣", inline=False)
                await ctx.send(embed=embed)
                print("Steven played Rock Paper Scissors and Lost to Billion Bot by deafault")
            else:
                if rps == 'rock':
                    embed = discord.Embed(
                    title = "Rock Paper Scissors",
                    colour = discord.Colour.light_grey()
                    )
                    embed.add_field(name="You Selected **Rock** <:3217_rock:702334613682389002>", value="I Choose **Rock** <:3217_rock:702334613682389002>")
                    embed.add_field(name="Its a **Draw**",value="<:2826_the_bird:702335336453242972>", inline=False)
                    await ctx.send(embed=embed)
                    print("Rock Paper Scissors command was used and Billion Bot Drew")
                if rps == 'paper':
                    embed = discord.Embed(
                    title = "Rock Paper Scissors",
                    colour = discord.Colour.light_grey()
                    )
                    embed.add_field(name="You Selected **Rock** <:3217_rock:702334613682389002>", value="I Choose **Paper** 📰")
                    embed.add_field(name="I **Win**",value="🤣", inline=False)
                    await ctx.send(embed=embed)
                    print("Rock Paper Scissors command was used and Billion Bot Won")
                if rps == 'scissors':
                    embed = discord.Embed(
                    title = "Rock Paper Scissors",
                    colour = discord.Colour.light_grey()
                    )
                    embed.add_field(name="You Selected **Rock** <:3217_rock:702334613682389002>", value="I Choose **Scissors** ✂️")
                    embed.add_field(name="I **Lose**",value="😠", inline=False)
                    await ctx.send(embed=embed)
                    print("Rock Paper Scissors command was used and Billion Bot Lost")
            
        if selection == 'paper':
            if str(ctx.message.author.id) =="474824764066627585":
                embed = discord.Embed(
                title = "Rock Paper Scissors",
                colour = discord.Colour.light_grey()
                )
                embed.add_field(name="You Selected **Paper** 📰", value="I Choose **Scissors** ✂️")
                embed.add_field(name="I **Win**",value="🤣", inline=False)
                await ctx.send(embed=embed)
                print("Steven played Rock Paper Scissors and Lost to Billion Bot by deafault")
            else:
                if rps == 'rock':
                    embed = discord.Embed(
                    title = "Rock Paper Scissors",
                    colour = discord.Colour.light_grey()
                    )
                    embed.add_field(name="You Selected **Paper** 📰", value="I Choose **Rock** <:3217_rock:702334613682389002>")
                    embed.add_field(name="I **Lost**",value="😠", inline=False)
                    await ctx.send(embed=embed)
                    print("Rock Paper Scissors command was used and Billion Bot Lost")
                if rps == 'paper':
                    embed = discord.Embed(
                    title = "Rock Paper Scissors",
                    colour = discord.Colour.light_grey()
                    )
                    embed.add_field(name="You Selected **Paper** 📰", value="I Choose **Paper** 📰")
                    embed.add_field(name="Its a **Draw**",value="<:2826_the_bird:702335336453242972>", inline=False)
                    await ctx.send(embed=embed)
                    print("Rock Paper Scissors command was used and Billion Bot Drew")
                if rps == 'scissors':
                    embed = discord.Embed(
                    title = "Rock Paper Scissors",
                    colour = discord.Colour.light_grey()
                    )
                    embed.add_field(name="You Selected **Paper** 📰", value="I Choose **Scissors** ✂️")
                    embed.add_field(name="I **Win**",value="🤣", inline=False)
                    await ctx.send(embed=embed)
                    print("Rock Paper Scissors command was used and Billion Bot Won")
        if selection == 'scissors':
            if str(ctx.message.author.id) =="474824764066627585":
                embed = discord.Embed(
                title = "Rock Paper Scissors",
                colour = discord.Colour.light_grey()
                )
                embed.add_field(name="You Selected **Scissors** 📰", value="I Choose **Rock** <:3217_rock:702334613682389002>")
                embed.add_field(name="I **Win**",value="🤣", inline=False)
                await ctx.send(embed=embed)
                print("Steven played Rock Paper Scissors and Lost to Billion Bot by deafault")
            else:
                if rps == 'rock':
                    embed = discord.Embed(
                    title = "Rock Paper Scissors",
                    colour = discord.Colour.light_grey()
                    )
                    embed.add_field(name="You Selected **Scissors** ✂️", value="I Choose **Rock** <:3217_rock:702334613682389002>")
                    embed.add_field(name="I **Won**",value="🤣", inline=False)
                    await ctx.send(embed=embed)
                    print("Rock Paper Scissors command was used and Billion Bot Won")
                if rps == 'paper':
                    embed = discord.Embed(
                    title = "Rock Paper Scissors",
                    colour = discord.Colour.light_grey()
                    )
                    embed.add_field(name="You Selected **scissors** ✂️", value="I Choose **Paper** 📰")
                    embed.add_field(name="I **Lost**",value="😠", inline=False)
                    await ctx.send(embed=embed)
                    print("Rock Paper Scissors command was used and Billion Bot Lost")
                if rps == 'scissors':
                    embed = discord.Embed(
                    title = "Rock Paper Scissors",
                    colour = discord.Colour.light_grey()
                    )
                    embed.add_field(name="You Selected **scissors** ✂️", value="I Choose **Scissors** ✂️")
                    embed.add_field(name="Its a **Draw**",value="<:2826_the_bird:702335336453242972>", inline=False)
                    await ctx.send(embed=embed)
                    print("Rock Paper Scissors command was used and Billion Bot Drew")

#Youtube Command
@client.command()
async def yt(ctx):
    embed = discord.Embed(
    title = "Link to Main Channel",
    url='https://www.youtube.com/channel/UCnBuJGQ1hfhdYrXSQbOe_iQ/', 
    colour = discord.Colour.light_grey()
    )
    embed.add_field(name ="Main Meme Channel" ,value="XXXMeme SquadXXX"),
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/700303754099949668/702403531382194216/2Q.png')
    await ctx.send(embed=embed)

client.run('NTg1MDE1NzIxNTM3NTY4NzY4.Xp0cnw.bo8OAnyosnqKgRFlah95NGE_Hqw')
