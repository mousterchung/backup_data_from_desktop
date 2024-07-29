import random as R
class Card():
    RANKS=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS=["♣️","♦️","♥️","♠️"]
    def __init__(self,rank,suit,face_up=True):
        self.rank=rank
        self.suit=suit
        self.is_face_up=face_up
    def __str__(self):
        if self.is_face_up:
            rep=self.suit+self.rank
        else:
            rep="XX"
        return rep
    def pic_order(self):
        if self.rank=="A":
            FaceNum=1
        elif self.rank=="J":
            FaceNum=11
        elif self.rank=="Q":
            FaceNum=12
        elif self.rank=="K":
            FaceNum=13
        else:
            FaceNum=int(self.rank)
        if self.suit=="♣️":
            Suit=1
        elif self.suit=="♦️":
            Suit=2
        elif self.suit=="♥️":
            Suit=3
        else:
            Suit=4
        return (Suit-1)*13+FaceNum
    def flip(self):
        self.is_face_up=not self.is_face_up
class Hand():
    def __init__(self):
        self.cards=[]
    def __str__(self):
        if self.cards:
            rep=""
            for card in self.cards:
                rep+=str(card)+"\t"
        return rep
        rep="無牌"
    def clear(self):
        self.cards=[]
    def add(self,card):
        self.cards.append(card)
    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)
class Poke(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank,suit))
    def shuffle(self):
        R.shuffle(self.cards)
    def deal(self,hands,per_hand=13):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card=self.cards[0]
                    self.give(top_card,hand)
                else:
                    print("牌已發完!")
if __name__=="__main__":
    players=[Hand(),Hand(),Hand(),Hand()]
    poke1=Poke()
    poke1.populate()
    poke1.shuffle()
    poke1.deal(players,13)
    n=1
    for hand in players:
        print("牌手",n,end=":")
        print(hand)
        n+=1
