import discord
from discord.ext import commands
from Bio import SeqIO
from Bio.Data import CodonTable
import pathlib

class TraduzirSequencias(commands.Cog):
    def __init__(self, boss):
        self.boss = boss

    @commands.command("Traduzir")
    async def traduzir(self, ctx, tabela_id: int, attachment: discord.Attachment):

        arquivo_saida = "traducoes.txt"

        tabela_codon = CodonTable.unambiguous_dna_by_id[tabela_id]
        traducoes = []

        # Iterar sobre as sequências no arquivo fasta
        for seq_record in SeqIO.parse(f"{attachment.filename}", "fasta"):
            # Verificar a presença de 'N' na sequência
            if 'N' in seq_record.seq:
                await ctx.send(f"A sequência ID: {seq_record.id} contém bases 'N' e não pode ser traduzida.")
                continue

            sequencia_traduzida = seq_record.seq.translate(table=tabela_codon, to_stop=False)

            traducoes.append((seq_record.id, str(sequencia_traduzida)))

        with open(arquivo_saida, "w") as arquivo:
            for id_seq, traducao in traducoes:
                arquivo.write(f"{id_seq}\n"
                              f"{traducao}\n"
            "<--------------------------------------->\n\n\n")

        with open(arquivo_saida, "rb") as arquivo:
            await ctx.send("Aqui estão as traduções: ", file=discord.File(arquivo, filename=arquivo_saida))

        pathlib.Path(arquivo_saida).unlink()

async def setup(boss):
    await boss.add_cog(TraduzirSequencias(boss))
