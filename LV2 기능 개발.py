def solution(progresses, speeds):
    Q=[]
    for x, y in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((x-100)//y):
            Q.append([-((x-100)//y),1])
            
        else:
            Q[-1][1]+=1
            
    return [i[1] for i in Q]