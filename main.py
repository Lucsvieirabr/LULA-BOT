import random
import html
import datetime
import time
import discord
from PIL import Image
from PIL import ImageFont, ImageDraw
from discord.ext import commands
import dropbox
from discord import user
msg_id = None
msg_user = None
from discord import permissions
import dropbox.files
import youtube_dl
from discord import opus
BOT_PREFIX = '+'
bot = commands.Bot(command_prefix=BOT_PREFIX)
players = {}
COR = 0xF7FE2E
cliente = discord.Client()
clienti = commands.Bot(command_prefix='+')


@cliente.event
async def on_ready():
    print('--------Olá mundo!!!----------')
    print('------- {0.user} -------------'.format(cliente))


@cliente.event
async def on_message(message):
    if (message.author.id == 'TOKEN DO SEU BOT'): return
    global escolhido, embed, rola
    if message.content.startswith('+'):
        huy = message.content[1:].strip()
        if huy.lower().startswith('ola'):
            dd = 689589012045889588
            embed = discord.Embed(title='',
                                  description='👻 Olá <@{}>, prazer em lhe conhecer, me chamo <@{}> 👻 '.format(
                                      message.author.id, dd), colour=discord.Colour.dark_blue())
            embed.set_image(url='https://media.giphy.com/media/fuWRtScJPRWtOdNymv/giphy.gif')
            await cliente.send_message(message.channel, embed=embed)
            return
    if message.content.startswith('+'):
        frase = message.content[1:].strip()
        if frase.lower().startswith('moeda'):
            a = str("Cara")
            b = str("Coroa")
            lista = [a, b]
            escolhido = random.choice(lista)
            await cliente.send_message(message.channel, str(
                "A moeda está girando....Ela caiu...O lado sorteado foi {}".format(escolhido)))
            return
    if message.content.startswith('+'):
        mg = message.content[1:].strip()
        if mg.lower().startswith('anime'):
            gen = Image.open('gen.jpg')
            oi = Image.open('af.jpg')
            lo = Image.open('as.jpg')
            pt = Image.open('pg.jpeg')
            pg = Image.open('ph.jpeg')
            pw = Image.open('pi.jpg')
            pp = Image.open('pl.jpg')
            px = Image.open('po.jpg')
            pn = Image.open('pu.jpg')
            pm = Image.open('py.jpg')
            eds = Image.open('yu.jpg')
            ki = Image.open('ru.jpeg')
            ko = Image.open('ro.jpg')
            ku = Image.open('ri.jpeg')
            ka = Image.open('re.jpg')
            pod = Image.open('ra.jpg')
            fa = Image.open('animeum.jpg')
            fc = Image.open('animedois.jpg')
            fd = Image.open('animetres.jpg')
            fg = Image.open('animequatro.jpg')
            gh = Image.open('animecinco.jpg')
            fb = Image.open('animeseis.jpg')
            fv = Image.open('animesete.jpg')
            listao = [gen, pod, ku, ka, ki, eds, pm, pn, px, pp, pw, pg, pt, lo, oi, fa, fc, fd, fg, gh, fb, fv]
            premiado = random.choice(listao)
            premiado.save('imagem.png')
            await cliente.send_file(message.channel, 'imagem.png')
            return
    if message.content.startswith('+'):
        jae = message.content[1:].strip()
        if jae.lower().startswith('reco'):
            a = str('beatless')
            b = str('Sekirei')
            c = str('Netoge no yome')
            d = str('Taimadou gakuen')
            e = str('Owari no seraph')
            f = str('Dakara boku a')
            g = str('Amagi Brilliant park')
            h = str('Qwaser')
            i = str('Tsurezure children')
            ksd = str('Strike blood')
            m = str('Monster')
            n = str('Musume no iru')
            o = str('Nichijo')
            p = str('Trinity seven')
            q = str('Isekai wa smarthphone')
            r = str('Campione')
            s = str('outbreak commpany')
            y = str('black clover')
            aa = str('boruto')
            bb = str('boku no kanojo ka')
            cc = str('Magi: Sinbad')
            dd = str('one piece')
            ee = str('naruto')
            ff = str('drifters')
            qwer = str('Koe no katachi')
            shja = str('Your Name')
            global premiar
            listar = [ee, ff, dd, cc, bb, aa, y, s, r, q, p, o, n, m, ksd, i, h, g, a, b, c, d, e, f]
            premiar = random.choice(listar)
            hi = str('incrível')
            hs = str('magnifíco')
            hu = str('maravilhoso')
            ho = str('....ah..não tenho como descrever,só vai assistir')
            ha = str('lindo')
            listu = [hi, ho, hu, ha, hs]
            premiu = random.choice(listu)
            await cliente.send_message(message.channel,
                                       "Olá,está a procura de um anime né?segue a dica e vê {},é simplesmente {}".format(
                                           premiar, premiu))
            return
    if message.content.startswith('+'):
        jaer = message.content[1:].strip()
        if jaer.lower().startswith('slap'):
            juju = message.content[6:]
            jop = juju.lower()
            abc = 'https://media.giphy.com/media/tX29X2Dx3sAXS/giphy.gif'
            bbc = 'https://media.giphy.com/media/8UHRbvmsFVyS2VXJKU/giphy.gif'
            cbc = 'https://media.giphy.com/media/xUNd9HZq1itMkiK652/giphy.gif'
            dbc = 'https://media.giphy.com/media/xUO4t2gkWBxDi/giphy.gif'
            ebc = 'https://media.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif'
            fbc = 'https://media.giphy.com/media/hpzxqgsLMWGRO/giphy.gif'
            gbc = 'https://media.giphy.com/media/Zau0yrl17uzdK/giphy.gif'
            hbc = 'https://media.giphy.com/media/81kHQ5v9zbqzC/giphy.gif'
            ibc = 'https://media.giphy.com/media/xXRDuvEcMA2JO/giphy.gif'
            jbc = 'https://media.giphy.com/media/3dpfdh0xAsCDS/giphy.gif'
            kbc = 'https://media.giphy.com/media/Lm4Y4etZfUCU8/giphy.gif'
            lbc = 'https://media.giphy.com/media/105pswBAqO76Io/giphy.gif'
            mbc = 'https://media.giphy.com/media/oSxTZVgYML0ac/giphy.gif'
            nbc = 'https://media.giphy.com/media/XriT1FPiR1RRe/giphy.gif'
            obc = 'https://media.giphy.com/media/PrXKpiHKVCYUw/giphy.gif'
            pbc = 'https://media.giphy.com/media/vpenzlPOBAU3S/giphy.gif'
            qbc = 'https://media.giphy.com/media/10Am8idu3qBYRy/giphy.gif'
            rbc = 'https://media.giphy.com/media/8KyQQKqy5BgGI/giphy.gif'
            sbc = 'https://media.giphy.com/media/bQtStIffkBfs4/giphy.gif'
            ybc = 'https://media.giphy.com/media/SZKr1f1I7Tb3y/giphy.gif'
            zbc = 'https://media.giphy.com/media/NPob342JvoTJK/giphy.gif'
            xbc = 'https://media.giphy.com/media/ryxGBGURsirNC/giphy.gif'
            listgif = [abc, bbc, cbc, dbc, ebc, fbc, gbc, hbc, ibc, jbc, kbc, lbc, mbc, nbc, obc, pbc, qbc, rbc, sbc,
                       ybc, xbc, zbc]
            pregif = random.choice(listgif)
            user = discord.utils.get(message.server.members, name='ZERO', discriminator=6885)
            dd = message.author.id
            embed = discord.Embed(title='@{} está furioso:'.format(message.author),
                                  description='<@{}> deu um tapa com muita força em: {}'.format(dd, jop),
                                  colour=discord.Colour.red())
            embed.set_image(url=pregif)
            await cliente.send_message(message.channel, embed=embed)
            return
    if message.content.startswith('+'):
        jui = message.content[1:].strip()
        jok = message.content[8:]
        if jui.lower().startswith('cafune'):
            gif1 = 'https://media.giphy.com/media/ARSp9T7wwxNcs/giphy.gif'
            gif2 = 'https://media.giphy.com/media/5tmRHwTlHAA9WkVxTU/giphy.gif'
            gif3 = 'https://media.giphy.com/media/4HP0ddZnNVvKU/giphy.gif'
            gif4 = 'https://media.giphy.com/media/109ltuoSQT212w/giphy.gif'
            gif5 = 'https://media.giphy.com/media/xVgGouGtc21H2/giphy.gif'
            gif6 = 'https://media.giphy.com/media/ye7OTQgwmVuVy/giphy.gif'
            gif7 = 'https://i.pinimg.com/originals/2e/27/d5/2e27d5d124bc2a62ddeb5dc9e7a73dd8.gif'
            gif8 = 'https://i.pinimg.com/originals/18/69/a0/1869a087b74dc5a8152278bcb9381b7e.gif'
            gif9 = 'https://i.pinimg.com/originals/c2/34/cd/c234cdcb3af7bed21ccbba2293470b8c.gif'
            gif10 = 'https://thumbs.gfycat.com/FlimsyDeafeningGrassspider-small.gif'
            gif11 = 'https://gifimage.net/wp-content/uploads/2017/09/anime-head-pat-gif-1.gif'
            gif12 = 'https://gifimage.net/wp-content/uploads/2017/09/anime-head-pat-gif-5.gif'
            gif13 = 'https://66.media.tumblr.com/6289c42ea805f475698f02207da0a377/tumblr_p14hcsxPsb1tm1dgio1_400.gif'
            gif14 = 'https://66.media.tumblr.com/b4d110b98079b935512467aad091f068/tumblr_myki5bzz0U1shdfeho1_500.gif'
            gif15 = 'https://i.kym-cdn.com/photos/images/original/001/286/811/7c7.gif'
            gif16 = 'https://i.pinimg.com/originals/7e/e2/9b/7ee29b45d40b1b16d3705c31d1bceba0.gif'
            gif17 = 'https://media1.tenor.com/images/183ff4514cbe90609e3f286adaa3d0b4/tenor.gif?itemid=5518321'
            gif18 = 'https://media1.tenor.com/images/291ea37382e1d6cd33349c50a398b6b9/tenor.gif?itemid=10204936'
            gif19 = 'https://media1.tenor.com/images/c0bcaeaa785a6bdf1fae82ecac65d0cc/tenor.gif?itemid=7453915'
            gif20 = 'https://i.gifer.com/OVXY.gif'
            gif21 = 'https://66.media.tumblr.com/580396767c1ac6d9b0eeb02f7ede30de/tumblr_p9b11ijLuy1th206io2_500.gif'
            gif22 = 'https://i.pinimg.com/originals/a0/6d/65/a06d65ad49f019aaae3f30fb872df619.gif'
            gif23 = 'https://data.whicdn.com/images/125164822/original.gif'
            gif24 = 'https://i.imgur.com/42VnOL9.gif'
            gif25 = 'https://thumbs.gfycat.com/NaughtySpottedAsiantrumpetfish-size_restricted.gif'
            gif26 = 'https://media.giphy.com/media/lq72vRtxJtpgQ/giphy.gif'
            gif27 = 'https://media1.tenor.com/images/d6bc68f949e78c7d17b55d2f65e445c0/tenor.gif?itemid=5628617'
            listacaf = [gif1, gif2, gif3, gif4, gif5, gif6, gif7, gif8, gif9, gif10, gif11, gif12, gif13, gif14, gif15,
                        gif16, gif17, gif18, gif19, gif20, gif21, gif22, gif23, gif24, gif25, gif26, gif27]
            premicaf = random.choice(listacaf)
            embed = discord.Embed(title='@{} está carente'.format(message.author),
                                  description='<@{}> fez um cafuné em {} '.format(message.author.id, jok),
                                  colour=discord.Colour.purple())
            embed.set_image(url=premicaf)
            await cliente.send_message(message.channel, embed=embed)
            return
    if message.content.startswith('+'):
        bol = message.content[1:].strip()
        if bol.lower().startswith('bolsonaro'):
            b1 = 'https://i.pinimg.com/236x/e2/bd/32/e2bd32d523183eaae363154578b1c217.jpg'
            b2 = 'https://i.pinimg.com/236x/5b/97/4a/5b974a4c236127cb3d2af30a76bddf1c.jpg'
            b3 = 'https://i.pinimg.com/236x/58/6e/be/586ebec2089aca3a9dfd9dc91ffd1cfc.jpg'
            b4 = 'https://i.pinimg.com/236x/f0/ef/55/f0ef5503e92a92d4cd1e50a1dd7b7a6f.jpg'
            b5 = 'https://i.pinimg.com/236x/f0/48/df/f048df0be1f5ed516fc7ea485c8c28f9.jpg'
            b6 = 'https://i.pinimg.com/236x/67/67/42/676742a67061a70aa6c4cf55a25a35e9.jpg'
            b7 = 'https://i.pinimg.com/236x/79/77/94/7977949fa9e2fd1bc9bab0e252e042e3.jpg'
            b8 = 'https://i.pinimg.com/236x/7a/84/7e/7a847ecbd7614e4f1734c814678bcd2e.jpg'
            b9 = 'https://i.pinimg.com/236x/60/bb/c0/60bbc09bf1daec99fed4422452d55677.jpg'
            b10 = 'https://i.pinimg.com/236x/83/cd/af/83cdaf6a1719cb697137b089fee26e3c.jpg'
            b11 = 'https://i.pinimg.com/236x/f0/48/df/f048df0be1f5ed516fc7ea485c8c28f9.jpg'
            b12 = 'https://i.pinimg.com/236x/48/62/4e/48624efabe36becae6a02ba0789c6246.jpg'
            b13 = 'https://i.pinimg.com/236x/43/ed/5c/43ed5c6eff34d74d41ba8fe07060e0f6.jpg'
            b14 = 'https://i.pinimg.com/236x/fe/7e/c5/fe7ec56a1e720ba870d6b342cc45e846.jpg'
            b15 = 'https://i.pinimg.com/236x/fe/20/7f/fe207fd6fa1cf716df3caa89c16a41a8.jpg'
            b16 = 'https://i.pinimg.com/236x/b0/f5/94/b0f59460eab6a9c6eeff7736be113a05.jpg'
            b17 = 'https://i.pinimg.com/236x/14/f0/d9/14f0d9faed20e4064b097dbb05b8bc25.jpg'
            b18 = 'https://i.pinimg.com/236x/f9/12/f8/f912f825c52cd5650b10255b637db3a9.jpg'
            b19 = 'https://i.pinimg.com/236x/79/8d/b0/798db054459bdbbc647628ad6e623965.jpg'
            b20 = 'https://i.pinimg.com/236x/75/ac/5e/75ac5ebb946ce200e251c9dc81adf13e.jpg'
            b21 = 'https://i.pinimg.com/236x/37/b5/9b/37b59b74709ce75be664256272e008ab.jpg'
            b22 = 'https://i.pinimg.com/236x/d9/2f/2d/d92f2dfdcc1a95a7f7ffb3d0ea7943f8.jpg'
            b23 = 'https://i.pinimg.com/236x/ff/0e/92/ff0e92a82a6cdc0002176a93175fd115.jpg'
            b24 = 'https://i.pinimg.com/236x/1f/d5/86/1fd586dc2488909fd860406d1c22d566.jpg'
            b25 = 'https://i.pinimg.com/236x/25/8c/ab/258cab7246d7fa4ced8df50ddb079594.jpg'
            b26 = 'https://i.pinimg.com/236x/96/a1/68/96a1681d1a26525f6135defb5edb0670.jpg'
            b27 = 'https://i.pinimg.com/236x/bd/46/b4/bd46b488c1015b74040456143c40ad54.jpg'
            b28 = 'https://i.pinimg.com/236x/9c/d3/11/9cd3111f1740c259b8e1ad02eaf26bc7.jpg'
            b29 = 'https://i.pinimg.com/236x/d5/29/61/d52961d364ebb4c7391c1e79ef31af70.jpg'
            b30 = 'https://i.pinimg.com/236x/29/f1/65/29f1650eeb12448645d724721e66ea77.jpg'
            b31 = 'https://i.pinimg.com/236x/50/9d/29/509d29cf2e92d8939fe93c9f90ad7659.jpg'
            listabos = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20, b21,
                        b22, b23, b24, b25, b26, b27, b28, b29, b30, b31]
            premiabols = random.choice(listabos)
            embed = discord.Embed(title='@{} , o nosso presidente é incrível né?'.format(message.author),
                                  description='<@{}> , separei esse meme pra você:  '.format(message.author.id),
                                  colour=discord.Colour.light_grey())
            embed.set_image(url=premiabols)
            await cliente.send_message(message.channel, embed=embed)
            return

    if message.content.startswith('+'):
        bolr = message.content[1:].strip()
        if bolr.lower().startswith('comandos'):
            embed = discord.Embed(
                title="Olá {}, deseja vêr minha lista de comandos né,ainda tenho poucos mas estou evoluindo a cada dia: ".format(
                    message.author),

                color=discord.Colour.dark_orange(),
                description="<@{}> essa é minha lista de comandos: ".format(message.author.id))
            embed.add_field(name="+ola", value="Te darei um oi especial", inline=False)
            embed.add_field(name="+slap", value="Está com raiva de alguém? esse é o comando perfeito", inline=True)
            embed.add_field(name="+moeda",
                            value="Jogarei uma moeda pra cima,você consegue acertar qual lado ela vai cair?",
                            inline=True)
            embed.add_field(name="+cafune", value="Faça carinho em quem você quiser", inline=True)
            embed.add_field(name="+bolsonaro", value="Enviarei um meme aleatorio incrível de nosso presidente",
                            inline=True)
            embed.add_field(name="+animes", value="Um meme aleatorio de anime especial para você", inline=True)
            embed.add_field(name="+reco", value="Está sem anime pra vêr? eis a solução", inline=True)
            embed.add_field(name="+avatar",
                            value="Acione o comando e mencione uma pessoa do server que eu manderei a imagem de perfil dela",
                            inline=True)
            embed.add_field(name="+op", value="GIFS épicos ou engraçados de One Pice especias para você", inline=True)
            embed.add_field(name="+pp",
                            value="Sabe aquele meme conhecido do bebe e suas primeiras palavras? acione o comando e escolha oque ele vai falar",
                            inline=True)
            embed.add_field(name="+piada",
                            value="Essa área é perigosa, ative se tiver consciência do que está fazendo kkkk",
                            inline=True,)
            embed.add_field(name="+cor",
                            value="Cansado da cor padrão , eu tenho a solução!",
                            inline=True, )
            embed.add_field(name="+sec21",
                            value="Sabe aqueles memes incríveis de adolecentes no séc21.. acione e mandeirei um aleatório para você",
                            inline=True)
            embed.set_image(url='https://media.giphy.com/media/fuWRtScJPRWtOdNymv/giphy.gif')
            await cliente.send_message(message.channel, embed=embed)
            return
    if message.content.startswith('+'):
        br = message.content[1:].strip()
        if br.lower().startswith('avatar'):
            if message.mentions.__len__() > 0:
                for us in message.mentions:
                    av = us.avatar_url
                    embed = discord.Embed(
                        title="Olá {},deseja ter a imagem dele né? ".format(
                            message.author),
                        color=discord.Colour.dark_orange(),
                        description="<@{}> como prometido, ta ai: ".format(message.author.id))
                    embed.set_image(url=av)
                await cliente.send_message(message.channel, embed=embed)
                return
    if message.content.startswith('+'):
        huy = message.content[1:].strip()
        texto = message.content[3:].strip()
        ret = message.content[6:].strip()
        doisp = texto.strip(str(ret))
        doispp = doisp + str('...')
        if huy.lower().startswith('pp'):
            dbx = dropbox.Dropbox('jOzZ7BfHhRAAAAAAAAAAbw2b8IZQ61xBjw7uYIhN2bH1yh5p1_BPPskUqsKzyj0K')
            img = Image.open('WhatsApp Image 2020-03-19 at 17.18.08.jpeg')
            fonte = ImageFont.truetype('certa.ttf', 50)
            escrever = ImageDraw.Draw(img)
            escrever.text(xy=(10, 15), text=doispp + doispp, fill=(0, 0, 0), font=fonte)
            img.save('whats2.png')
            img2 = Image.open('whats2.png')
            fonte2 = ImageFont.truetype('certa.ttf', 45)
            escrever = ImageDraw.Draw(img)
            escrever.text(xy=(10, 305), text=texto + str('!!!'), fill=(0, 0, 0), font=fonte2)
            img.save('whats3.png')
            await cliente.send_file(message.channel, 'whats3.png')
            return
    if message.content.startswith('+'):
        yui = message.content[1:]
        if yui.lower().startswith('op'):
            op1 = 'https://media.giphy.com/media/136n9rP7K1fvqw/giphy.gif'
            op2 = 'https://media.giphy.com/media/QltmijjW1vcnC/giphy.gif'
            op3 = 'https://media.giphy.com/media/J9aCXNRgRKqNq/giphy.gif'
            op4 = 'https://media.giphy.com/media/T9lEux2hPQYne/giphy.gif'
            op5 = 'https://media.giphy.com/media/tIZUToOMEFGM0/giphy.gif'
            op6 = 'https://media.giphy.com/media/dYtNHNGCCSMX6/giphy.gif'
            op7 = 'https://media.giphy.com/media/rCdzKS756yiGs/giphy.gif'
            op8 = 'https://media.giphy.com/media/rCdzKS756yiGs/giphy.gif'
            op9 = 'https://media.giphy.com/media/HLxxu7f131ypy/giphy.gif'
            op10 = 'https://media.giphy.com/media/uQjxEEdDhmqbK/giphy.gif'
            op11 = 'https://media.giphy.com/media/B2CxNosDKhYiY/giphy.gif'
            op12 = 'https://media.giphy.com/media/Qcrmc6dbGyLMQ/giphy.gif'
            op13 = 'https://media.giphy.com/media/137G0psMDt22gU/giphy.gif'
            op14 = 'https://media.giphy.com/media/vfTWTF1OFO4ik/giphy.gif'
            op15 = 'https://media.giphy.com/media/nQDKSeRlIyfmw/giphy.gif'
            op16 = 'https://media.giphy.com/media/fO64lYHZfTgmk/giphy.gif'
            op17 = 'https://media.giphy.com/media/MiBjaJYukUyC4/giphy.gif'
            op18 = 'https://media.giphy.com/media/idXYLeInD4wkU/giphy.gif'
            op19 = 'https://media.giphy.com/media/biFwyelRgl5wQ/giphy.gif'
            op20 = 'https://media.giphy.com/media/1qGaYAEAk7eOA/giphy.gif'
            op21 = 'https://media.giphy.com/media/M7vuylW3ons0E/giphy.gif'
            op22 = 'https://media.giphy.com/media/145oanYST4wYhi/giphy.gif'
            op23 = 'https://media.giphy.com/media/67s8C7oF1fSIDe1ib0/giphy.gif'
            op24 = 'https://media.giphy.com/media/7HyjMW9JKFgmQ/giphy.gif'
            op25 = 'https://media.giphy.com/media/12mRllHWXpt4M8/giphy.gif'
            op26 = 'https://media.giphy.com/media/uaJLuMokII24w/giphy.gif'
            op27 = 'https://media.giphy.com/media/7VORL6fuVCARW/giphy.gif'
            op28 = 'https://media.giphy.com/media/uSczV8io3XROU/giphy.gif'
            op29 = 'https://media.giphy.com/media/1QXBllMyrIqRO/giphy.gif'
            op30 = 'https://media.giphy.com/media/aXpDSRxhgdx5e/giphy.gif'
            criac = [op1, op2, op3, op4, op5, op6, op7, op8, op9, op10, op11, op12, op13, op14, op15, op16, op17, op18,
                     op19, op20, op21, op22, op23, op24, op25, op26, op27, op28, op29, op30]
            result = random.choice(criac)
            embed = discord.Embed(
                title="Olá {}, deseja um gif de one piece: ".format(
                    message.author),
                color=discord.Colour.teal(),
                description="<@{}> como prometido, um gif épico saindo do forno: ".format(message.author.id))
            embed.set_image(url=result)
            await cliente.send_message(message.channel, embed=embed)
            return

    if message.content.startswith('+'):
        yo = message.content[1:].strip()
        if yo.lower().startswith('cor'):
            link = 'https://media.giphy.com/media/sIIhZliB2McAo/200.gif'
            embed = discord.Embed(
                title="Olá {},a cor padrão é meio feia né,escolha sua agora: ".format(message.author),
                color=discord.Colour.gold(),
                description="-Roxo =  🟣\n"
                            "-Verde = 🟢\n"
                            "-Rosa = 🌸\n"
                            "-Laranja = 🟠\n"
                            "-Amarelo = 🟡\n"
                            "-Azul = 🟦\n")
            embed.set_image(url=link)
            botmsg = await cliente.send_message(message.channel, embed=embed)
            await cliente.add_reaction(botmsg, "🟣")
            await cliente.add_reaction(botmsg, "🟢")
            await cliente.add_reaction(botmsg, "🌸")
            await cliente.add_reaction(botmsg, "🟠")
            await cliente.add_reaction(botmsg, "🟡")
            await cliente.add_reaction(botmsg, "🟦")

            global msg_id
            msg_id = botmsg.id

            global msg_user
            msg_user = message.author

    if message.content.startswith('+'):
        yo = message.content[1:].strip()
        if yo.lower().startswith('piada'):
            p1 = ("Por que o Luke Skywalker escondeu seus livros? \n"
                  "Porque ele não quer que a Princesa Leia")
            p2 =  ("Por que o bombeiro não caminha? \n"
                   "Porque ele socorre")
            p3 = ("Por que o policial não usa sabão? \n"
                   "Porque ele prefere deter gente")
            p4 = ("Por que a estante não se move? \n"
                  "Porque ela é cômoda")
            p5 = ("Por que o caminhão de frigorífico não sobe a ladeira? \n"
                   "Porque elingüiça")
            p6 = ("Por que o motoboy foi demitido? \n"
                   "Porque não estava capacetado para o trabalho")
            p7 = ("Por que o cego é um bom pedreiro? \n"
                   "Porque ele apalpa toda a obra")
            p8 = ("Por que a família do músico sente saudades dele? \n"
                   "Porque ele faz flauta")
            p9 = (" Por que o rádio não pode ter filhos? \n"
                  "Porque ele é stereo")
            p10 = ("Por que no exército não falta luz? \n"
                    "Porque todo cabo já foi soldado")
            p11 = ("Por que não se deve comer a bíblia? \n"
                    "Porque tem salmonela")
            p12 = (" Por que o bebê prestou queixa na delegacia? \n"
                     "Porque foi fraldado")
            p13 = ("Por que fizeram 3 furos na régua? \n"
                   "Porque medidas tinham que ser tomadas")
            p14 = ("Por que a mocinha não pode aproveitar a Black Friday? \n"
                    "Porque só tem promoção")
            p15 = ("Porque a Dona Florinda foi mal atendida no McDonald's? \n"
                   "Porque ela foi de Bobs")
            p16 = ("Por que dói mais tropeçar numa caixa de som? \n"
                    "Porque amplificador")
            p17 = ("Por que tem mulher que ri com comercial de remédio? \n"
                    "Porque o Ministério da Saúde a diverte")
            p18 = ("Por que as cartas sempre chegam nas operadoras de telefonia móvel? \n"
                   "Porque tem selo lá")
            p19 = ("Por que o terrorista não foi trabalhar? \n"
                    "Porque estava de atestado islâmico")
            p20 = ("Por que o petróleo foi ao psicólogo? \n"
                    "Porque estava no fundo do poço")
            p21 = ("Por que o vendedor de instrumentos musicais não pode xingar os outros? \n"
                    "Porque o que vende baixo não me atinge")
            p22 = ("Por que o caminhoneiro não pega mulher no deserto? \n"
                    "Porque é muita areia pro seu caminhão")
            p23 = ("Por que a loja de canivete faliu? \n"
                    "Porque só vendia afiado")
            p24 = ("Por que a faxineira não luta karatê? \n"
                    "Porque ela já luta capoeira")
            p25 = ("Por que o Gene Simmons criou uma banda? \n"
                    "Porque ele Kiss")
            p26 = ("Por que o contorcionista está sempre cansado? \n"
                    "Porque trabalha dobrado")
            p27 = ("Por que a fita isolante vence a fita crepe? \n"
                   "Porque é faixa preta")
            p28 = ("Por que a mulher bonita foi demitida do trabalho voluntário? \n"
                      "Porque ela não dava sopa pra ninguém")
            p29 = ("Por que o Batman colocou o batmóvel no seguro? \n"
                    "Porque ele tem medo que Robin")
            p30 = ("Como o Batman conheceu o Robin? \n"
                    "Pelo bat-papo")
            p31 = ("Por que o Batman entrou na igreja? \n"
                    "Para participar de um bat-zado")
            p32 = ("Por que a mulher do Hulk largou ele? \n"
                    "Ela queria um homem mais maduro")
            p33 = ("O que o The Flash disse para a Mulher Maravilha antes de dar uma rapidinha? \n"
                    "Vai ser bom, não foi?")
            p34 = ("O que é um ponto preto lutando de espada? \n"
                    "É um be-zorro")
            p35 = ("O que são 5 pontos coloridos no jardim? \n"
                    "Os Flower Rangers")
            p36 = ("Por o que o Hulk grita quando se tranforma? \n"
                    "Porque a cueca dele não rasga")
            p37 = ("Onde comprar comida para um Super-Herói? \n"
                    "No Super-Mercado")
            p38 = ("O que aconteceu quando o Super-Homem morreu? \n"
                    "O Lex ficou de Luthor")
            p39 = ("Qual o programa preferido do Bruce Banner? \n"
                    "Caldeirão do Hulk")
            p40 = ("Qual o jogo em que o Batman ensina a dar salto mortal? \n"
                    "Mortal Kombatman")
            p41 = ("Qual o game que só tem 1, 3, 5, 6, 7 e 9? \n"
                    "Age of Impares")
            p42 = ("Qual o estado que solta hadouken? \n"
                    "O Ryu de Janeiro")
            p43 = ("O que são vários pontinhos amarelos na praia? \n"
                    "Um arrastão de Pac-Man")
            p44 = ("O que a polícia do Street Fighter faz? \n"
                    "Honda")
            p45 = ("Qual o café preferido do gamer? \n"
                    "NEScafé")
            p46 = ("Qual o jogo preferido do Hitler? \n"
                    "Meinkraft")
            p47 = ("Qual o jogo preferido do Hitler? \n"
                    "Meinkraft")
            p48 = ("Mataram o Ash, qual o nome do filme? \n"
                    "Mewtwo matou um cara")
            p49 = ("Por que o Mario se dá bem na fase da água? \n"
                    "Porque ele é marinho")
            p50 = ("Qual o game que está sempre gripado? \n"
                   "O Overwatchim")

            listp = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p34, p35, p36, p37, p38, p39, p40, p41, p42, p43, p44, p45, p46, p47, p48, p49, p50]
            resp = random.choice(listp)

            gr1 = 'https://media2.giphy.com/media/pa1WaYStUKyLC/giphy.gif'
            gr4 = 'https://media.giphy.com/media/Tgjj2PSbr3pL2/giphy.gif'
            gr5 = 'https://media1.giphy.com/media/Ol5txbUddBL7a/source.gif'
            gr6 = 'https://66.media.tumblr.com/7b0a9b55a9a98f0f742d48f0714f57a2/tumblr_p015gkhon91tydz8to1_400.gifv'
            listgg = [gr1, gr4, gr5, gr6]
            linke = random.choice(listgg)
            re1 = "Essa até eu ri kkkk"
            re2 = "Não é possível kkkk"
            re3 = "Vocês seres humanos não tem nada pra fazer não kkkkkkkk"
            re4 = "Essa é ruim assumo"
            re5 = "Me superei agora kkkk"
            listr = [re1, re2, re3, re4, re5]
            listadere = random.choice(listr)
            embed = discord.Embed(
                title="Quer rir? eu sou perfeito pra isso kkkk: ",
                color=discord.Colour.orange(),
                description=None)
            embed.add_field(name="{}".format(listadere),
                            value=resp,
                            inline=True)
            embed.set_image(url=linke)
            await cliente.send_message(message.channel, embed=embed)

    if message.content.startswith('+'):
        ftt = message.content[1:].strip()
        if ftt.lower().startswith('sec21'):
            m1 = 'https://i.pinimg.com/originals/28/33/2c/28332cb4067ae5cfaca645146ad4feff.png'
            m2 = 'https://i.pinimg.com/236x/a1/fe/f9/a1fef9cb30b6ae90d9a96170ca0ca81a.jpg'
            m3 = 'https://i.pinimg.com/236x/41/30/ea/4130ea6dee86e0bf5a846bb782553b53.jpg'
            m4 = 'https://i.pinimg.com/236x/f2/c6/4a/f2c64ad804e9c126a4946666d68eb5eb.jpg'
            m5 = 'https://i.pinimg.com/236x/dd/4f/35/dd4f358c3a7f40eb7a836cf2be16f265.jpg'
            m6 = 'https://i.pinimg.com/236x/21/65/6c/21656c99f6987b714ecbe645fd89a795.jpg'
            m7 = 'https://i.pinimg.com/236x/44/41/b3/4441b353b2af0d8be77fe038d6e971c4.jpg'
            m8 = 'https://i.pinimg.com/236x/27/af/ea/27afea38226545e4e542d577a1669f5c.jpg'
            m9 = 'https://i.pinimg.com/236x/f4/54/a4/f454a45242359e13b324c69477bfb345.jpg'
            m10 = 'https://i.pinimg.com/236x/a9/a4/fc/a9a4fcd6f32895dad67310a5dec277d7.jpg'
            m11 = 'https://i.pinimg.com/236x/06/98/80/06988072f5979b466426081b7c7c5830.jpg'
            m12 = 'https://i.pinimg.com/236x/fe/b8/15/feb81538349ffb56d72f8b2670d398bf.jpg'
            m13 = 'https://i.pinimg.com/236x/ac/5a/f9/ac5af91d7aefa6d2e045908eadbc3e02.jpg'
            m14 = 'https://i.pinimg.com/236x/0f/59/7f/0f597f83d43af30cd986e94f78c641d8.jpg'
            m15 = 'https://i.pinimg.com/236x/ab/e1/ac/abe1acf629517e3754f157e381588986.jpg'
            m16 = 'https://i.pinimg.com/236x/92/32/dc/9232dc1483f1832314793802432ef0bc.jpg'
            m17 = 'https://i.pinimg.com/236x/ab/e1/ac/abe1acf629517e3754f157e381588986.jpg'
            m18 = 'https://i.pinimg.com/236x/0e/ac/14/0eac146dde3a12a356df1c0d20a99470.jpg'
            m19 = 'https://i.pinimg.com/236x/1e/67/2e/1e672e095623b0acdd067c2f025b6935.jpg'
            m20 = 'https://i.pinimg.com/236x/0c/ae/fb/0caefbdf6c00f6246e01024f721c1f97.jpg'
            m21 = 'https://pbs.twimg.com/media/ETmS_BsXQAEnF-f.jpg'
            m26 = 'https://pbs.twimg.com/media/D_esACCXUAAg79N.jpg:large'
            m27 = 'https://pbs.twimg.com/media/D_tG_lnWwAABZSc.jpg:large'
            m28 = 'https://pbs.twimg.com/media/EAXEZx9XoAEne-i.jpg:large '
            m29 = 'https://pbs.twimg.com/media/D_yu-SrU0AAHyMX.jpg:large'
            m30 = 'https://pbs.twimg.com/media/ECXv1xiXUAAz4Ob.png'
            m31 = 'https://pbs.twimg.com/media/D_o5hieX4AAY6Ko.jpg'
            m32 = 'https://pbs.twimg.com/media/EDV3TfvUcAU7AD3.jpg'
            m37 = 'https://pbs.twimg.com/media/D_UBnnBXoAA32nD.jpg'
            m38 = 'https://pbs.twimg.com/media/EAvEqH-WwAomMkm.jpg'
            m39 = 'https://pbs.twimg.com/media/EAH3zK5WwAEILwt.jpg'
            m41 = 'https://pbs.twimg.com/media/D_t4YjbXsAETGJT.jpg'
            m44 = 'https://pbs.twimg.com/media/ECcpahOXkAAXHyo.jpg:large'
            m45 = 'https://pbs.twimg.com/media/D_3VG1dX4AIHiXP.jpg'
            liym = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20, m21, m26, m27, m28, m29, m30, m31, m32, m37, m38, m39, m41, m44, m45]
            linkes = random.choice(liym)
            embed = discord.Embed(
                title="Adolecentes no Século 21 kkkkk: ",
                color=discord.Colour.orange(),
                description="Separei esse meme para você kkkkkk")
            embed.set_image(url=linkes)
            await cliente.send_message(message.channel, embed=embed)

    if message.content.startswith('+'):
        rtty = message.content[1:].strip()
        jok = message.content[6:]
        if rtty.lower().startswith('kick'):
            if message.mentions.__len__() > 0:
                for us in message.mentions:
                    userr = message.author.id
                    if userr == "ADMIN ID":
                        embed = discord.Embed(
                            title="Eu o declaro culpado ",
                            color=discord.Colour.orange(),
                            description="{},que o martelo da justiça caia sobre você!!".format(jok))
                        embed.set_image(url='https://media1.tenor.com/images/4c'
                                            '906e41166d0d154317eda78cae957a/tenor.gif?itemid=12646581')
                        await cliente.kick(us)
                        await cliente.send_message(message.channel, embed=embed)
                    else:
                        embed = discord.Embed(
                            title="Parece que você não possui a força ",
                            color=discord.Colour.orange(),
                            description="<@{}>, Você não é o meu criador!!!".format(message.author.id))
                        embed.set_image(url='https://thumbs.gfycat.com/PastUnconsciousHoneycreeper-size_restricted.gif')
                        await cliente.send_message(message.channel, embed=embed)

    if message.content.startswith('+'):
        rtty = message.content[1:].strip()
        jok = message.content[6:]
        if rtty.lower().startswith('mute'):
            if message.mentions.__len__() > 0:
                for us in message.mentions:
                    userr = message.author.id
                    if userr == "ADMIN ID":
                        embed = discord.Embed(
                            title="PELOS PODEROS DO ADMIN VOCE ESTÁ MUTADO",
                            color=discord.Colour.dark_blue(),
                            description="{},CALE-SE ATÉ OUTRAS ORDENS!!".format(jok))
                        embed.set_image(url='https://media1.tenor.com/images/371'
                                            'c86b0c819876f8f927b6e3bc15144/tenor.gif?itemid=12700315')
                        role = discord.utils.find(lambda r: r.name == "Mutado", message.server.roles)
                        await cliente.add_roles(us, role)
                        await cliente.send_message(message.channel, embed=embed)
                    else:
                        embed = discord.Embed(
                            title="Meus olhos dectaram um ser inferior tentando executar comandos do admin",
                            color=discord.Colour.orange(),
                            description="<@{}>, Você não é o meu criador!!!".format(message.author.id))
                        embed.set_image(url='https://kurokonobaskerpg.weebly.com/u'
                                            'ploads/1/2/1/2/12128159/1813041_orig.gif')
                        await cliente.send_message(message.channel, embed=embed)

    if message.content.startswith('+'):
        rtty = message.content[1:].strip()
        jok = message.content[6:]
        if rtty.lower().startswith('ban'):
            if message.mentions.__len__() > 0:
                for us in message.mentions:
                    userr = message.author.id
                    if userr == "ADMIN ID":
                        embed = discord.Embed(
                            title="O ADMIN TA ON",
                            color=discord.Colour.blue(),
                            description="{},FOI BANIDO PELO REI!!".format(jok))
                        embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS'
                                            'CNZJZMhZPmaGOtCk5nYn5Ussi5UXpY2JPjN9LwiQQp98wBzol')
                        await us.ban()
                        await cliente.send_message(message.channel, embed=embed)
                    else:
                        embed = discord.Embed(
                            title="Você não é meu criador, não possui essa permissão",
                            color=discord.Colour.orange(),
                            description="<@{}>,Você receberá oque plantou!!!".format(message.author.id))
                        embed.set_image(url='https://i.kym-cdn.com/photos/images/original/001/580/532/b35.gif')
                        await cliente.send_message(message.channel, embed=embed)
                        time.sleep(2.5)
                        await cliente.kick(message.author)
    if message.content.startswith('+'):
        tyi = message.content[1:].strip()
        jok = message.content[7:]
        if tyi.lower().startswith('unmute'):
            if message.mentions.__len__() > 0:
                for us in message.mentions:
                    userr = message.author.id
                    if userr == "409870907067203584":
                        embed = discord.Embed(
                            title="O admin é generoso...",
                            color=discord.Colour.blue(),
                            description="{}, O grande Admin destruio suas correntes!!".format(jok))
                        embed.set_image(url='https://media.tenor.com/images/147b55eec200488ca70dc994d47a00d2/tenor.gif')
                        role = discord.utils.find(lambda r: r.name == "Mutado", message.server.roles)
                        await cliente.remove_roles(us, role)
                        await cliente.send_message(message.channel, embed=embed)
                    else:
                        embed = discord.Embed(
                            title="Você é generoso, porém fraco!!",
                            color=discord.Colour.orange(),
                            description="<@{}>,O Criador é o único que pode me dar ordens desse tipo!!!".format(message.author.id))
                        embed.set_image(url='https://media.giphy.com/media/xULW8MYvpNOfMXfDH2/giphy.gif')
                        await cliente.send_message(message.channel, embed=embed)



@cliente.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    if reaction.emoji == "🟣" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Roxo", msg.server.roles)
        await cliente.add_roles(user, role)

    if reaction.emoji == "🟢" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Verde", msg.server.roles)
        await cliente.add_roles(user, role)

    if reaction.emoji == "🌸" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Rosa", msg.server.roles)
        await cliente.add_roles(user, role)

    if reaction.emoji == "🟠" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Laranja", msg.server.roles)
        await cliente.add_roles(user, role)

    if reaction.emoji == "🟡" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Amarelo", msg.server.roles)
        await cliente.add_roles(user, role)

    if reaction.emoji == "🟦" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Azul", msg.server.roles)
        await cliente.add_roles(user, role)


@cliente.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message
    if reaction.emoji == "🟣" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Roxo", msg.server.roles)
        await cliente.remove_roles(user, role)

    if reaction.emoji == "🟢" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Verde", msg.server.roles)
        await cliente.remove_roles(user, role)

    if reaction.emoji == "🌸" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Rosa", msg.server.roles)
        await cliente.remove_roles(user, role)

    if reaction.emoji == "🟠" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Laranja", msg.server.roles)
        await cliente.remove_roles(user, role)

    if reaction.emoji == "🟡" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Amarelo", msg.server.roles)
        await cliente.remove_roles(user, role)

    if reaction.emoji == "🟦" and msg_id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Azul", msg.server.roles)
        await cliente.remove_roles(user, role)

@cliente.event
async def on_member_join(member):
    canal = cliente.get_channel("689606043226865683")
    img = Image.open('bemvindo.jpg')
    fonte = ImageFont.truetype('Daitengu DEMO.otf', 120)
    escrever = ImageDraw.Draw(img)
    escrever.text(xy=(120, 5), text=member.name, fill=(106, 17, 148), font=fonte)
    img.save('bv.png')
    await cliente.send_file(canal, 'bv.png')

cliente.run('TOKEN DO SEU BOT')

OWNER == LUCAS VIEIRA DA SILVA ------ DISCORD == Darling#3852

