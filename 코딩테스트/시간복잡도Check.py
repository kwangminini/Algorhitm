import time

array = [1,2,3,4,5]*100
start_time = time.time() #측정 시작
array.sort() #정렬 알고리즘 수행
end_time = time.time() #측정 종료

print("수행 시간 ::",end_time - start_time)