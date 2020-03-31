"""
문제 제목 : 거스름돈
문제 난이도 : 하
문제 유형 : 그리디
거스름돈의 최소 개수를 계산
가장 기초적인 탐욕 알고리즘 문제 유형
단순히 '큰 화폐 단위' 순서대로 잔돈을 거슬러 주면 최적의 해를 얻을 수 있음
"""
coin_list=[500,100,50,10,5,1]
coin = int(input())
garage = 1000-coin

coin_list.sort(reverse=True)

coin_num=0
for i in coin_list:
    value=garage // i
    coin_num += value
    garage -= i*value
print(coin_num)
