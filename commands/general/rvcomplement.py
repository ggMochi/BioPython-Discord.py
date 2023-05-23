from Bio.Seq import Seq
from discord.ext import commands

class ReverseComplement(commands.Cog):
    def __init__(self, boss):
        #super().__init__()
        self.boss = boss
        
    @commands.command("RVC")
    async def ReverseComplement(self, ctx, seq):
        if seq == ValueError:
            pass 
    
        sequence = Seq(seq)
        await  ctx.send(f'Reverse complement: {sequence.reverse_complement()}')

async def setup(boss):
    await boss.add_cog(ReverseComplement(boss))