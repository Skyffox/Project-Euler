'''
We simply look at every subset of 4 of the digits and count the number of consecutive values 
that can be found by listing the value of every integer arithmetic expression that can be written.
'''
 
import time
 
def subset(myList,n):
    l = len(myList)
    if(l==0):
        if(n==0):
            return [[]]
        return []
    if(l<n):
        return []
    if(l==n):
        return [sorted(myList)]
    a = myList[0]
    total = subset(myList[1:],n)
    possible = subset(myList[1:],n-1)
    for x in possible:
        t = x[:]
        t.append(a)
        total.append(sorted(t))
    return total
 
def permutations(myList):
    l = len(myList)
    if(l==0):
        return []
    if(l==1):
        return [myList]
    a = myList[0]
    b = permutations(myList[1:])
    total = []
    for c in b:
        for x in range(l):
            t = c[0:x]
            t.append(a)
            t.extend(c[x:])
            total.append(t)
    return total
 
def allTuples(myList,n):
    if(n==0):
        return [[]]
    b = allTuples(myList,n-1)
    total = []
    for x in b:
        for y in myList:
            z = x[:]
            z.append(y)
            total.append(z)
    return total

def insertOperations(myList):
    operationTriples = allTuples(["+","-","*","/"],3)
    parentheseOptions = [" o o o ","( o o )o ","( o )o o ", "( o )o( o )","(( o )o )o "]
    final = []
    wrongCount = 0
    for p in parentheseOptions:
        for o in operationTriples:
            s = ""
            c = 0
            d = 0
            for x in p:
                if x==" ":
                    s+=str(float(myList[c]))
                    c+=1
                elif(x=="o"):
                    s+=str(o[d])
                    d+=1
                else:
                    s+=x
            try:
                myValue = eval(s)
                if(myValue-int(myValue)==0):
                    if int(myValue) not in final:
                        final.append(int(myValue))
                else:
                    wrongCount+=1
            except:
                wrongCount+=1
    return final
 
def projectEulerProblemNinetyThree():
    quadruples = subset([0,1,2,3,4,5,6,7,8,9],4)
    maxFound = 28
    maxQuadruple = [1,2,3,4]
    for x in quadruples:
        y = permutations(x)
        total = []
        for z in y:
            w = insertOperations(z)
            for a in w:
                if a>0 and a not in total:
                    total.append(a)
        c = 1
        while c in total:
            c+=1
        if(c>maxFound):
            maxFound = c
            maxQuadruple = x
    s = ""
    for a in maxQuadruple:
        s+=str(a)
    return s
 
start = time.time()
print(projectEulerProblemNinetyThree())
print ("--- %s seconds ---" % (time.time()-start))