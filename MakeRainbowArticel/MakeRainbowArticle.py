
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

def first_letter_yellow_title(s):
    s_lis=s.split()
    s_lis[0]=''.join(list(s_lis[0])[1:])
    for nr,i in enumerate(s_lis):
        chars=list(i)
        to_set=''
        if chars[0].isupper():
            to_set='[size=70px][color=#f00]'+chars[0]+'[/color][/size]'
            print(to_set)
            chars[0]=''
        print(chars)
        rest=''.join(chars)
        to_set+='[size=35px][color=#fff]'+rest+" "+'[/color][/size]'
        s_lis[nr]=to_set
    print(s_lis)
    return '[center][rr][b]'+''.join(s_lis)+'[/b][/rr][/center]'

def first_letter_slightly_different_normal(s):
    s_lis=s.split()
    for nr,i in enumerate(s_lis):
        chars=list(i)
        to_set=''
        if chars[0].isupper():
            to_set='[size=25px]'+chars[0]+'[/size]'
            chars[0]=''
        rest=''.join(chars)
        to_set+='[size=20px]'+rest+" "+'[/size]'
        s_lis[nr]=to_set
    return "[center]"+''.join(s_lis)+"[/center]"

def make_Image(s):
    return '[center][img]'+s+'[/img][/center]\n'


def file_changer():
    with open('file.txt') as f:
        with open('out.txt','w+') as w:
            for line in f:
                if list(line)[0]=='h' and list(line)[1]=='t':
                    w.write(make_Image(line))
                elif list(line)[0]=='|':
                    w.write(first_letter_yellow_title(line)+"\n"+"\n")
                else:
                    w.write(first_letter_slightly_different_normal(line)+"\n"+"\n")
            #w.write('[center][rr]'+'[size=70px]Powered by the [color=#f00]S[/color]wiss [color=#f00]G[/color]uards[/size][/rr][/center]'+"\n")
            #w.write('[center][url=http://rivalregions.com/#slide/party/87981][img]http://static.rivalregions.com/static/parties/981/87981_1519158044_big.png[/img][/url][/center]'+"\n")
            #w.write('[center][rr][size=30px]http://rivalregions.com/#slide/party/87981[/size][/rr][/center]'+"\n")
            w.write('[center][rr][b][size=70px][color=#f00]K[/color][/size][size=35px][color=#fff]ings [/color][/size][size=70px][color=#f00]O[/color][/size][size=35px][color=#fff]re [/color][/size][/b][/rr][/center][center][url= http://m.rivalregions.com/#factory/index/27679][img]https://media.giphy.com/media/39uiEJ9bEXgL03H1oN/giphy.gif[/img][/url][/center]'+"\n")
            w.write('[center][rr][size=30px]http://rivalregions.com/#factory/index/27679[/size][/rr][/center]'+"\n")

file_changer()
s="Die Mine der Könige"
#print(first_letter_yellow(s))