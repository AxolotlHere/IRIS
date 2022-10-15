import discord
import pandas as pd
import praw
import random
import discord.ext.commands as commands
import time







data_poke = pd.read_excel("Pokedex.xlsx")
poke_names = list(data_poke.Pokemon)
bot = commands.Bot(command_prefix="c!")
morning_time = [i for i in range(5,12)]
afternoon_time = [i for i in range(11,17)]
evening_time = [i for i in range(16,19)]
night_time = [i for i in range(18,6)]


@bot.event
async def on_ready():
    general_server = bot.get_channel(905110214188105801)
    await general_server.send("Hello Im in how are you guys doing !!")

@bot.command(name='meme')
async def meme(ctx):
    reddit_instance = praw.Reddit(client_id="-pSPiKAER-EyCsC8pdEfxg", client_secret="Q-Mf5eNG2O_tllof1rmkSgmr1ccEZw",
                                  user_agent="/u/Spectrum_py")
    sub_reddit = reddit_instance.subreddit("memes").new(limit=25)
    meme_list = []
    for memes in sub_reddit:
        meme_list.append(memes)
    index = random.randint(0, 25)
    orig_meme = meme_list[index]
    title_meme = orig_meme.title
    img_meme = orig_meme.url

    embed = discord.Embed(title=title_meme)
    embed.set_image(url=img_meme)

    await ctx.send(embed=embed)
    print("working")






@bot.command(name='uncle')
async def uncle(ctx):
    await ctx.send(file=discord.File("uncle.jpg"))

@bot.command(name="surprise")
async def surprise(ctx):
    rickroll_title = "**Guess what I have for you !!!**"
    await ctx.send(file=discord.File(r"C:\Users\Kavide\IRIS_BOT\surprise.mp4"),content=rickroll_title)

@bot.command(name="wish")
async def wishes(ctx,what_they_say):
    await ctx.send("Loading....")
    localtime_ref = time.localtime()
    localtime_ref = time.strftime('%H:%M:%S', localtime_ref)
    await ctx.send("now the time is "+str(localtime_ref))
    await ctx.send(what_they_say)
    if str(what_they_say).lower() == "good morning":
        if int(str(localtime_ref)[0:2]) in morning_time:
            await ctx.send("Hey there Good Morning .Hope you would have a great day ahead")
        elif int(str(localtime_ref)[0:2]) in afternoon_time:
            await ctx.send("Get up asap ....It is afternoon idiot get ready for your school")
        elif int(str(localtime_ref)[0:2]) in evening_time:
            await ctx.send("My god....after a long day of stress ,I guess you dropped your brain somewhere .Find it as you are already in a pathetic state coz it is evening now")
        elif int(str(localtime_ref)[0:2]) in night_time:
            await ctx.send("Think of it ,you are texting me in your dreams... Wake up now it is night and let me sleep")

    elif str(what_they_say).lower() == "good afternoon":
        if int(str(localtime_ref)[0:2]) in morning_time:
            await ctx.send("Why did you wake me up so soon retard it isnt afternoon yet ,now let me sleep")
        elif int(str(localtime_ref)[0:2]) in afternoon_time:
            await ctx.send("Good afternoon ,Hope you are having a great day")
        elif int(str(localtime_ref)[0:2]) in evening_time:
            await ctx.send("Yo I know you are exhausted by those online classes but hey wake up man it is evening now")
        elif int(str(localtime_ref)[0:2]) in night_time:
            await ctx.send("I know I know you are bored by those lectures but hey man its only been 5 minutes it is still afternoon. Wake up buddy")

    elif str(what_they_say).lower() == "good evening":
        if int(str(localtime_ref)[0:2]) in morning_time:
            await ctx.send("Stop trolling me I have a watch idiot.....It is evening now")
        elif int(str(localtime_ref)[0:2]) in afternoon_time:
            await ctx.send("It already time buddy pack your things up and better get going to you home before teacher gives you some assignments coz it is evening now")
        elif int(str(localtime_ref)[0:2]) in evening_time:
            await ctx.send("Good evening man ,how was your day")
        elif int(str(localtime_ref)[0:2]) in night_time:
            await ctx.send("You have been playing games for so long that you know do not know the time ...its already night go sleep now else you would be late for your school !!!")
    elif str(what_they_say).lower() == "good night":
        if int(str(localtime_ref)[0:2]) in morning_time:
            await ctx.send("Hey ,get ready for school it is morning now")
        elif int(str(localtime_ref)[0:2]) in afternoon_time:
            await ctx.send("Hey are you waking up ,it is already afternoon .Do you even have the idea of getting off your bed")
        elif int(str(localtime_ref)[0:2]) in evening_time:
            await ctx.send("No buddy not yet we still have time to sleep ,it is only evening now .Save your dreams")
        elif int(str(localtime_ref)[0:2]) in morning_time:
            await ctx.send("Good night big guy .Sweet dreams ......")
    elif str(what_they_say) == "good":
        await ctx.send("enter your wishes under quotes")
    else:
        await ctx.send("Enter a valid wish ......")

@bot.command(name="info")
async def info(ctx):
    await ctx.send("```Hello user ,thanks for reaching out .The commands to perform specific functions are listed down below :\n\n\t1. c!hello or c!hai : Wishes you back with a hai message\n\t2. c!who<pokemon hint> or c!poke<pokemon hint> : Helps you with searching a pokemon's name based on a hint given\n\tc!meme : Fetches you a meme\n\tc!wish\"<your_wish>\" : Returns the wholehearted greeting from the bot (or roast at certain circumstances)```")


@bot.command(name="start_count")
async def count(ctx,id,counts):
    try:
        count_channel = bot.get_channel(int(id))
        recent_count = await count_channel.fetch_message(count_channel.last_message_id)
        if counts<recent_count:
            await ctx.send("Sorry the counting has already been done")
        else:
            for i in range(recent_count,counts+1):
                await ctx.send(str(i))
    except:
        ctx.send("- Please enter the parameters : ")





@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if message.content == "c!hello" or message.content == "c!hai" or message.content == "c!Hai"  or message.content == "c!Hello":
        await message.channel.send("Hello "+message.author.name+" .How are you buddy !!!")

    if message.content.startswith("c!poke") or message.content.startswith("c!who"):
        p_list = str(message.content).split()
        p_list.remove(p_list[0])

        if True:
            hint = ""
            for i in p_list:
                hint += i
                if p_list[0] != hint:
                    hint += " "
            hint = hint.capitalize()
            maybe_list_1 = []
            maybe_list_2 = []
            for i in poke_names:
                if len(i) == len(hint):
                    maybe_list_1.append(i)
            for j in maybe_list_1:
                j = j.capitalize()
                for k in range(len(j) - 1):
                    if hint[k].isalpha():
                        if hint[k] != j[k]:
                            break
                else:
                    maybe_list_2.append(j)
        await message.channel.send("My guess are : " + str(maybe_list_2))


bot.run("OTE1MjU1NDUwMzgxOTc5NjU4.YaY8Dw.kn6DHjKeTqPDPOgkC-B7tokkSY0")