from Bio.Seq import Seq
from Bio import SeqIO
from io import StringIO

import pathlib
import discord
from discord.ext import commands

class UploadFasta(commands.Cog):
    def __init__(self, boss):
        #super().__init__()
        self.boss = boss
        
    @commands.command("UploadFasta")
    async def upload(self, ctx, attachment: discord.Attachment):
    
        data = await attachment.read()
        
        with open(f'{attachment.filename}.txt', 'w') as arquivo: #Não sei quão relevantes são esses pontos do docorgi
            for record in SeqIO.parse(StringIO(data.decode()), "fasta"):
                #print("ID %s" % record.id) 
                sequence=Seq(record.seq)
                arquivo.write("ID: %s \n" % record.id + 
                                "Sequencia: %s\n" %record.seq + 
                                "Tamanho da Sequencia: %s\n\n" % len(record) +
                                "Complemento: %s\n\n" % sequence.complement() +
                                "Template: %s\n\n" % sequence.reverse_complement() +
                                "RNA: %s\n\n" % sequence.transcribe()+
                                "\n\n") 
        
        with open(f'{attachment.filename}.txt', 'rb') as arquivo:        
            await ctx.send("Aqui está o arquivo", file=discord.File(arquivo))        
    
        final_attch=pathlib.Path(f'{attachment.filename}.txt')
        final_attch.unlink() 

async def setup(boss):
    await boss.add_cog(UploadFasta(boss))
