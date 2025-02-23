def checkip(ip):
    if not ip or len(ip) > 15: #Nếu xâu rỗng
        return False
    tach = ip.split(".") #192.1.2.3 ("192","1", "2", "3")
    if len(tach) != 4:
        return False
    
    for i in tach:
        if not i.isdigit():
            return False
    
        soip = int(i)
        if soip < 0 or soip > 255:
            return False
    return True

for i in range(int(input())):   
    ip = input().strip()
    if checkip(ip):
        print("YES")
    else:
        print("NO")
    
    

    