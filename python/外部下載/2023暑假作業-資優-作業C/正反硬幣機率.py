import random

#config
both_up = 2 #兩正
both_down = 3 #兩反
ouod = 3 #一正一反

total = 100000 #跑幾次
log_checkpoints = 8 #記錄幾次
#config_end

p, q = 0, 0
coins = [(1,1)for _ in range(both_up)] + [(0,0)for _ in range(both_down)] + [(1,0)for _ in range(ouod)]
total_coins = both_up + both_down + ouod
checkpoint_cnt = 1
checkpoint = 1 / log_checkpoints

for i in range(total):
    if i / total > checkpoint:
        print("Checkpoint {} ({}% complete), P is {}, Q is {}, Q/P is {}".format(checkpoint_cnt, round(i/total * 100, 2), p, q, q/p))  
        checkpoint_cnt += 1
        checkpoint = (1/log_checkpoints) * checkpoint_cnt
    get_side = random.randint(0,total_coins*2 - 1)
    side = coins[get_side//2][get_side%2]
    if side == 1:
        p += 1
        if coins[get_side//2][abs(get_side%2-1)] == 1:
            q += 1

print("P is {}, Q is {}, Q/P is {}".format(p, q, q/p))