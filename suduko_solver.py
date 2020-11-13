#Taking size and then suduko(lists of list) from the user
suduko=[]
print("enter length of suduko")
n=int(input())
print("Enter elements row-wise with separating space and if no element is present,enter it as 0")
for i in range(n):
    temp=[]
    temp=input().split(" ")
    suduko.append(temp)
def solver(s):
    find=is_empty(s)
    if not find:
        return True
    else:
        row,col=find
    for i in range(1,10):
        if valid(s,i,(row,col)):
            #print(row,col)
            s[row][col]=str(i)
            if solver(s):
                #print("solver block")
                return True
            s[row][col]='0'
    return False

#printing suduko in a format of boxes
def print_suduko(s):
    for i in range(n):
        if i%3==0:
            print("-----------------------")
        for j in range(n):
            if j%3==0 and j!=0:
                print(" | ",end="")
            print(s[i][j],end=" ")
        print()
print_suduko(suduko)
#checking whether the box is empty or not(if it is 0 then it is empty)
def is_empty(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i][j]=='0':
                return (i,j) #(row_index,col_index)
    return 0
def valid(s,num,pos):
    #checking in row
    for i in range(len(s)):
        if s[pos[0]][i]==str(num) and pos[1]!=i:
            return False
    #checking in column
    for i in range(len(s)):
        #print("2nd for")
        if s[i][pos[1]]==str(num) and pos[0]!=i:
            return False
    #checking in box
    _x=pos[0]//3
    _y=pos[1]//3
    for i in range(_x*3,_x*3+3):
        for j in range(_y*3,_y*3+3):
            if s[i][j]==str(num) and pos!=(i,j):
                return False    
    return True
solver(suduko)
print_suduko(suduko)
