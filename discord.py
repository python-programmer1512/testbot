import discord
client=discord.Client()
def codeup(ex):
    if len(ex)==1:
        return "https://codeup.kr"
    else:
        if ex[1]=="profile"or ex[1]=="프로필":
            if len(ex)==3:
                q="https://codeup.kr/userinfo.php?user="+ex[2]
                return q
        elif ex[1]=="rank"or ex[1]=="랭크"or ex[1]=="순위":
            if len(ex)==2:
               return "https://codeup.kr/ranklist.php"
            else:
                page="https://codeup.kr/ranklist.php?start="+str((int(ex[2])-1)*50)
                return page
        else:
            q="https://codeup.kr/problem.php?id="+ex[1]
            return q

def boj(ex):
    if len(ex)==1:return "https://www.acmicpc.net/"
    else:
        if ex[1]=="profile"or ex[1]=="프로필":
            if len(ex)==3:
                q="https://www.acmicpc.net/user/"+ex[2]
                return q
        elif ex[1]=="rank"or ex[1]=="랭크"or ex[1]=="순위":
            if len(ex)==2:
                return "https://www.acmicpc.net/ranklist"
            else:
                page="https://www.acmicpc.net/ranklist/"+ex[2]
                return page
        else:
            q="https://www.acmicpc.net/problem/"+ex[1]
            return q

def solved(ex):
    if len(ex)==1:return "https://solved.ac"
    else:
        if ex[1]=="profile"or ex[1]=="프로필":
            if len(ex)==3:
                q="https://solved.ac/profile/"+ex[2]
                return q
        else:
            if(len(ex)==3 or len(ex)==4)and (ex[1]=="rank"or ex[1]=="랭크"or ex[1]=="순위"):
                if ex[2]=="ti"or ex[2]=="티어":
                    if len(ex)==3:page="https://solved.ac/ranking/tier"
                    else:page="https://solved.ac/ranking/tier?page="+ex[3]
                if ex[2]=="cl"or ex[2]=="클래스":
                    if len(ex)==3:page="https://solved.ac/ranking/class"
                    else:page="https://solved.ac/ranking/class?page="+ex[3]
                if ex[2]=="co"or ex[2]=="기여도":
                    if len(ex)==3:page="https://solved.ac/ranking/contribution"
                    else:page="https://solved.ac/ranking/contribution?page="+ex[3]
                return page
def deln(ip):
    for i in range(len(ip)):
        if ip[i]=="건"or ip[i]=="충"or ip[i]=="gun"or ip[i]=="고"or ip[i]=="원"or ip[i]=="규"or ip[i]=="추ᇰ"or ip[i]=="ㄱㅓㄴ"or ip[i]=="거ᇈ":return False
    return True

@client.event
async def on_ready():
    print("Start {0.user}".format(client))
system=0
@client.event
async def on_message(message):
    global system
    if message.author==client.user:return
    if message.content.startswith("~good"):q="good";await message.channel.send(q)

    if message.content.startswith("~마자효"):q="마자효\n1104";await message.channel.send(q)
    
    if message.content.startswith("~system"):
        userip=str(message.author).split("#")
        if not deln(userip[0]):
            msg=message.content[8:].split()
            if len(msg)==1:
                if msg[0]=="on":system=1
                elif msg[0]=="off":system=0
                else:await message.channel.send("please say on or off")
            if msg[0]=="on"or msg[0]=="off":await message.channel.send("on" if system==1 else "off")
        else:
            await message.channel.send("당신은 관리자가 아닙니다")

    if message.content.startswith("~fan"):
        msg=message.content[5:];msg+="님 팬이에요";await message.channel.send(msg)

    if message.content.startswith("~cute"):
        #await message.channel.send("누군가 때문에 지움 ㅅㄱ")
        msg=str(message.content[6:])
        if system==0:
            if deln(msg):msg+="님 귀여워요~";await message.channel.send(msg)
            else:await message.channel.send("그 이름은 금지 되어있습니다")
        else:
            msg+="님 귀여워요~";await message.channel.send(msg)

    if message.content.startswith("~help"):
        ms=""
        ms+="팬이에요 : ~fan nickname\n\n"
        ms+="귀여워요:~cute nickname\n\ngood:~good\n\ngyman:~gyman nickname\n\ngod:~god nickname\n\n"
        ms+="지원하는 사이트:baekjoon(boj)(백준),codeup(코드업),solved.ac,koistudy(코이스터디),codeforces(코포,코드포스)\n\n"
        ms+="ps site:~ps sitename\n\npssite number:~ps sitename number\n\n"
        ms+="ps site profile:~ps sitename profile name\n\n"
        ms+="ps site rank:~ps sitename rank pagenumber\n\n"
        ms+="solved.ac rank tier:~ps solved.ac rank (ti or 티어) pagenumber\n\n"
        ms+="solved.ac rank class:~ps solved.ac rank (cl or 클래스) pagenumber\n\n"
        ms+="solved.ac rank contribution(기여도):~ps solved.ac rank (co or 기여도) pagenumber\n\n"
        ms+="ps codeforces rank korea:~ps codeforces rank korea pagenumber\n\n"
        await message.channel.send(message.channel,embed=discord.Embed(title="test bot help",description=ms,color=0x62c1cc))
        
    if message.content.startswith("~gyman"):
        #await message.channel.send("별게 다 뚫리네ㅡㅡ")
        msg=str(message.content[7:])
        if system==0:
            if deln(msg):
                msg+="님 기만";await message.channel.send(msg)
                embed=discord.Embed(timestamp=message.created_at,colour=discord.Colour.red(),title="기만",description="")
                embed.set_image(url="https://drive.google.com/file/d/1Dfb5NZZ7pZ4d9Hfv2YJRK9Xj1zDieR2_/view?usp=sharing")
                embed.set_footer(text=message.author,icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
            else:await message.channel.send("기만이 아닙니다")
        else:
            msg+="님 기만";#await message.channel.send(msg)
            embed=discord.Embed(timestamp=massage.created_at,colour=discord.Colour.red(),title="기만",description="")
            embed.set_image(url="https://drive.google.com/file/d/1Dfb5NZZ7pZ4d9Hfv2YJRK9Xj1zDieR2_/view?usp=sharing")
            embed.set_footer(text=message.author,icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)
        
    if message.content.startswith("~god"):
        msg=str(message.content[5:])
        if system==0:
            if deln(msg):msg+="님 갓";await message.channel.send(msg)
            else:await message.channel.send("갓이 아닙니다")
        else:
            msg+="님 갓";await message.channel.send(msg)
        
    if message.content.startswith("~ps"):
        ex=message.content[4:].split()
        if len(ex)!=0:
            if ex[0]=="codeup"or ex[0]=="코드업":
                await message.channel.send(codeup(ex))
            elif ex[0]=="boj"or ex[0]=="baekjoon"or ex[0]=="백준":
                await message.channel.send(boj(ex))
            elif ex[0]=="solved.ac":
                await message.channel.send(solved(ex))
            elif ex[0]=="koistudy"or ex[0]=="코이스터디":
                if len(ex)==1:await message.channel.send("http://koistudy.net/")
                else:
                    if ex[1]=="rank"or ex[1]=="랭크"or ex[1]=="순위":
                        if len(ex)==2:await message.channel.send("http://koistudy.net/?mid=rank")
                        else:
                            page="http://koistudy.net/?mid=rank&TH=&SEARCH=&pg="+str(int(ex[2])-1)+"&WORD="
                            await message.channel.send(page)
                    elif ex[1]=="profile"or ex[1]=="프로필":
                        if len(ex)==3:
                            q="http://koistudy.net/?mid=view_prob&id="+ex[2]
                            await message.channel.send(q)
            elif ex[0]=="codeforces"or ex[0]=="코포"or ex[0]=="코드포스":
                if len(ex)==1:await message.channel.send("https://codeforces.com/")
                else:
                    if ex[1]=="profile"or ex[1]=="프로필":
                        if len(ex)==3:
                            q="https://codeforces.com/profile/"+ex[2]
                            await message.channel.send(q)
                    if ex[1]=="rank"or ex[1]=="랭크"or ex[1]=="순위":
                        if len(ex)>=3 and (ex[2]=="korea"or ex[2]=="한국"):
                            if len(ex)==3:await message.channel.send("https://codeforces.com/ratings/country/South%20Korea")
                            elif len(ex)==4:
                                page="https://codeforces.com/ratings/country/South%20Korea/page/"+ex[3]
                                await message.channel.send(page)
                        elif len(ex)==2:await message.channel.send("https://codeforces.com/ratings")
                        else:
                            page="https://codeforces.com/ratings/page/"+ex[2]
                            await message.channel.send(page)
                
client.run("Nzg1NzkxNzY3ODMyMDM1MzQ4.X88_nA.qG_-XJmtyX24eeelYh8GmBQquWc")
