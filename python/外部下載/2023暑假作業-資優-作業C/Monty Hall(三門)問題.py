import random

total = 1000   #實驗次數
success = 0

for i in range(1000):
    doors = [0,0,0]   
    doors[random.randint(0,2)] = 1

    selection = random.randint(0,2)
    
    if doors[selection] == 0:
        for j in range(3):
            if j != selection and doors[j] != 1: opened = j
        for j in range(3):
            if j != opened and j != selection: final = j
        if doors[final] == 1: success += 1
        continue
    else:
        not_sel = [0,1,2]
        not_sel.remove(selection)
        opened = not_sel[random.randint(0,1)]
        for j in range(3):
            if j != opened and j != selection: final = j
        if doors[final] == 1: success += 1
        continue

print("Out of {} tries, {} tries got the car".format(total, success))