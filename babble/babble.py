import discord
from discord.ext import commands
import random


class Babble:
    """Babble"""

    def __init__(self, bot):
        self.bot = bot
        self.gibberish = dict() # maps channel id to list of words

    async def on_message(self, message):
        if channelid not in self.gibberish:
            return
        words = message.clean_content.split()
        gibberish = self.gibberish[channelid]
        if len(words) < 4:
            # take this opportunity to speak
            if len(gibberish) >= random.randInt(5, 9):
                await self.bot.say(" ".join(gibberish))
                gibberish = []
            return
        word = words[random.randint(0, len(words) - 1)]
        if len(word) > 12:
            return
        gibberish.append(word)

    @commands.command(pass_context=True, no_pm=True)
    async def babble(self, ctx):
        """Toggle babble for this channel"""
        channelid = ctx.message.channel.id
        if channelid in self.gibberish:
            del self.gibberish[channelid]
            await self.bot.say("Stopped babbling.")
        else:
            self.gibberish[channelid] = [] # start with empty list
            await self.bot.say("Started babbling.")


def setup(bot):
    b = Babble(bot)
    bot.add_listener(b.on_message, "on_message")
    bot.add_cog(b)

