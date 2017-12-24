def gcdlcm(a, b):#유클리드 호제법
    # answer = []
    x = a
    y = b
    while True:
        z = x % y
        if z == 0:
            break
        x = y
        y = z
    # answer.append(y)
    # answer.append(int(a*b/y))
    answer = [y, int(a*b/y)]
    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))