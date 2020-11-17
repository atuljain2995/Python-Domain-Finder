# regex imported
import re

# country domain listed
myInput = "ac ad ae af ag ai al am an ao aq ar as at au aw ax az ba bb bd be bf bg bh bi bj bl bm bn bo br bq bs bt bv bw by bz ca cc cd cf cg ch ci ck cl cm cn co cr cs cu cv cw cx cy cz dd de dj dk dm do dz ec ee eg eh er es et eu fi fj fk fm fo fr ga gb gd ge gf gg gh gi gl gm gn gp gq gr gs gt gu gw gy hk hm hn hr ht hu id ie il im in io iq ir is it je jm jo jp ke kg kh ki km kn kp kr kw ky kz la lb lc li lk lr ls lt lu lv ly ma mc md me mf mg mh mk ml mm mn mo mp mq mr ms mt mu mv mw mx my mz na nc ne nf ng ni nl no np nr nu nz om pa pe pf pg ph pk pl pm pn pr ps pt pw py qa re ro rs ru rw sa sb sc sd se sg sh si sj sk sl sm sn so sr ss st su sv sx sy sz tc td tf tg th tj tk tl tm tn to tp tr tt tv tw tz ua ug uk um us uy uz va vc ve vg vi vn vu wf ws ye yt yu za zm zr zw"

#List create by spliting myInput string with space
myList = myInput.split(" ")


#Taking user input for phrase
userInputString = input("{}Enter a phrase, and we'll try to find some URLs that matche: " .format('\n')).lower()

#Using regex substitution to remove whitespace and special characters
updatedUserInput = re.sub('[^A-Za-z0-9]+','',userInputString)

# print(updatedUserInput)

presentLastTwo = ''
userInputLength = len(updatedUserInput)

while( userInputLength > 1 ):
    currentDomain = updatedUserInput[userInputLength-2:userInputLength]
    if(userInputLength == len(updatedUserInput)):
        leftOverPath = ''
    else:
        leftOverPath = updatedUserInput[userInputLength+1:]
    if currentDomain in myList:
        print(updatedUserInput[:userInputLength-2]+"."+currentDomain+"/"+leftOverPath)
        userInputLength -= 1
    else:
        userInputLength -= 1


