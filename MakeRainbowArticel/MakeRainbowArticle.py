
def to_rainbow(s):
    s_lis=list(s)
    for nr,i in enumerate(s_lis):
        to_set=nr%7
        if to_set==0:
            i="[color=#90d]"+i+"[/color]"
            s_lis[nr]=i
        if to_set==1:
            i="[color=#705]"+i+"[/color]"
            s_lis[nr]=i
        if to_set==2:
            i="[color=#00f]"+i+"[/color]"
            s_lis[nr]=i
        if to_set==3:
            i="[color=#0f0]"+i+"[/color]"
            s_lis[nr]=i
        if to_set==4:
            i="[color=#ff0]"+i+"[/color]"
            s_lis[nr]=i
        if to_set==5:
            i="[color=#f70]"+i+"[/color]"
            s_lis[nr]=i
        if to_set==6:
            i="[color=#f00]"+i+"[/color]"
            s_lis[nr]=i

    return ''.join(s_lis)

def to_black_white(s):
    s_lis=list(s)
    for nr,i in enumerate(s_lis):
        to_set=nr%7
        if to_set==0:
            i="[color=#fff]"+i+"[/color]"
            s_lis[nr]=i
        if to_set==1:
            i="[color=#ddd]"+i+"[/color]"
            s_lis[nr]=i
        if to_set==2:
            i="[color=#aaa]"+i+"[/color]"
            s_lis[nr]=i
        if to_set==3:
            i="[color=#888]"+i+"[/color]"
            s_lis[nr]=i
        if to_set==4:
            i="[color=#666]"+i+"[/color]"
            s_lis[nr]=i
        if to_set==5:
            i="[color=#444]"+i+"[/color]"
            s_lis[nr]=i
        if to_set==6:
            i="[color=222]"+i+"[/color]"
            s_lis[nr]=i

    return ''.join(s_lis)

def to_red_white(s):
    s_lis=list(s)
    for nr,i in enumerate(s_lis):
        to_set=nr%2
        if to_set==0:
            i="[color=#f00]"+i+"[/color]"
            s_lis[nr]=i
    return ''.join(s_lis)

def first_letter_yellow(s):
    s_lis=s.split()
    for nr,i in enumerate(s_lis):
        chars=list(i)
        to_set=''
        if chars[0].isupper():
            to_set='[size=25px][color=#fc0]'+chars[0]+'[/color][/size]'
            print(to_set)
            chars[0]=''
        print(chars)
        rest=''.join(chars)
        to_set+='[size=20px][color=#ffe]'+rest+" "+'[/color][/size]'
        s_lis[nr]=to_set
    print(s_lis)
    return ''.join(s_lis)

def first_letter_yellow_title(s):
    s_lis=s.split()
    s_lis[0]=''.join(list(s_lis[0])[1:])
    for nr,i in enumerate(s_lis):
        chars=list(i)
        to_set=''
        if chars[0].isupper():
            to_set='[size=50px][color=#fc0]'+chars[0]+'[/color][/size]'
            print(to_set)
            chars[0]=''
        print(chars)
        rest=''.join(chars)
        to_set+='[size=30px][color=#ffc]'+rest+" "+'[/color][/size]'
        s_lis[nr]=to_set
    print(s_lis)
    return '[rr][b]'+''.join(s_lis)+'[/b][/rr]'

def first_letter_slightly_different(s):
    s_lis=s.split()
    for nr,i in enumerate(s_lis):
        chars=list(i)
        to_set=''
        if chars[0].isupper():
            to_set='[size=25px]'+chars[0]+'[/color][/size]'
            chars[0]=''
        rest=''.join(chars)
        to_set+='[size=20px]'+rest+" "+'[/size]'
        s_lis[nr]=to_set
    print(s_lis)
    return ''.join(s_lis)

def first_letter_red_title(s,only_word=False):
    s_lis=s.split()
    if only_word:
        s_lis[0]=''.join(list(s_lis[0]))
    else:
        s_lis[0]=''.join(list(s_lis[0])[1:])
    for nr,i in enumerate(s_lis):
        chars=list(i)
        to_set=''
        if chars[0].isupper():
            to_set='[size=70px][color=#f00]'+chars[0]+'[/color][/size]'
            print(to_set)
            chars[0]=''
        rest=''.join(chars)
        to_set+='[size=35px][color=#fff]'+rest+" "+'[/color][/size]'
        s_lis[nr]=to_set
    if(only_word):
        return '[rr][b]' + ''.join(s_lis) + '[/b][/rr]'
    else:
        return '[center][rr][b]'+''.join(s_lis)+'[/b][/rr][/center]'

def first_letter_slightly_different_normal(s):
    s_lis=s.split()
    for nr,i in enumerate(s_lis):
        chars=list(i)
        to_set=u''
        if chars[0].isupper():
            to_set=u'[size=22px]'+chars[0]+'[/size]'
            chars[0]=u''
        rest=u''.join(chars)
        to_set+=u'[size=18px]'+rest+" "+'[/size]'
        s_lis[nr]=to_set
    return u"[center]"+''.join(s_lis)+u"[/center]"
def make_vote(s):
    pos_votes=s.split(',')
    to_append=u'\n[center][vote]'+first_letter_red_title(pos_votes[0][1:],only_word=True)+"[/vote]\n \n \n \n \n \n \n\n"
    for i in pos_votes[1:]:
        to_append+=u'[v]'+first_letter_red_title(i,only_word=True)+"[/v]\n \n \n \n \n \n \n\n"
    to_append+=u"[/center]\n"
    return to_append

def make_Image(s):
    return '[center][img]'+s+'[/img][/center]\n'
def makeLineSpacer():
    #return '[center][img]https://i.imgur.com/T7sMBze.png[/img][/center]'
    return '[center][img]http://andyhotel.co/wp-content/uploads/2017/10/divider.png[/img][/center]'
def bottomSpacer():
    return '[center][img]https://cdn.pbrd.co/images/HE9LsNJt.png[/img][/center]'
def topSpacer():
    return '[center][img]https://cdn.pbrd.co/images/HE9L4k5.png[/img][/center]'
def lineSpacer():
    return '[center][img]https://cdn.pbrd.co/images/HE9LhsC.png[/img][/center]'
def articleEnder():
    return '[center][img]https://cdn.pbrd.co/images/HE9M86B.png[/img][/center]'

def holySign():
    return '[center][img]https://cdn.pbrd.co/images/HE9KCHt.png[/img][/center]'

def file_changer():
    with open('file.txt',encoding='utf-8') as f:
        with open('out.txt','w+',encoding="utf-8") as w:
            w.write(lineSpacer())

            w.write(topSpacer())
            for line in f:
                print(line)
                if list(line)[0]=='h' and list(line)[1]=='t':
                    w.write(make_Image(line))
                elif list(line)[0]=='&':
                    w.write(makeLineSpacer())
                elif list(line)[0]=='|':
                    w.write(first_letter_red_title(line) + "\n" + "\n")
                elif  list(line)[0]=='$':
                    w.write(make_vote(line)+"\n")
                else:
                    w.write(first_letter_slightly_different_normal(line)+"\n"+"\n")

            #w.write('[center][rr]'+'[size=70px]Powered by the [color=#f00]S[/color]wiss [color=#f00]G[/color]uards[/size][/rr][/center]'+"\n")
            #w.write('[center][url=http://rivalregions.com/#slide/party/87981][img]http://static.rivalregions.com/static/parties/981/87981_1519158044_big.png[/img][/url][/center]'+"\n")
            #w.write('[center][rr][size=30px]http://rivalregions.com/#slide/party/87981[/size][/rr][/center]'+"\n")
            #w.write('[center][rr][b][size=70px][color=#f00]K[/color][/size][size=35px][color=#fff]ings [/color][/size][size=70px][color=#f00]O[/color][/size][size=35px][color=#fff]re [/color][/size][/b][/rr][/center][center][url= http://m.rivalregions.com/#factory/index/27679][img]https://media.giphy.com/media/39uiEJ9bEXgL03H1oN/giphy.gif[/img][/url][/center]'+"\n")
            #w.write('[center][rr][size=30px]http://rivalregions.com/#factory/index/27679[/size][/rr][/center]'+"\n")
            w.write(articleEnder())
            w.write(bottomSpacer())
            w.write(lineSpacer())


file_changer()
s="Die Mine der Könige"
#print(first_letter_yellow(s))