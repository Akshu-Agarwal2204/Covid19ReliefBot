from discord import Embed, Color
from discord.ext import commands
from datetime import datetime
from json import load

with open('./bot/data/credentials.json') as f:
    data = load(f)
PREFIX = data['prefix']

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        client.remove_command('help')

    @commands.command(name="help")
    async def help(self, ctx):
        embed = Embed(title="Help Command",
                      description="I'm a Bot by which you can Search for Covid 19 Relief Facilities near your Location.\n\nAt the Hard Times, everyone is suffering from this Disease. It would be very helpful if you help people around you suffering from any Problems. Fight against the Invisible Enemy and Defeat it!",
                      color=Color.random(),
                      timestamp=datetime.utcnow())
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"Thanks for using {ctx.guild.me.name}", icon_url=ctx.guild.me.avatar_url)
        embed.add_field(name=f"{PREFIX}search", value="Search for the Covid 19 Relief Facilities at your Location\nAliases: `reliefsearch`, `coronarelief`, `covidsearch`")
        await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Help(client))