# 새로 알게된 python 기능,함수 목록

## list, string

''.join(list) list를 문자열로 나타내기 (list는 문자열이여만 한다)

for i,x in enumerate(list): index와 같이 매핑한다

for x,y in zip(list1,list2): 2개 이상의 데이터를 같이 매핑한다

.rjust(크기,초기화할 값) 부족한 크기만큼 초기화시켜줌
.zfill(크기) 부족한 크기만큼 0으로 초기화시켜줌

sorted(list,key=lamda x: 정렬 기준) 정렬 커스텀. 튜플로 여러 기준 가능
sorted(list,key=lamda x: (기준1,기준2))

sorted(String) split처럼 List로 반환함

list1.extend(list2) list 추가

## 기타

**2는 제곱, **.5는 제곱근

/ float나누기
// int나누기

bin(10진수)= '0b'+2진수 반환 -> bin(10진수)[2:] 로 2진수만 반환
비트 연산자 AND='&' OR='|' XOR='^' NOT='~' 가 있다

from collections import defaultdict
d = defaultdict(int) 0으로 초기화하는 dict

return A and B - 둘다 참 -> B를 리턴 / 둘 다 거짓 -> A를 리턴 / 하나만 참 -> 거짓을 리턴
return A or B - 반대
대부분 return A or B 로 하나만 참일 때 참을 리턴하는 것을 씀

ord = 문자를 숫자로
chr = 숫자를 문자로

# 자주 까먹는 python 기능,함수

.count(값) 값이 몇 개 있는지 반환
"asasas".count("as") -> 3

sum(list) 리스트 원소의 총 합을 반환

if 값 in list: 값이 list에 있거나 없을 때의 조건문
if 값 not in list:
if 값 not in dict.keys(): dict도 가능

list.index(값) list 버전 값의 위치 반환 (없으면 -1)
string.find(값) string 버전

string.isdigit() 특수 표현 가능(⅔) 숫자인지 확인
string.isdecimal() 특수 표현 불가능, 0을 포함한 양수

list.remove(값) list에서 값인 원소 제거(앞에서부터 1개만)
list.pop(index값) list의 인덱스값에 위치한 원소 제거
