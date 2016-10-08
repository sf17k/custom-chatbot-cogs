import discord
from discord.ext import commands
import random


class Butt:
    """Butt"""

    def __init__(self, bot):
        self.bot = bot
        self.lastMsgInChannel = dict()

    @client.async_event
    def on_message(self, message):
        self.lastMsgInChannel[channel] = message
        await self.bot.process_commands(message)

    @commands.command(pass_context=True)
    async def butt(self, ctx):
        """butt"""

        channel = ctx.message.channel
        if channel not in lastMsgInChannel:
            return
        msg = self.lastMsgInChannel[channel].clean_content
        words = msg.split()
        index = random.randint(0, len(words) - 1)
        words[index] = "butt"
        await self.bot.say(str.join(words))


def setup(bot):
    bot.add_cog(Butt(bot))
