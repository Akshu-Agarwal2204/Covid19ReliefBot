import os
import json
from discord import Intents, Activity, ActivityType
from discord.ext import commands
from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler

INTENTS = Intents.default()
COGS = list()

for files in os.listdir('./bot/cogs'):
    if files.endswith('.py'):
        COGS.append(files)
        print(f"Added {files} to the List...")

with open("./bot/data/credentials.json", "r", encoding="utf-8") as f:
    data = json.load(f)

TOKEN = data['token']
PREFIX = data['prefix']

class Bot(BotBase):
    def __init__(self):
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(
            command_prefix=PREFIX,
            intents=INTENTS,
            case_insensitive=True,
            strip_after_prefix=True,
            activity=Activity(type=ActivityType.listening, name=f"Use {PREFIX}search to Search for COVID 19 Relief Facilities")
        )

    def setup(self):
        for fileName in COGS:
            self.load_extension(f"bot.cogs.{fileName[:-3]}")
            print(f"Loaded {fileName} Successfully!")

        print("All Cogs are Successfully Loaded!")

    def run(self, version):
        self.version = version

        print("Starting the Setup....")
        self.setup()

        print("Running Bot...")
        super().run(TOKEN, reconnect=True)

    async def on_connect(self):
        print("Bot Connected!")

    async def on_disconnect(self):
        print("Bot Disconnected!")

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, commands.CommandNotFound):
            pass
        elif hasattr(exc, "original"):
            raise exc.original
        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.scheduler.start()
            print("Bot is now Ready!")

        else:
            print("Bot has Reconnected!")

    async def process_commands(self, message):
        ctx = await self.get_context(message, cls=commands.Context)

        if ctx.command is not None:
            if self.ready:
                await self.invoke(ctx)
            else:
                await ctx.send("Bot is Currently Starting Up! Please wait for a few Seconds...")

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)


client = Bot()