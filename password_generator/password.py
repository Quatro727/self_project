import random



def password_generator(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    all_characters = ""
    code_dict={
        "spec":['*','&','!', '$', '#','%'],
        "upper_eng":['A','B','C','D' 'E' 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'V', 'X','Y', 'Z'],
        "lower_eng":['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z'],
        "num":[0,1,2,3,4,5,6,7,8,9]
    }
    # 조건에 맞는 문자 집합 추가
    if use_uppercase=='y' or use_uppercase=='Y':
        for element in code_dict["upper_eng"]:
            all_characters+=element
    if use_lowercase=='y' or use_lowercase=='Y':
        for element in code_dict["lower_eng"]:
            all_characters+=element
    if use_digits=='y'or use_digits=='Y':
        for element in code_dict["num"]:
            all_characters+=str(element)
    if use_special_chars=='y' or use_special_chars=='Y':
        for element in code_dict["spec"]:
            all_characters+=element

    # 비밀번호 생성
    password = ''
    for _ in range(length):
        # ranmdom 모듈의 choice()를 이용해 모든 문자들을 모은 all_characters에서 랜덤으로 문자 하나 추출
        password+=random.choice(all_characters)
    return password


# 사용자 입력 받기
length = int(input("비밀번호 길이를 입력하세요: "))
use_uppercase = input("대문자를 포함하겠습니까? (y/n): ")
use_lowercase = input("소문자를 포함하겠습니까? (y/n): ")
use_digits = input("숫자를 포함하겠습니까? (y/n): ")
use_special_chars = input("특수문자를 포함하겠습니까? (y/n): ")

# 비밀번호 생성
password = password_generator(length, use_uppercase, use_lowercase, use_digits, use_special_chars)

# 결과 출력
print("생성된 비밀번호:", password)