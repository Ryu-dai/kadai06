import random

print('おみくじを引きます')

omikuji = random.randint(0,6)

if omikuji == 0:
    print('大吉です　最高！')

if omikuji == 1:
    print('吉です　いいね！')

if omikuji == 2:
    print('中吉です　いいじゃん！')

if omikuji == 3:
    print('小吉です　悪くない！')

if omikuji == 4:
    print('末吉です　全然大丈夫！')

if omikuji == 5:
    print('凶です　いいことある！')

if omikuji == 6:
    print('大凶です　強運（凶運）だぜ！')