from Bio import SeqIO
from Bio import BiopythonWarning
import warnings
import discord
from discord.ext import commands

import pathlib

class ConvertGenbankToFasta(commands.Cog):
    def __init__(self, boss):
        #super().__init__()
        self.boss = boss
        
    @commands.command("GenbankToFasta")
    async def ConvertFasta_GenBank(self, ctx, attachment: discord.Attachment):
        data = await attachment.read()        
        with open(f'{attachment.filename}', 'w') as arquivo:
            arquivo.write("%s"%data.decode())#Não consigo dizer quão produtivo é reescrever e não baixar o arquivo via discord.Attachment.save()
        
        count = SeqIO.convert(f'{attachment.filename}', "genbank", "output.fasta", "fasta","DNA")                 
        await ctx.send(f"Conversão concluída! {count} sequências foram convertidas com sucesso.")
        with open(f'output.fasta', 'rb') as arquivo:  
            await ctx.send("Aqui está o arquivo:",file=discord.File(arquivo, "Arquivo_Fasta.fasta"))        
        
        if (BiopythonWarning):
            warnings.simplefilter('ignore', BiopythonWarning)
            print(f"{BiopythonWarning.__name__}: {warnings.catch_warnings}")
            await ctx.send("Verifique se o arquivo está correto", ephemeral = True) 
                
        final_attch=pathlib.Path(f'{attachment.filename}')
        final_attch.unlink()
        final_attch=pathlib.Path('output.fasta')
        final_attch.unlink() 

async def setup(boss):
    await boss.add_cog(ConvertGenbankToFasta(boss))
                