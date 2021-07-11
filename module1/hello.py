# coding=utf8

"""
Author: chanroid
Date : 20210711
여러줄 주석
https://wikidocs.net/12769 따라하기
"""

# 문자열 변수 선언
text: str = 'hihi'
text2 = "hihi"

# 따옴표 3개로 여러 줄 사용
text3 = '''
hihi
hihi
'''
text4 = """
hihi
hihi
"""
text5 = text4 * 2

# 숫자 변수 선언
num1: int = 10
num2 = 10.5  # 소수

# 논리 변수 선언
yes: bool = True
no = False

# 여러 변수 한가지 값으로 선언
x = y = 10

# 여러 변수 다른 값으로 선언
x2, y2 = 1, 2


def print_int(value):
    print(x2)


def print_value(value):
    print(value)


# 문자열 indexof
# index_char = text5[2]

# 자르기
# concat_string = text5[0:7]

# 음수는 뒤에서 센 자리
# concat_from_end = text5[:-3]

# formatting
# format_value = "decimal: %d, %d, string: %s, %s" % (x, x2, text, text2)
# format_value_2 = "decimal: {0}, {1}, string: {2}, {3}".format(x, x2, text, text2)
# format_value_3 = "decimal: {xx}, {xx2}, string: {t1}, {t2}".format(xx=x, xx2=x2, t1=text, t2=text2)
# format_value_4 = f"decimal: {x}, {x2}, string: {text}, {text2}"

