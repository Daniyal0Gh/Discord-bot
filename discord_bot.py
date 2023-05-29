import discord


client = discord.Client()


@client.event
async def on_ready():
    print('Bot Is Ready!')
    print('created by Daniyal__Gh')

#send massage 
@client.event
async def on_message(massage):
  if massage.author == client.user:
    return
#pm hay ahval porsi
  if massage.content.startswith('$salam'):
    await massage.channel.send('salam be roy golet🌹')
  if massage.content.startswith('$chetori'):
    await massage.channel.send('man khobam to chetori❤')
  if massage.content.startswith('$khobam'):
    await massage.channel.send('khodaro shokr🙏')
  if massage.content.startswith('$chekhabar'):
    await massage.channel.send('salamti⚡')
#pm hay robat
  if massage.content.startswith('$ki to ro sakhte'):
    await massage.channel.send('{Daniyal__Gh}mano sakhte👾')
  if massage.content.startswith('$to ki hasti'):
    await massage.channel.send('man robat BRAVO team hastam')
  if massage.content.startswith('$bravo'):
    await massage.channel.send('🏆THE BEST SERVER GAMING IN IRAN🏆')
  if massage.content.startswith('$link'):
    await massage.channel.send("https://discord.gg/JXMecUF")



   

#starter BOT
client.run('')#token is here