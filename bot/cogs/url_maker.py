from discord.ext import commands
from asyncio.exceptions import TimeoutError

class URLMaker(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="search", aliases=['reliefsearch', 'covidsearch', 'coronarelief'])
    async def search(self, ctx):
        try:
            msg = await ctx.reply("In what Location you want to Search for the Relief Facilities? Type the name of the city/state...\nExample: `mumbai`, `jaipur`")
            inp = await self.client.wait_for('message', timeout=120,
                                             check=lambda message: message.author == ctx.author)
            LOCATION_STR = inp.content
            await inp.delete()

            await msg.edit(content="Type the name of the Relief Facilities Required... (separated by a comma for multiple requirements)\nExample: `bed, oxygen, icu, ventilator, remdesivir, plasma`")
            inp = await self.client.wait_for('message', timeout=120,
                                             check=lambda message: message.author == ctx.author)
            REQUIREMENTS_STR = inp.content
            await inp.delete()

            await msg.edit(content="Exclude the Words which should not come in Search (separated by a comma for multiple words). Type `none` to Skip...\nFor omitting Unverified Results (search should not contain unverified results), copy and type `unverified,not verified,non verified`\nExample: `needed`, `required`, `request`, `not verified,needed,unverified`")
            inp = await self.client.wait_for('message', timeout=120,
                                             check=lambda message: message.author == ctx.author)
            OMITTED_WORDS_STR = inp.content
            await inp.delete()

            await msg.edit(
                content="Include the Words which should come in Search (separated by a comma for multiple words). Type `none` to Skip...\nFor getting only Verified Results (search should contain verified results), copy and type `verified`\nExample: `needed`, `required`, `verified`")
            inp = await self.client.wait_for('message', timeout=120,
                                             check=lambda message: message.author == ctx.author)
            INCLUDED_WORDS_STR = inp.content
            await inp.delete()

            LOCATION = LOCATION_STR

            REQUIREMENTS_LIST = (str(REQUIREMENTS_STR).replace(" ", "")).split(',')
            REQUIREMENTS = "+OR+".join(x for x in REQUIREMENTS_LIST)

            if str(OMITTED_WORDS_STR).lower() == 'none':
                OMITTED_WORDS_LIST = None
            else:
                OMITTED_WORDS_LIST = str(OMITTED_WORDS_STR).split(',')

            if str(INCLUDED_WORDS_STR).lower() == 'none':
                INCLUDED_WORDS_LIST = None
            else:
                INCLUDED_WORDS_LIST = str(INCLUDED_WORDS_STR).split(',')

            if OMITTED_WORDS_LIST is not None:
                OMITTED_WORDS_TEMP_LIST = list()
                for WORD in OMITTED_WORDS_LIST:
                    WORD = WORD.replace(" ", "+")
                    WORD = f"-%22{WORD}%22"
                    OMITTED_WORDS_TEMP_LIST.append(WORD)
                OMITTED_WORDS_INI = '+'.join(x for x in OMITTED_WORDS_TEMP_LIST)
                OMITTED_WORDS = f"+{OMITTED_WORDS_INI}"
            else:
                OMITTED_WORDS = ""

            if INCLUDED_WORDS_LIST is not None:
                INCLUDED_WORDS_TEMP_LIST = list()
                for WORD in INCLUDED_WORDS_LIST:
                    WORD = WORD.replace(" ", "+")
                    INCLUDED_WORDS_TEMP_LIST.append(WORD)
                INCLUDED_WORDS = f"{'+'.join(x for x in INCLUDED_WORDS_TEMP_LIST)}+"
            else:
                INCLUDED_WORDS = ""

            TWITTER_URL_HEAD = f"https://www.twitter.com/search?q={LOCATION}+{INCLUDED_WORDS}%28{REQUIREMENTS}%29{OMITTED_WORDS}&f=live"

            message = f"""Here's the URL: <{TWITTER_URL_HEAD}>
This may also Help you (may not work after some Time): http://bit.ly/All_India_COVID19_HELPLINE
            
**Tips:**
1). **Do NOT make advanced payments unless you are 100% sure about their authenticity.**
2). Check for replies under the tweets.
3). Make sure search results are sorted by `Latest`."""

            await msg.edit(content=message)

        except TimeoutError:
            await msg.edit(content="You Timed Out Responding... Please Try Again!")

def setup(client):
    client.add_cog(URLMaker(client))