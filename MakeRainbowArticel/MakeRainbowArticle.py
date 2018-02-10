
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
            to_set='[size=25px][color=#ffc]'+chars[0]+'[/color][/size]'
            chars[0]=''
        rest=''.join(chars)
        to_set+='[size=20px]'+rest+" "+'[/size]'
        s_lis[nr]=to_set
    print(s_lis)
    return ''.join(s_lis)


def file_changer():
    with open('file.txt') as f:
        with open('out.txt','w+') as w:
            for line in f:
                if list(line)[0]=='|':
                    w.write(first_letter_yellow_title(line)+"\n"+"\n")
                else:
                    w.write(first_letter_slightly_different(line)+"\n"+"\n")

file_changer()
s="Die Mine der Könige"
#print(first_letter_yellow(s))