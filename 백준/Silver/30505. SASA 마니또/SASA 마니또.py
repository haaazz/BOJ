import sys
input=sys.stdin.readline
n,m=map(int,input().split())
#왼쪽 숫자 담을 리스트
a_list=[]
#오른쪽 숫자 담을 리스트
b_list=[]
#숫자를 담음
for i in range(m):
    a,b=map(int,input().split())
    a_list.append(a)
    b_list.append(b)
#세종이 숫자를 담음
sejong=int(input())
#마니또 번호 초기화
manitto=0

#경우의 수 초기화 ,숫자의 개수만큼으로
count=n

#세종이가 왼쪽,오른쪽에 없으면 경우의 수는 
#n의 크기-오른쪽 숫자 개수에서 1을 더 뺌
if sejong not in a_list and sejong not in b_list:
    count= count-len(b_list)-1


#세종이가 왼쪽리스트가 있을때에는 무조건 경우의 수 1개
#당연함 마니또 당해버린거임.
elif sejong in a_list:
    count=1

#세종이가 a에는 없고 b에만 있을 때 
#일단은 경우의 수에서 오른쪽 숫자
elif sejong in b_list and sejong not in a_list:
    count=count-len(b_list)

    #근데 질문게시판의 반례(4<-4)나 예제 입력 2처럼(3<-3) 
    #같은 수는 마니또를 못 시켜서 경우의 수가 1개가 될 경우가 나올 수 있음
    for i in range(1,n+1):
        if i!=sejong and i not in a_list and i not in b_list and count==2:
            count-=1

#경우의수가 1보다 많으면 출력 아니면 노잼
if count>1:
    print(count)
else:
    print("NOJAM")