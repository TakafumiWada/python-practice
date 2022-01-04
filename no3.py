# 1行目の入力をline1に代入
line1 = input()

# line1を一文字ずつ分割し、listに代入
list = list(line1)

# sumに初期値0を代入
sum = 0

# listをfor文でループさせる
for element in list:
    if element == "1":  # listの要素が"1"だったら
        sum += 1  # sumに値を1増やす

print(sum)
