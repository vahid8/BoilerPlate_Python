from my_task import add

for i in range(10000):
    add.delay(i,i)
    print(i)