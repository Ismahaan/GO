from Set import Set
class Stone:  
    def __init__(self,posx,posy,board,color):
        self.posx = posx
        self.posy = posy
        self.color = color
        self.board = board

        initFreedom = []
        colorCount = 0

        sameColor = []
        
        if posx != 0:
            initFreedom.append(board.printBoard[posx-1][posy])
            if board.playBoard[posx-1][posy] != '0':
                if self.color == board.playBoard[posx-1][posy].color:
                    sameColor.append(board.playBoard[posx-1][posy])
        if posx != 8:
            initFreedom.append(board.printBoard[posx+1][posy])
            if board.playBoard[posx+1][posy] != '0':
                if self.color == board.playBoard[posx+1][posy].color:
                    sameColor.append(board.playBoard[posx+1][posy])
        if posy != 0:
            initFreedom.append(board.printBoard[posx][posy-1])
            if board.playBoard[posx][posy-1] != '0':
                if self.color == board.playBoard[posx][posy-1].color:
                    sameColor.append(board.playBoard[posx][posy-1])
        if posy != 8:
            initFreedom.append(board.printBoard[posx][posy+1])
            if board.playBoard[posx][posy+1] != '0':
                if self.color == board.playBoard[posx][posy+1].color:
                    sameColor.append(board.playBoard[posx][posy+1])

        while 'bl' in initFreedom: initFreedom.remove('bl')
        while 'wh' in initFreedom: initFreedom.remove('wh')

        if color == 'white': 
            board.printBoard[posx][posy] = 'wh'    
        else:
            board.printBoard[posx][posy] = 'bl'
        board.playBoard[posx][posy]=self

        if sameColor == []:
            Set(self,initFreedom)
            for set in board.whiteSet:
                print(board.emptyBoard[posx][posy])
                if board.emptyBoard[posx][posy] in set.freedomList:
                    set.freedomList.remove(board.emptyBoard[posx][posy])
            for set in board.blackSet:
                if board.emptyBoard[posx][posy] in set.freedomList: 
                    set.freedomList.remove(board.emptyBoard[posx][posy])
        elif self.color == 'white':
            firstSet = None
            for stoneList in sameColor:
                for set in board.whiteSet:
                    for stoneinSet in set.stoneList:
                        if stoneList == stoneinSet and firstSet == None:
                            set.stoneList.append(self)
                            set.freedomList.extend(initFreedom)
                            set.freedomList = list(dict.fromkeys(set.freedomList))
                            firstSet = set
                        elif stoneList == stoneinSet:
                            firstSet.stoneList.extend(set.stoneList)
                            firstSet.freedomList.extend(set.freedomList)
                            firstSet.freedomList = list(dict.fromkeys(firstSet.freedomList))
                            board.whiteSet.remove(set)
                    if board.emptyBoard[posx][posy] in set.freedomList: 
                        set.freedomList.remove(board.emptyBoard[posx][posy])
                for set in board.blackSet:
                    if board.emptyBoard[posx][posy] in set.freedomList: 
                        set.freedomList.remove(board.emptyBoard[posx][posy])
        elif self.color == 'black':
            firstSet = None
            for stoneList in sameColor:
                for set in board.blackSet:
                    for stoneinSet in set.stoneList:
                        if stoneList == stoneinSet and firstSet == None:
                            set.stoneList.append(self)
                            set.freedomList.extend(initFreedom)
                            set.freedomList = list(dict.fromkeys(set.freedomList))
                            firstSet = set
                        elif stoneList == stoneinSet:
                            firstSet.stoneList.extend(set.stoneList)
                            firstSet.freedomList.extend(set.freedomList)
                            firstSet.freedomList = list(dict.fromkeys(firstSet.freedomList))
                            board.blackSet.remove(set)
                    if board.emptyBoard[posx][posy] in set.freedomList: 
                        set.freedomList.remove(board.emptyBoard[posx][posy])
                for set in board.whiteSet:
                    if board.emptyBoard[posx][posy] in set.freedomList: 
                        set.freedomList.remove(board.emptyBoard[posx][posy])

        if board.whiteSet != []:
            print('white' + str(board.whiteSet[0].freedomList))
        print('black' + str(board.blackSet[0].freedomList))