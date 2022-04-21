from my_task import minus

for i in range(10000):
    minus.delay(i, i)
    print(i)