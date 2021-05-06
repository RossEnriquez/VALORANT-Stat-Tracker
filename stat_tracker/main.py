import fetch_data
from fetch_data import *
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='%')
token = null

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=' VALORANT | %help]'))
    print(f'Bot connected as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('%'):
        try:
            mode = message.content.split(' ')[0]
            input = message.content.split(' ', 1)[1]
            print(input)
            name = input.split('#')[0]
            data = fetch(input, mode)
            if data is not None:
                #make embed
                embed = discord.Embed(title=f"{name}'s stats", color=0xdc3d4b, url=fetch_data.site)
                embed.set_thumbnail(url='https://seeklogo.com/images/V/valorant-logo-FAB2CA0E55-seeklogo.com.png')
                embed.set_footer(text="via tracker.gg")

                e_name = f'K/D Ratio: {data[1][1]}'
                val = f'\nWins: {data[4][1]} | Win %: {data[3][1]}\n' \
                        f'Kills: {data[5][1]} | Deaths: {data[7][1]}\n' \
                        f'Headshots: {data[6][1]} ({data[2][1]}%)\n' \
                        f'Assists: {data[8][1]} | Flawless: {data[12][1]} | Clutches: {data[11][1]}\n\n' \
                        f'Score/R: {data[9][1]} | Kills/R: {data[10][1]} | DMG/R: {data[0][1]}\n' \
                        f'Most Kills in a Match: {data[13][1]}'

                embed.add_field(name=e_name, value=val, inline=True)
                await message.channel.send(embed=embed)
            else:
                await message.channel.send('The mode was not found!')
        except:
            await message.channel.send('The player was not found!')

client.run(token)
