test = int(input())
 
for i in range(test):
    #Doc so N
    N = input().strip()
    #Lay hai chu so dau va hai chu so cuoi
    haichusodau = N[:2]
    haichusocuoi = N[-2:]
    
    #Kiem tra:
    if haichusodau ==  haichusocuoi:
        print("YES")
    else:
        print("NO")
         