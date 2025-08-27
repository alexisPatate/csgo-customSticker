from StickerClass import Sticker

class StickerPlaced(object):
    def __init__(self, playerNameTag):
        self.nameTag = playerNameTag
        #if i do some scraping i could get all thz data about each sticker
        # and recommend some craft if their are from the same major
        self.type = ""
        self.image = ""
        self.link = "link to Sticker"
        self.major = ""
        self.nameTag = playerNameTag
        self.sliceUsed=[0,0]
        self.startPlacementSlice=0
        self.flushEnd=False
        self.flushStart=False
        self.order=0

    def placeSticker(self, slice , placement):
        self.sliceUsed = slice
        self.startPlacementSlice = placement

