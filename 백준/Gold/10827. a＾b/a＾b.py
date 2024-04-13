# 컴터는 2진수로 변환해서 연산 -> 오차가 생길 수밖에 없음
# 그럼 어떻게 정확한 계산을 할 수 있을까
# 파이썬은 decimal 이라는 자료구조가 존재 -> 소수를 스트링으로 만들어 연산

from decimal import getcontext, Decimal

a, b = map(str, input().split())

# decimal 모듈에 1101자리의 정밀도(precision) 설정
# -> 거듭제곱의 연산의 결과가 매우 크거나 작아도 정확하게 계산하기 위함
getcontext().prec = 1101


print("{0:f}".format(Decimal(a) ** int(b)))