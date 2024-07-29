from itertools import permutations
def queen_basic(n):
    answers=[]
    def is_safe(ans,col):
        for i,c in enumerate(ans):
            if len(ans)-i==abs(c-col):
                return False
        return True
    def sub(ans,n):
        if len(ans)==n:
            answers.append(ans)
        else:
            for col in range(n):
                if col not in ans and is_safe(ans,col):
                    sub(ans+(col,),n)
    sub((),n)
    return answers
def queen_hettingers(n):
    answers=[]
    cols=range(n)
    for ans in permutations(cols):
        if(n==len(set([ans[i]+i for i in cols]))==len(set([ans[i]-i for i in cols]))):
            answers.append(ans)
    return answers
def queen_howell(n):
    answers=[()]
    def under_attack(col,ans):
        return(col in ans or any(abs(col-x)==len(ans)i for i,x in enumerate(ans)))
    for row in range(n):
        answers=[ans+(col,)for ans in answers for col in range(n)if not under_attack(col,ans)]
    return answers
def queen_hettingers_gf(n):
    cols=range(n)
    for ans in permutations(cols):
        if(n==len(set(ans[i]+i for i in cols))==len(set(ans[i]-i for i in cols))):
            yield ans