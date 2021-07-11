# 문자열 나누기
identifier = "881120-1068234"
hypen_find = identifier.find('-')  # 없으면 -1
hypen_index = identifier.index('-')  # 없으면 에러 발생

if hypen_find == -1:
    print('유효한 주민번호가 아님')
    exit()

# 인덱스 지정
head = identifier[:hypen_find]
foot = identifier[hypen_find + 1:]
print(f"{head}, {foot}")

# 구분자로 분리
split_array = identifier.split('-')
print(f"{split_array[0]}, {split_array[1]}")

# 문자열 추출
gender = identifier[hypen_find + 1]
print(gender)

# 배열 안에서 찾기
if gender in ['1', '3']:
    print('3등시민 ㅜㅜ')
elif gender in ['2', '4']:
    print('쓰니야 나 넘 감동 ㅜㅜ')
else:
    pass

# 문자열 치환
print("a:b:c:d".replace(':', '#'))

# 배열 정렬
sort_q6 = [1, 3, 5, 4, 2]
sort_q6.sort()
sort_q6.reverse()

for item in sort_q6:
    print(item)

# 문자열 병합
join_q7 = ['Life', 'is', 'too', 'short']
print(" ".join(join_q7))

# 튜플 요소 추가
tuple_q8 = (1, 2, 3)
tuple_q8_addition = (4, )
print(tuple_q8 + tuple_q8_addition)

dictionary_q10 = {'A': 90, 'B': 80, 'C': 70}
print(dictionary_q10['B'])
print(dictionary_q10.pop('B'))

# 집합을 이용한 리스트 중복제거
list_q11 = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
set_q11 = set(list_q11)
print(set_q11)
