from turtle import*
class ArgumentNoneError(BaseException):
    pass
class NotInDictError(BaseException):
    pass
class ModeError(BaseException):
    pass
class ClearTextZhuyinError(BaseException):
    pass
class ClearTextEngError(BaseException):
    pass
class ClearTextNumError(BaseException):
    pass
def drawSqare(fill):
    if fill:
        begin_fill()
    for k in range(4):
        fd(size)
        rt(90)
    if fill:
        end_fill()
def drawCrypticText(drawList):
    for i in range(len(drawList)):
        for j in range(len(i)):
            if j==1:
                drawSqare(True)
            elif j==0:
                drawSqare(False)
            up()
            fd(size)
            down()
        up()
        rt(90)
        fd(size)
        rt(90)
        fd(size*2)
        rt(180)
        down()
def setWord(mode=None,clearText=None):
    if mode is None:
        raise ArgumentNoneError("Argument \"mode\" is None.")
    if clearText is None:
        raise ArgumentNoneError("Argument \"clearText\" is None.")
    if mode not in "123":
        raise ModeError("Argument \"mode\" can not identify.")
    if mode=="1":
        if clearText not in zhuyin:
            raise ClearTextZhuyinError(f"The word \"{clearText}\" not in the dict \"zhuyin\".")
        drawCrypticText(mode["M1Zhuyin"])
        drawCrypticText(zhuyin[clearText])
    elif mode=="2":
        if clearText not in eng:
            raise ClearTextEngError(f"The word \"{clearText}\" not in the dict \"eng\".")
        drawCrypticText(mode["M2Eng"])
        drawCrypticText(eng[clearText])
    elif mode=="3":
        if clearText not in num:
            raise ClearTextNumError(f"The word \"{clearText}\" not in the dict \"num\".")
        drawCrypticText(mode["M3Num"])
        drawCrypticText(num[clearText])
zhuyin={
    "ㄅ":[[1,0,0],[1,1,1],[0,1,1]],
    "ㄆ":[[1,0,0],[1,1,1],[0,1,0]],
    "ㄇ":[[1,1,1],[1,0,1],[1,0,1]],
    "ㄈ":[[1,1,1],[1,0,0],[1,1,1]],
    "ㄉ":[[1,0,0],[1,1,1],[1,0,1]],
    "ㄊ":[[0,1,0],[1,1,1],[1,1,1]],
    "ㄋ":[[1,1,0],[0,1,1],[0,0,1]],
    "ㄌ":[[1,0,1],[1,1,1],[1,0,1]],
    "ㄍ":[[1,0,0],[1,1,1],[0,1,1]],
    }
eng={
    "A":[[0,1,0],[1,1,1],[1,0,1]],
    
    }
num={
    "1":[[1,1,0],[0,1,0],[1,1,1]],
    
    }
mode={
    "M1Zhuyin":[[0,0,0],[1,0,0],[0,0,0]],
    "M2Eng":[[0,0,0],[0,1,0],[0,0,0]],
    "M3Num":[[0,0,0],[0,0,1],[0,0,0]]
    }
mode=input("mode=")
word=input("word=")
shape("turtle")
setWord(mode,word)
hideturtle()
