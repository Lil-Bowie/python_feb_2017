num = 1
for num in range(1,1000):
    print num
#start my counter

value = 5
for value in range(5,1000000) :
    if value % 5 == 0:
        print value
#print the multiples of 5

def fSum():
    i = 0
    arr = [1,2,5,10,255,3]
    i = sum(arr)
    print i
fSum()
#take the sum of List.

def fAvg():
    i = 0
    arr = [1,2,5,10,255,3]
    i = sum(arr)/len(arr)
    print i
fAvg()
