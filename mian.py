# test-bot(bot class)
# This example requires the 'members' and 'message_content' privileged intents to function.

import os
import discord
import random
from discord.ext import commands
from bot_logic import gen_pass

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
# command prefix 
bot = commands.Bot(command_prefix='>', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# adding two numbers
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

# spamming word
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

# password generator        
@bot.command()
async def pw(ctx):
    await ctx.send(f'Kata sandi yang dihasilkan: {gen_pass(10)}')

# coinflip
@bot.command()
async def coinflip(ctx):
    num = random.randint(1,2)
    if num == 1:
        await ctx.send('It is Head!')
    if num == 2:
        await ctx.send('It is Tail!')

# rolling dice
@bot.command()
async def dice(ctx):
    nums = random.randint(1,6)
    if nums == 1:
        await ctx.send('It is 1!')
    elif nums == 2:
        await ctx.send('It is 2!')
    elif nums == 3:
        await ctx.send('It is 3!')
    elif nums == 4:
        await ctx.send('It is 4!')
    elif nums == 5:
        await ctx.send('It is 5!')
    elif nums == 6:
        await ctx.send('It is 6!')

# welcome message
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

    # random local meme image
@bot.command()
async def mem(ctx):
    with open('mem/mem1.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)


# Event ketika bot sudah siap
@bot.event
async def on_ready():
    print('Bot telah siap!')

# Command untuk melakukan perkalian
@bot.command()
async def perkalian(ctx, angka1: int, angka2: int):
    hasil = angka1 * angka2
    await ctx.send(f'Hasil dari {angka1} * {angka2} adalah {hasil}')


# Event ketika bot sudah siap
@bot.event
async def on_ready():
    print('Bot telah siap!')

# Command untuk memberikan informasi tentang bahaya polusi
@bot.command()
async def polusi(ctx):
    pesan = "Polusi udara dapat memiliki dampak serius terhadap kesehatan manusia dan lingkungan. Polusi udara dapat meningkatkan risiko penyakit pernapasan, seperti asma dan bronkitis, serta meningkatkan risiko penyakit jantung dan kanker paru-paru. Selain itu, polusi udara juga dapat merusak lingkungan, mengurangi kualitas air dan tanah, serta merusak ekosistem dan keanekaragaman hayati."
    await ctx.send(pesan)

# Command untuk memberikan informasi tentang bahaya polusi
@bot.command()
async def Penyebab(ctx):
    pesan = ("1. Asap kendaraanAsap kendaraan, baik motor atau mobil, merupakan salah satu penyebab utama pencemaran udara. Asap ini terbentuk dari pembakaran bahan bakar fosil, seperti minyak bumi, yang biasanya digunakan untuk menghasilkan energi bagi transportasi.Emisi kendaraan mengandung gas karbon dioksida yang kemudian membentuk ozon di permukaan bumi dan menjadi polusi. Konsentrasi ozon penyebab polusi udara ini dapat meningkat jika cuaca sedang panas dan kelembapan udara rendah. 2. Pembangkit listrik Sama seperti kendaraan, pembangkit listrik juga menggunakan bahan bakar fosil minyak bumi dan batu bara untuk menghasilkan energi. Karena penggunaannya dalam skala besar, hasil pembakaran ini bisa menyumbang hampir 80% polusi udara.Selain karbon dioksida, pembakaran bahan bakar fosil pada pusat pembangkit listrik juga menjadi penyebab polusi udara. Pasalnya, kegiatan ini menghasilkan emisi sulfur nitrogen oksida, karbon dioksida, partikulat (PM), dan sulfur dioksida (SO2). 3. Limbah pertanianBidang pertanian juga turut andil dalam pencemaran udara, lho. Penggunaan pupuk yang berlebihan dan pupuk tidak layak guna dapat melepaskan gas ke udara yang disebut amonia (NH3). Selain itu, proses penyemprotan pestisida dan pembakaran untuk pembukaan lahan juga menyebabkan polusi udara.")
    await ctx.send(pesan)

