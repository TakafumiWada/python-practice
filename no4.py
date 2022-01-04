# 入力を変数に代入
line1 = input()
line2 = input()

# line2を' 'ずつ分割し、int型に変換してlistに代入
list = [int(el) for el in line2.split(' ')]


def isEvenList(list):  # listが全て偶数かを判断する関数
    for el in list:
        if el % 2 == 1:
            return False
    return True


# sumの初期値を定義
sum = 0
# list全てが偶数の場合ループ処理を行う
while isEvenList(list):
    # listの値全てを2で割る
    list = [el / 2 for el in list]
    # sumに値を1加える
    sum += 1

# sumの値を出力する
print(sum)
