import operator as OP
import sys
ops={
    '+':OP.add,
    '-':OP.sub,
    '*':OP.mul,
    '/':OP.floordiv
}
def cal_tree(tree):
    if type(tree)==int:
        return tree
    else:
        return cal_forest(tree[1:],tree[0])
def cal_forest(forest,op):
    if len(forest)==2:
        return ops[op](cal_tree(forest[0]),cal_tree(forest[1]))
    else:
        hsr=cal_forest(forest[:-1],op)
        return ops[op](hsr,cal_tree(forest[-1]))
print('ex.')
print("tree_a=['-',6,2]")
print("tree_b=['/',10,2]")
print("tree_c=['+',3,tree_a,tree_b]")
print("tree_d=['-',5,2,1]")
print("tree_e=['*',tree_d,tree_c]")
print("cal_tree(tree_e)")
print(cal_tree(eval(input())))
