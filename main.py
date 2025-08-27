#function
import copy

from StickerClass import Sticker
from StickerPlaced import StickerPlaced
from dataPlayerScraping import scrapting
import colorama

def showWordOfSticker(listOfStickers):
    for sticker in listOfStickers:
        print(sticker.nameTag)


def researchStupid(lStickers,mapTest,searchedWord):
    for sIdx in range(len(lStickers)):
        for lIdx in range(len(lStickers[sIdx].nameTag)):
            lIdx2 = lIdx+1
            while lIdx2<=len(lStickers[sIdx].nameTag) and (lStickers[sIdx].nameTag[lIdx:lIdx2] in searchedWord) :
                infoStart = ""
                infoEnd = ""
                if lIdx==0:
                    infoStart = "**"
                if lIdx2==len(lStickers[sIdx].nameTag):
                    infoEnd = "**"
                if mapTest.get(infoStart+lStickers[sIdx].nameTag[lIdx:lIdx2]+infoEnd) is not None:
                    mapTest[infoStart+lStickers[sIdx].nameTag[lIdx:lIdx2]+infoEnd].append(sIdx)
                else :
                    mapTest[infoStart+lStickers[sIdx].nameTag[lIdx:lIdx2]+infoEnd] = [sIdx]
                lIdx2 += 1


def test(word,indexWord,mapTest,stickerUsed,indexDepth,nbPlaced,listMouvement):
    #if i got at the end of the word or placed 5 stickers
    if nbPlaced ==5 or indexWord==len(word):
        stickerShow(word,stickerUsed,indexDepth,nbPlaced,listMouvement)
        return
    else:
        # i got through all the possibles letters conbinations from the start of the remaining letters
        #
        # exemple if i only have lexi to do a will try (l,le,lex,lexi)
        #
        #print(word, indexWord, stickerUsed, indexDepth, nbPlaced, listMouvement)
        for wIdx in range(indexWord,len(word)):
            #since a can only do max 5 levels of stickers i need to see in which level it is
            #
            # here i get the X of the last placed sticker
            #
            indexLast=len(stickerUsed[indexDepth])-1
            #if i find a possible combinaison i will do different things by looking if the part of the sticker i want
            #touch the end or the start of the sticker word
            # if the part needed is not a the end or the start
            if  (mapTest.get(word[indexWord:wIdx + 1]) is not None and(
                    (indexLast == -1 or
                   stickerUsed[indexDepth][indexLast][len(stickerUsed[indexDepth][indexLast])-1]=="*"))):

                    if indexDepth==0:
                        stickerUsed2 = copy.deepcopy(stickerUsed)
                        stickerUsed2.insert(0,[word[indexWord:wIdx+1]])
                        listMouvement2=listMouvement[:]
                        listMouvement2.append(-1)
                        test(word, (indexWord + 1 + (wIdx - indexWord)), mapTest, stickerUsed2, 0, nbPlaced + 1,listMouvement2)
                    else:
                        stickerUsed2 = copy.deepcopy(stickerUsed)
                        stickerUsed2[indexDepth-1].append(word[indexWord:wIdx+1])
                        listMouvement2=copy.deepcopy(listMouvement)
                        listMouvement2.append(-1)
                        test(word, (indexWord +1 + (wIdx - indexWord)), mapTest, stickerUsed2, indexDepth-1, nbPlaced + 1,listMouvement2)

            if  (mapTest.get(word[indexWord:wIdx + 1] + "**") is not None and(
                   (indexLast == -1 or
                   stickerUsed[indexDepth][indexLast][len(stickerUsed[indexDepth][indexLast])-1]=="*"))):
                    if indexDepth==0:
                        stickerUsed2 = copy.deepcopy(stickerUsed)
                        stickerUsed2.insert(0,[word[indexWord:wIdx+1]+"**"])
                        listMouvement2=listMouvement[:]
                        listMouvement2.append(-1)
                        test(word, (indexWord + 1 + (wIdx - indexWord)), mapTest, stickerUsed2, 0, nbPlaced + 1,listMouvement2)
                    else:
                        stickerUsed2 = copy.deepcopy(stickerUsed)
                        stickerUsed2[indexDepth-1].append(word[indexWord:wIdx+1]+"**")
                        listMouvement2=copy.deepcopy(listMouvement)
                        listMouvement2.append(-1)
                        test(word, (indexWord + 1 +(wIdx - indexWord)), mapTest, stickerUsed2, indexDepth-1, nbPlaced + 1,listMouvement2)


            # if the part needed is at the start or if the part needed is the whole sticker
            if mapTest.get("**"+word[indexWord:wIdx + 1]) is not None:
                if indexLast == -1 or stickerUsed[indexDepth][indexLast][len(stickerUsed[indexDepth][indexLast])-1]=="*" :
                    stickerUsed2 = copy.deepcopy(stickerUsed)
                    stickerUsed2[indexDepth].append(("**"+word[indexWord:wIdx + 1]))
                    listMouvement2 = copy.deepcopy(listMouvement)
                    listMouvement2.append(0)
                    test(word, indexWord + 1 + (wIdx-indexWord), mapTest, stickerUsed2, indexDepth, nbPlaced+1, listMouvement2)
                else:
                    stickerUsed2 = copy.deepcopy(stickerUsed)
                    if indexDepth+1==len(stickerUsed):
                        stickerUsed2.append([("**"+word[indexWord:wIdx + 1])])
                    else:
                        stickerUsed2[indexDepth+1].append(("**"+word[indexWord:wIdx + 1]))
                    listMouvement2 = copy.deepcopy(listMouvement)
                    listMouvement2.append(1)
                    test(word, indexWord + 1 + (wIdx-indexWord), mapTest, stickerUsed2, indexDepth+1, nbPlaced+1, listMouvement2)




            if mapTest.get("**"+word[indexWord:wIdx + 1]+"**")is not None:
                if indexLast == -1 or stickerUsed[indexDepth][indexLast][len(stickerUsed[indexDepth][indexLast])-1]=="*" :
                    stickerUsed2 = copy.deepcopy(stickerUsed)
                    stickerUsed2[indexDepth].append(("**"+word[indexWord:wIdx + 1]+"**"))
                    listMouvement2 = copy.deepcopy(listMouvement)
                    listMouvement2.append(0)
                    test(word, indexWord + 1 + (wIdx-indexWord), mapTest, stickerUsed2, indexDepth, nbPlaced+1, listMouvement2)
                else:
                    stickerUsed2 = copy.deepcopy(stickerUsed)
                    if indexDepth+1==len(stickerUsed):
                        stickerUsed2.append([("**"+word[indexWord:wIdx + 1]+"**")])
                    else:
                        stickerUsed2[indexDepth+1].append(("**"+word[indexWord:wIdx + 1]+"**"))
                    listMouvement2 = copy.deepcopy(listMouvement)
                    listMouvement2.append(1)
                    test(word, indexWord + 1 + (wIdx-indexWord), mapTest, stickerUsed2, indexDepth+1, nbPlaced+1, listMouvement2)

def stickerShow(word,stickerUsed,indexDepth,nbPlaced,listMouvement):
    #print("***1")
    #print(stickerUsed,indexDepth)
    #print("***2")
    order=["" for i in range(len(listMouvement))]
    order2 =[]
    for index in range(len(listMouvement)-1,-1,-1):
        partWord = stickerUsed[indexDepth].pop()

        for indexOrder in range(len(order)):
            if indexOrder == indexDepth:
                if partWord[0]=="*" and partWord[len(partWord)-1]=="*" :
                    order[indexOrder] = colorama.Fore.GREEN+(partWord[2:len(partWord)-2] + order[indexOrder])
                elif partWord[0] == "*" :
                    order[indexOrder] = colorama.Fore.BLUE+(partWord[2:len(partWord)] + order[indexOrder])
                elif partWord[len(partWord) - 1] == "*":
                    order[indexOrder] = colorama.Fore.YELLOW+(partWord[0:len(partWord)-2] + order[indexOrder])
                else :
                    order[indexOrder] = colorama.Fore.RED+(partWord + order[indexOrder])

            else:


                if partWord[0]=="*" and partWord[len(partWord)-1]=="*" :
                    order[indexOrder] = colorama.Fore.BLACK+((len(partWord)-4)*".") + order[indexOrder]
                elif partWord[0] == "*" :
                    order[indexOrder] = colorama.Fore.BLACK+((len(partWord)-2)*".") + order[indexOrder]
                elif partWord[len(partWord) - 1] == "*":
                    order[indexOrder] = colorama.Fore.BLACK+((len(partWord)-2)*".") + order[indexOrder]
                else :
                    order[indexOrder] = colorama.Fore.BLACK+(len(partWord)*".") + order[indexOrder]

        order2.append(partWord)
        indexDepth -= listMouvement[index]

    if ((len(order2)==4 and ((order2[0][len(order2[0])-1]=="*") or (order2[-1][0]=="*"))) or
            (len(order2)==5 and ((order2[0][len(order2[0])-1]=="*") and (order2[-1][0]=="*"))) or
            (len(order2)<4)):

        print(colorama.Fore.YELLOW+"jaune est pour quand on utilise la fin du sticker")
        print(colorama.Fore.RED+"rouge est pour quand on utilise le milieu le sticker")
        print(colorama.Fore.GREEN+"vert est pour quand on utilise tout le sticker")
        print(colorama.Fore.BLUE+"bleu est pour quand on utilise le debut du sticker")
        for depthLevel in order:
            print(depthLevel)

        print("")
        print(colorama.Fore.WHITE+"si le premier est jaune ou rouge il va y avoir des lettres qui dépassent")
        print(colorama.Fore.WHITE+"si le dernier est blue ou rouge il va y avoir des lettres qui dépassent")
        print("")
        for partOfWord in order2:
            playerPartWord=colorama.Fore.WHITE+"Joueurs pour "+partOfWord+" :"
            playerIds=mapTest.get(partOfWord)
            for playerId in playerIds:
                playerPartWord+=colorama.Fore.WHITE+listOfStickers1[playerId].nameTag+",  "
            print(playerPartWord)
        print('__________________________________')




wordSearch = input(" mot a former ")
listOfStickers2 = scrapting()
global listOfStickers1
listOfStickers1=[]
for playerName in listOfStickers2:
    listOfStickers1.append(Sticker(playerName))


stickerUsed= [[]]
mapTest={}
test245=[]

researchStupid(listOfStickers1,mapTest,wordSearch)
print(mapTest)
test(wordSearch,0,mapTest,stickerUsed[:], 0,0,test245[:])
'''test with
stickerUsed[0].append(StickerPlaced("Tizian"))
stickerUsed[0].append(StickerPlaced("Obo"))
stickerUsed[0][0].placeSticker([0,5],0)
stickerUsed[0][1].placeSticker([0,1],6)'''