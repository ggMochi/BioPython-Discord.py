from Bio import SeqIO
import pathlib
import discord
from discord.ext import commands
from io import StringIO

class UploadGenbankProtein(commands.Cog):
    def __init__(self, boss):
        #super().__init__()
        self.boss = boss
        
    @commands.command("UploadGenbankGene")
    async def uploadProtein(self, ctx, attachment: discord.Attachment):
        
        genes_codificantes = {} 
        countgene =0
        rRNAs = {}
        countrRNA=0
        tRNAs = {}
        counttRNA=0
        data = await attachment.read()
   
        for record in SeqIO.parse(StringIO(data.decode()), "genbank"):
            for feature in record.features:  
                if feature.type == 'CDS':
                    gene_name = feature.qualifiers.get('gene', ['Unknown'])[0] + ' - ' + feature.qualifiers.get('product', ['Unknown'])[0]
                    genes_codificantes[gene_name] = genes_codificantes.get(gene_name, 0) + 1
                    countgene+=1
                    
                elif feature.type == 'rRNA':
                    rRNA_name = feature.qualifiers.get('product', ['Unknown'])[0]
                    rRNAs[rRNA_name] = rRNAs.get(rRNA_name, 0) + 1
                    countrRNA+=1
                    
                elif feature.type == 'tRNA':
                    tRNA_name = feature.qualifiers.get('product', ['Unknown'])[0]
                    tRNAs[tRNA_name] = tRNAs.get(tRNA_name, 0) + 1
                    counttRNA+=1
                    
        with open(f'{attachment.filename}.txt', 'w') as arquivo: #Não sei quão relevantes são esses pontos do docorgi

            arquivo.write(f'\nGenes codificantes:{countgene}\n\n') 
            for gene_name, count in genes_codificantes.items():
                arquivo.write(f'{gene_name}: {count}\n')
            arquivo.write(f'\n\nrRNAs:{countrRNA}\n\n')
            for rRNA_name, count in rRNAs.items():
                arquivo.write(f'{rRNA_name}: {count}\n')
            arquivo.write(f'\n\ntRNAs:{counttRNA}\n\n')
            for tRNA_name, count in tRNAs.items():
                arquivo.write(f'{tRNA_name}: {count}\n')
        
        with open(f'{attachment.filename}.txt', 'rb') as arquivo:        
            await ctx.send("Aqui está o arquivo", file=discord.File(arquivo))        
    
        final_attch=pathlib.Path(f'{attachment.filename}.txt')
        final_attch.unlink() 

async def setup(boss):
    await boss.add_cog(UploadGenbankProtein(boss))