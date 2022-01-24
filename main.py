import math
import random

def finish(ab, ac, bc):
    #переменные
    dct={"a":0,"b":0,"c":0,}


    #запись данных
    for i in range(0, len(ab)):
        if ab[i] == ">" or ab[i] == "<" or ab[i] == "=":
            sign_ab = ab[i]
            break
    for i in range(0, len(ac)):
        if ac[i] == ">" or ac[i] == "<" or ac[i] == "=":
            sign_ac = ac[i]

            break
    for i in range(0, len(bc)):
        if bc[i] == ">" or bc[i] == "<" or bc[i] == "=":
            sign_bc = bc[i]
            break


    #решение
    if sign_ab == "=" and sign_ac == "=" and sign_bc == "=":
        return ('abc')

    else:
        if sign_ab == '>':
            dct["b"]+=1
        if sign_ac =='>':
            dct["c"] += 1
        if sign_bc=='>':
            dct["c"] += 1
        elif sign_ab =='<':
            dct["a"] += 1
        elif sign_ac == "<":
            dct["a"] += 1
        elif sign_bc == "<":
            dct["b"] += 1
    copy = sorted(dct, key=dct.get)
    return(copy[2] + copy[1] + copy[0] )







'''res_ab = str(input())
res_ac = str(input())
res_cb = str(input())
print(finish(res_ab, res_ac, res_cb)'''


def numSort(lnum):
    if lnum[-1]==0 and lnum[0]==0 and len(set(lnum))>1:
        return('NO')
    for i in range(0,len(lnum)):
        if len(set(lnum))==1:
            print('YES')
            fStr = ''
            for i in range(0, len(lnum)):
                fStr += str(lnum[i]) + ' '
            return (fStr)

# ----------------------------------------------------------


# ----------------------------------------------------------

        elif lnum[i] == 0:
            for j in range(0, len(lnum)):
                if j == len(lnum)-1:
                    pass
                elif abs(lnum[i])<abs(lnum[i+1]):
                    pass
                else:
                    return('NO')
            print('YES')
            fStr = ''
            for i in range(0, len(lnum)):
                if lnum[i]<0:
                    lnum[i]*=(-1)
                fStr += str(lnum[i]) + ' '
            return (fStr)

# ----------------------------------------------------------

        elif lnum[-1] == 0:
            for j in range(0, len(lnum)):
                if j==len(lnum)-1:
                    pass
                elif abs(lnum[j])>=abs(lnum[j+1]):
                    pass
                else:
                    return ("NO")
            print('YES')
            fStr = ''
            for i in range(0, len(lnum)):
                if lnum[i]>0:
                    lnum[i]*=(-1)
                fStr += str(lnum[i]) + ' '
            return (fStr)

# ----------------------------------------------------------

        elif 0 in lnum:
            index = 0
            for k in range(0,len(lnum)):
                if lnum[k]==0:
                    index = k
                    for j in range(0,k):
                        if j == len(lnum) - 1:
                            pass
                        elif abs(lnum[j]) >= abs(lnum[j + 1]):
                            pass
                        else:
                            return ("NO")

                    for j in range(k+1,len(lnum)):
                        if j == len(lnum) - 1:
                            pass
                        elif abs(lnum[j]) <= abs(lnum[j + 1]):
                            pass
                        else:
                            return ("NO")





                    print('YES')
                    fStr = ''
                    for i in range(0, len(lnum)):
                        if i<index and lnum[i]>0:
                            lnum[i]*=(-1)
                        elif i>index and lnum[i]<0:
                            lnum[i]*=(-1)
                        fStr += str(lnum[i]) + ' '
                    return (fStr)


#----------------------------------------------------------
        else:
            for k in range(0, len(lnum)):


                if k == len(lnum) - 1:
                    pass

                elif k == (len(lnum) - 1) or (lnum[k] <= lnum[k + 1]):
                    pass


                elif lnum[k] == lnum[k - 1] and k != 0 and lnum[k]>lnum[k+1] and lnum[k+1]*(-1)>=lnum[k]:
                    lnum[k+1]*=(-1)

                elif lnum[k] == lnum[k - 1] and k != 0:
                    pass



                elif lnum[k] > lnum[k + 1] and ((-1) * (lnum[k]) <= (lnum[k + 1])) and (((-1) * lnum[k] >= lnum[k - 1]) or k == 0):

                    lnum[k] *= (-1)



                elif (lnum[k]<=lnum[k+1]) and (lnum[k]<0) and (lnum[k+1]>0) and ((-1)*lnum[k+1]>=lnum[k]):

                    lnum[k+1]*=(-1)



                elif lnum[k] < 0 and lnum[k + 1] < 0 and lnum[k] > lnum[k + 1] and ((-1) * lnum[k] <= (-1) * lnum[k + 1]) and (((-1) * (lnum[k] >= lnum[k - 1]) or k == 0)):

                    lnum[k] *= (-1)
                    lnum[k + 1] *= (-1)



                elif (lnum[k] > lnum[k + 1]) and (lnum[k + 1] * (-1) >= lnum[k]):

                    lnum[k + 1] *= (-1)



                else:
                    return ("NO")

            print('YES')
            fStr = ''
            for i in range(0, len(lnum)):
                fStr += str(lnum[i]) + ' '
            return (fStr)


'''cnt = int(input())
num = list(map(int,input().split()))
print(numSort(num))'''



def Sweets(N,K,A,B):
    count = 0
    balance = A

    if (N*B>A) and ((K-1)*B>A):
        return(A%B)
    else:
        if (N*B<=A) and ((K-1)*B>A):
            while(balance>=N*B):
                balance = balance - N*B
                count+=N+1
            remains = balance//B
            return(count + remains)

        elif N*B>A and (K-1)*B<=A:
            while(balance>(K-1)*B):
                balance -=(K-1)*B
                count+=K
            remains = balance // B
            return (count + remains)
        else:
            while(balance>0):
                 if ((N+1)/(N*B)) > (K/(K-1)*B):
                     if (balance - N*B )<0:
                         count+=balance//B
                         break
                     balance-=N*B
                     count += N+1
                 elif ((N + 1) / (N * B)) < (K / (K - 1) * B):
                     if (balance - ((K-1)* B)) < 0:
                         count += (balance//B)
                         break
                     balance =balance - ((K-1)*B)
                     count = count + K

                 else:
                     if (balance - N*B )<0:
                         count+=balance//B
                         break
                     balance -= N * B
                     count += N + 1

    return(count)

'''N_new= int(input())
K_new = int(input())
A_new = int(input())
B_new = int(input())
print(Sweets(N_new,K_new,A_new,B_new))'''

def MaxMinScore(newList):
    max_score = max(newList)
    min_score = min(newList)
    for i in range(0,len(newList)):
        if newList[i]==max_score:
            newList[i]=min_score
    return(newList)


'''Score = list(map(int,input().split()))
N=Score[0]
Score.pop(0)
print(MaxMinScore(Score))'''



def EnterToTheMinistry(justList):
    def CharNum(string):
        if string == 'a' or string == 'b' or string == 'c':
            return('2')
        elif string == 'd' or string == 'e'  or string == 'f':
            return('3')
        elif string == 'g' or string == 'h' or string == 'i':
            return('4')
        elif string == 'j' or string == 'k' or string == 'l':
            return('5')
        elif string == 'm' or string == 'n' or string == 'o':
            return('6')
        elif string == 'p' or string == 'q' or string == 'r' or string == 's':
            return('7')
        elif string == 't' or string == 'u' or string == 'v':
            return('8')
        elif string == 'w' or string == 'x' or string == 'y' or string == 'z':
            return('9')

    sortList = []

    for i in range(0,len(justList)):
        sum = ''
        for j in range(0,7):
            sum += CharNum(justList[i][j])
        sortList.append(sum)
    return(len(set(sortList)))

'''N = int(input())
newList = []
for i in range(0,N):
    newList.append(input())
print(EnterToTheMinistry(newList))'''











