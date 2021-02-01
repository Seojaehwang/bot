import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("배그")
    await client.change_presence(status=discord.Status.online, activity=game)

sub = 0

@client.event
async def on_message(message):
    if message.content.startswith(";안녕"):
        await message.channel.send("안녕 반가워 난 말로징 봇이라고 해, 난 스크립트를 잘하징")
    if message.content.startswith(";서버"):
            await message.content.startswith("서버가 열려 있습니다")
    if message.content.startswith(";춤춰바"):
        await message.channel.send("전 몸치여서 춤을 못춰요 ㅎㅎ")
    if message.content.startswith(";자기소개"):
        await message.channel.send("난 말로징봇이구 스크립트를 잘해, 나는 크왕이의 코드에서 태어났고 말로징을 기반으로 만들어 졌어")
    if message.content.startswith(";바보야"):
        await message.channel.send("바보가 뭔뜻이야?")
    if message.content.startswith(";힘들어"):
        await message.channel.send("힘내자!")
    if message.content.startswith(";비트박스"):
        await message.channel.send("나는야 말로징 봇, 챗봇이징 말로징을 기반으로 만들어졌징 예!")
    if message.content.startswith(";사랑해"):
        await message.channel.send("나도(づ￣ 3￣)づ")





client.run("ODA1NjE5MzI5OTI3NDc5MzM2.YBdhdw.9Qdr08brKF_Swmc8GTNMXxQa2HA")




