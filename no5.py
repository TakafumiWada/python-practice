# 入力を変数に代入
a = int(input())
b = int(input())
c = int(input())
x = int(input())

# countの初期値を0にする
count = 0
# a,b,cの全パターンの組み合わせを実行できるようにfor文を重ねる
for numA in range(a + 1):
    for numB in range(b + 1):
        for numC in range(c + 1):
            # ある組み合わせパターンにおける合計金額を算出
            sum = 500 * numA + 100 * numB + 50 * numC
            # 合計金額がxと一致すればcountを加算する
            if sum == x:
                count += 1
print(count)
