def solution(polynomial):
    x=0
    num=0
    temp=''
    i=0
    while i<len(polynomial):
        if polynomial[i]=="x":
            x+=1
        
        elif polynomial[i]>"0" and polynomial[i]<="9" :
            for j in range(i,len(polynomial)):
                if polynomial[j]==" ":
                    num+=int(temp)
                    i=j
                    temp=''
                    break

                elif polynomial[j]=="x":
                    x+=int(temp)
                    i=j
                    temp=''
                    break 
                    
                elif j==len(polynomial)-1:
                    temp+=polynomial[j]
                    num+=int(temp)
                    i=j
                    temp=''
                    break

                else:
                    temp+=polynomial[j]
                    
        i+=1
        
    answer=""
    if x>0 : 
        if x==1 : answer+="x"
        else : answer+=str(x)+"x"
        
        if num>0 : answer+=" + "+str(num)
    elif num>0 :
        answer+=str(num)
    return answer

        