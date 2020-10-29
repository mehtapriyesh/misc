

import numpy as np
mat = np.array(
        [[np.NAN, np.NAN, np.NAN],
        [np.NAN, np.NAN, np.NAN],
        [np.NAN, np.NAN, np.NAN]]
        )

print("In this game you will be giving positions of where you want to place your mark.  \nGame will automatically be checked and you'll get your result.\nBe careful while giving your coordinates\nGive the row and column position seperated by space like a normal matrix. \nex: 1 1, 1 2, .... 3 2, 3 3")

name1 = input("Enter your name player 1")
name2 = input("Enter your name player 2")


def check(obj):
    for n in range(3):
        if sum(obj[n,]) == 3 or sum(obj[n,]) == 0:
            print(obj[n,1])
            return True
        elif sum(obj[:,n]) == 3 or sum(obj[:,n]) == 0:
            print(obj[1,n])
            return True
    if sum(np.diag(obj)) == 3 or sum(np.diag(obj)) == 0:
            print(np.diag(obj))
            return True
    elif sum(np.diag(np.fliplr(obj))) == 3 or sum(np.diag(np.fliplr(obj))) == 0:
            print((np.diag(np.fliplr(obj)))[1])
            return True
    
    
print("Start from this position and do not use any prefilled positions")

while mat.mean() != np.NAN:
    print(mat)
    print("Enter your position", name1)
    a,b = input().split()
    a = int(a) - 1
    b = int(b) - 1
    mat[a][b] = 1
    print(mat)
    if check(mat) == True or mat.mean() == np.NAN:
        break
    print("Enter your position", name2)
    x,y = input().split()
    x = int(x) - 1 
    y = int(y) - 1
    mat[x][y] = 0
    if check(mat) == True:
        break

if check(mat) == False:
    print("Game ended in a draw")
else:
    if (np.count_nonzero(~np.isnan(mat)))%2 == 0:
        print("Player", name2, "is winner.")
    else:
        print("Player", name1, "is winner.")


