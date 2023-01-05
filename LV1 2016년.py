def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']

    sum = b
    for i in range(a-1):
        sum += month[i]

    return days[sum % 7]


'''
def solution(a, b):
    month=[31,29,31,30,31,30,31,31,30,31,30,31]
    days=['THU','FRI','SAT','SUN','MON','TUE','WED']
    
    return days[(sum(month[:a-1])+b)%7]
'''
