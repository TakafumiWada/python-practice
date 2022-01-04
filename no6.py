# 入力を変数に代入
line1 = input()
# line1をn,a,bに分割する
n, a, b = map(int, line1.split(' '))

possibleList = []
# 1~nまでのループ処理
for num in range(1, n + 1):
    # numをstring型に変換
    numStr = str(num)
    # line1を一文字ずつ分割し、listに代入
    numList = [int(el) for el in list(numStr)]
    # listの合計値(各桁の合計値)を算出
    numSum = sum(numList)
    # numSumがa以上b以下の場合、possibleListに追加
    if a <= numSum and numSum <= b:
        possibleList.append(num)
# possibleListの合計値を出力
print(sum(possibleList))
