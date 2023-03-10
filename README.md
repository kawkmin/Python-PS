# list, string

''.join(list) list를 문자열로 나타내기 (list는 문자열이여만 한다)
"".join(map(str, li)) 로 int List도 가능

list.index(값) list 버전 값의 위치 반환 (없으면 오류)
string.find(값) string 버전 (없으면 -1)

list.remove(값) list에서 값인 원소 제거(앞에서부터 1개만)  
list.pop(index값) list의 인덱스값에 위치한 원소 제거

li = list(set(li)) list의 중복 제거

for i,x in enumerate(list): index와 같이 매핑한다  
for x,y in zip(list1,list2): 2개 이상의 데이터를 같이 매핑한다

부족한 크기만큼 채우기(str만 됨,sorted처럼 반환함 )
.rjust(크기,초기화할 값) 부족한 크기만큼 초기화시켜줌(앞에서부터)
.zfill(크기) 부족한 크기만큼 0으로 초기화시켜줌 (앞에서부터)
.ljust(크기,초기화할 값) 부족한 크기만큼 초기화시켜줌(뒤에서부터)

sorted(list,key=lamda x: 정렬 기준) 정렬 커스텀. 튜플로 여러 기준 가능  
sorted(list,key=lamda x: (기준1,기준2))

list1.extend(list2) list 추가

.count(값) 값이 몇 개 있는지 반환

string.isdigit() 특수 표현 가능(⅔) 숫자인지 확인  
string.isdecimal() 특수 표현 불가능, 0을 포함한 양수

문자열에서 remove 없으니, replace 또는 슬라이스로 지우자

비교할 때 string in ['123','124'] in 사용 가능

# dict

정렬
dic=sorted(dic, key=lambda x: x[1]) = value의 값으로 정렬 후, items의 List로 반환
dic=sorted(dic, key=lambda x: x[0]) = key의 값으로 정렬 후, items의 List로 반환
dic=sorted(dic.items(),key=lambda x: x[1]) = value의 값으로 정렬 후, List tuple형태로 반환 !!

리스트 삽입을 zip으로 사용가능
a=['a','b','c']
b=[1,2,3]
dic(zip(a,b))

dict foreach할 때  
for i in dict:  
i[0]//key  
i[1]//values 가 된다

# 기타

bin(10진수)= '0b'+2진수 반환 -> bin(10진수)[2:] 로 2진수만 반환  
비트 연산자 AND='&' OR='|' XOR='^' NOT='~' 가 있다

return A or B 로 하나만 참일 때 참을 리턴하는 것을 씀

ord = 문자를 숫자로  
chr = 숫자를 문자로

a=[0 for i in range(100)] 으로 배열 초기화 처럼 사용 가능

list comprehension에 else를 추가  
['yes' if x in store else 'no' for x in customer]

int형변환은 자동으로 앞의 0을 지워준다
a = "001" int(a)==1

리스트 중 하나라도 True면, return True
any([])
if all(구현): all안에 반복문들이 모두 True 일때

a와 b swap하는 법
a,b=b,a

값을 찾을 때, 쓰는 x in [1,2,3]는 속도가 매우느리다
-> set()으로 바꿔주면 매우 빨라짐

deque는 .pop(위치)가 없고 popleft등 이 있다

import copy의 copy.deepcopy(복사할 리스트)로 깊은 복사 가능
