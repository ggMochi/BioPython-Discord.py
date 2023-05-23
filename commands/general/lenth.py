from Bio.Seq import Seq
from discord.ext import commands

class Length(commands.Cog):
    def __init__(self, boss):
        #super().__init__()
        self.boss = boss
        
    @commands.command("Tamanho")
    async def length(self, ctx, seq):
        if seq == ValueError:
            pass 
    
        sequence = Seq(seq)
        await ctx.send(f'A sequencia possui: {len(sequence)} bases')

         

async def setup(boss):
    await boss.add_cog(Length(boss))