def oFunc():
    num = 1
    for num in range (1,2001):
        if num % 2 == 0:
            print "Number is" + str(num) + ". This is an even number."
        else:
            print "Number is" + str(num) + ". This is an odd number."

oFunc()

def mFunc():
    a = [2,4,10,16]
    for value in range(0,4) :
        b = a[value] * 5
        print b
mFunc()
