def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def usd_to_krw(usd, exchange_rate=1304):  # exchange_rate의 기본값은 1304
    krw = usd * exchange_rate
    return krw

def amp_to_ma(ampere):
    milliampere = ampere * 1000
    return milliampere

def main():
    while True:
        print("단위 변환기: 1. 섭씨를 화씨로 변환, 2. 달러를 원화로 변환, 3. 전류 변환, 0. 종료")

        try:
            choice = int(input("원하는 작업을 선택하세요 (1, 2, 3, 또는 0): "))

            if choice == 1:
                # 섭씨를 화씨로 변환
                celsius = float(input("섭씨 온도를 입력하세요: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius} 섭씨는 {fahrenheit} 화씨입니다.")
                
            elif choice == 2:
                # 달러를 원화로 변환
                usd = float(input("달러를 입력하세요: "))
                krw = usd_to_krw(usd)
                print(f"{usd} 달러는 {krw} 원입니다.")

            elif choice == 3:
                # 전류를 밀리암페어로 변환
                ampere = float(input("전류를 입력하세요 (암페어): "))
                milliampere = amp_to_ma(ampere)
                print(f"{ampere} 암페어는 {milliampere} 밀리암페어입니다.")

            elif choice == 0:
                print("프로그램을 종료합니다.")
                break

            else:
                print("1, 2, 3, 또는 0 중에서 선택해주세요.")

        except ValueError: # 사용자가 숫자가 아닌 값을 입력했을 때
            print("올바른 숫자를 입력하세요.") # 에러 메시지 출력

if __name__ == "__main__": # 이 파일이 직접 실행되면 main() 함수를 호출하라
    main() # main() 함수 호출
