from collections import deque
from itertools import permutations

n = int(input())
#최대 점수
max_score = -1
#타자가 기록할 결과 리스트
batter = [list(map(int,input().split())) for _ in range(n)]
#타자 순서를 정하기 위한 리스트
entry = [i for i in range(1,9)]




def attack(batting,b1,b2,b3,score,out_count):
    if batting == 0:
        out_count += 1
        
    elif batting == 1:
        score += b3
        b1,b2,b3 = 1,b1,b2
       
    elif batting == 2:
        score += b2+b3
        b1,b2,b3 = 0,1,b1
       
    elif batting == 3:
        score += b1+b2+b3
        b1,b2,b3 = 0,0,1
      
    elif batting == 4:
        score += b1+b2+b3+1
        b1,b2,b3 = 0,0,0
    return b1,b2,b3,score,out_count   


def next_batter(next):
    if next == 8:
        next = 0
    else:
        next += 1
    return next
     

for i in permutations(entry,8):
    #다음 타자
    next = 0
    #스코어
    score = 0
    #4번타자를 슬라이싱으로 넣어주는 과정
    temp = list(i)
    temp = temp[:3]+[0]+temp[3:]


    for j in range(n):
        #1루 주자
        b1 = 0
        #2루 주자    
        b2 = 0
        #3루 주자
        b3 = 0
        #아웃 카운트
        out_count = 0
        #3아웃까지 타격
        while out_count < 3:
            b1,b2,b3,score,out_count=attack(batter[j][temp[next]],b1,b2,b3,score,out_count)
            
            #다음 타자 갱신
            next = next_batter(next)
    #최고점수 비교                 
    if max_score < score:
        max_score = score
print(max_score)