from discord.ext import commands


class Testing(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Test command"""
        await ctx.send(f'Pong! {ctx.message.author.mention}')


def setup(bot):
    bot.add_cog(Testing(bot))