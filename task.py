#function to print even numbers between 1 and 20
def displayEven():
    evenList=[]
    for i in range(1,21):
        if i%2==0:
            evenList.append(i) 
    return evenList
