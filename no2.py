# 1行目の入力をline1に代入
line1 = input()

# line1を' 'で分割し、それぞれをint型に変換。その後に変換されたlistの0番目をb,1番目をcに代入
a, b = map(int, line1.split(' '))
# a,bの積をsumに代入
sum = a * b

if sum % 2 == 0:  # sumが偶数なら
    print('Even')
else:  # sumが奇数なら
    print('Odd')
