def solution(num, total):
    answer = []
    start=-100
    end=1000
    while start<=end:
        mid=int((start+end)/2)
        sum=0
        for i in range(mid,mid+num):
            sum+=i
            
        if sum==total:
            for i in range(mid,mid+num):
                answer.append(i)
            break;
        
        if sum<total:
            start=mid+1
        elif sum>total:
            end=mid-1
        
    return answer