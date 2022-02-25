import discord
from discord.ext import commands, tasks
import random
import keep_alive
from hypixelaPY import Hypixel
import asyncio
from extras import *
import os
#among us
API_KEY = os.environ['HYPIXEL_API_KEY']
playerlist = []
intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="%", intents=intents)


async def main():
    global hypixel
    hypixel = await Hypixel(API_KEY)


@bot.command(brief="Hypixel Statistics",
             help="See some statistics about someone on the Hypixel Network")
async def hy_profile(ctx, player_name):
    try:
        player = await hypixel.player.get(name=player_name)
        network_rank = player.rank.name
        ach_points = player.achievement_points
        level = player.level.level
        login = player.logins.last
        karma = player.karma
        embed_color = rank_color(network_rank)
        #print(thing)
        #await ctx.channel.send("Player **{}** has **{}** karma".format(player_name,karma))
        embedVar = discord.Embed(title=player_name,
                                 description=" Hypixel Overall Stats",
                                 color=embed_color)
        embedVar.add_field(name="Network Rank:", value=str(network_rank))
        embedVar.add_field(name="Network Level:", value=str(level))
        embedVar.add_field(name="Achievement Points:", value=str(ach_points))
        embedVar.add_field(name="Karma:", value=str(karma))
        embedVar.add_field(name="Last Login:", value=login)
        await ctx.channel.send(embed=embedVar)
    except:
        embedVar = discord.Embed(title="Error",
                                 description="The following error occured:",
                                 color=0xff0000)
        embedVar.add_field(
            name="Player **{}** does not exist".format(player_name),
            value="Maybe check your spelling.",
            inline=False)
        await ctx.channel.send(embed=embedVar)


@bot.command(help="Get some basic bedwars stats from the Hypixel Network.",
             brief="Bedwars stats",
             aliases=["bw", "bedwar"])
async def bedwars(ctx, player_name):
    player = await hypixel.player.get(name=player_name)
    level = player.bedwars.prestige.star
    coins = player.bedwars.coins
    games = player.bedwars.games_played
    beds = player.bedwars.beds
    bedwars_embed = discord.Embed(title=player_name,
                                  description="Bedwars Stats",
                                  color=0xff0000)
    bedwars_embed.add_field(name="Level", value=str(level))
    bedwars_embed.add_field(name="Coins", value=str(coins))
    bedwars_embed.add_field(name="Games Played", value=str(games))
    bedwars_embed.add_field(name="Beds Broken", value=str(beds))
    await ctx.channel.send(embed=bedwars_embed)


@bot.command(help="See how connected two people are at this moment in time",
             brief="Love meter.")
async def lovemeter(ctx, person_1="", person_2=""):

    if person_1 != "" and person_2 != "":
        love = random.randint(5, 100)
        diceroll1 = random.randint(1, 2)
        diceroll2 = random.uniform(0.5, 1)
        love_final = round(love * diceroll1 * diceroll2, 1)
        if love_final > 100:
            love_final = 100
        if person_1 == "nathan" or person_1 == "Nathan" and person_2 == "ethan" or person_2 == "Ethan":
            love_final = 150
        elif person_2 == "nathan" or person_2 == "Nathan" and person_1 == "ethan" or person_1 == "Ethan":
            love_final = 150
        await ctx.channel.send(
            "The relationship between **{}** and **{}** is **{}** percent".
            format(person_1, person_2, love_final))
    else:
        await ctx.channel.send(
            "Two arguements are required, %lovemeter <person_1> <person_2>")
        await ctx.channel.send(e("Technoblade"))


@bot.command(help="Get some", brief="Get some")
async def get_bitches(ctx):
    chance = random.randint(-10, 100)
    if ctx.author.id == 922282746225774604:
        chance = 100 - 200
    elif ctx.author.id == 882428635502510181 or ctx.author.id == 528677495227154443:
        chance = random.randint(90, 100)
    elif ctx.author.id == 491760288064995328:
        chance = random.randint(1, 35)
    elif ctx.author.id == 549634577044340747:
        chance = random.randint(50, 100)
    elif ctx.author.id == 628610377831284736:
        chance = random.randint(70, 90)
    else:
        pass
    await ctx.channel.send(
        "{}'s'chance of getting bitches at this current moment is **{}** percent"
        .format(ctx.author, chance))


#@bot.command()
#async def test(ctx,name):
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

keep_alive.keep_alive()
bot.run(os.environ['BOT_TOKEN'])
