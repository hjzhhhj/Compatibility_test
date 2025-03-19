import random

def calculate_compatibility(name1, name2):
    combined = name1 + name2
    score = sum(ord(char) for char in combined) % 101  # 0~100 사이 점수
    return score

def main():
    print("이름 궁합 테스트!")
    name1 = input("첫 번째 이름을 입력하세요: ")
    name2 = input("두 번째 이름을 입력하세요: ")
    
    score = calculate_compatibility(name1, name2)
    print(f"{name1} 님과 {name2} 님의 궁합 점수는 {score}점입니다!")
    
    if score > 80:
        print("💖 최고의 궁합! 운명적인 만남!")
    elif score > 50:
        print("😊 꽤 좋은 궁합이네요!")
    elif score > 30:
        print("🤔 음.... 음...... 화이팅!")
    else:
        print("💔 띠로리~")

if __name__ == "__main__":
    main()