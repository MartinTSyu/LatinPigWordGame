#coding:utf-8

alphabet = raw_input("請輸入一個單詞: ")
string1 = list(alphabet)
#把alphabet轉化為list，便於後面拆分，移除，合併

for letter in string1:
    #遍歷單詞中的字母，找到第一個輔音音素字母
    if letter.lower() in "aeiou":
        #當前字母是元音，pass
        pass
    else:
        string1.remove(letter)
        #當前字母是輔音，將其從原list中移除
        string2 = ''.join(string1)
        #將移除第一個輔音的list合併為string
        string3 = string2 + '-' + letter + 'ay'
        #將一個輔音字母添加到後綴中'-Xay'
        print string3
        break
