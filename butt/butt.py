import discord
from discord.ext import commands
import random


class Butt:
    """Butt"""

    def __init__(self, bot):
        self.bot = bot
        self.lastMsgInChannel = dict()

    async def on_message(self, message):
        self.lastMsgInChannel[message.channel.id] = message
        #await self.bot.process_commands(message)

    @commands.command(pass_context=True)
    async def butt(self, ctx):
        """butt"""

        channelid = ctx.message.channel.id
        if channelid not in self.lastMsgInChannel:
            return
        msg = self.lastMsgInChannel[channelid].clean_content
        words = msg.split()
        index = random.randint(0, len(words) - 1)
        words[index] = "butt"
        await self.bot.say(" ".join(words))


def setup(bot):
    b = Butt(bot)
    bot.add_listener(b.on_message, "on_message")
    bot.add_cog(b)

