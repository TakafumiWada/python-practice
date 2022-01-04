# 1行目の入力を変数に代入
line1 = input()
# 2行目の入力を変数に代入
line2 = input()
# 3行目の入力を変数に代入
line3 = input()

# line1をint型に変換し、aに代入
a = int(line1)
# line2を' 'で分割し、それぞれをint型に変換。その後に変換されたlistの0番目をb,1番目をcに代入
b, c = map(int, line2.split(' '))
# line3をそのままString型でsに代入
s = line3

# a+b+cの和とsをスペース一つ空けて出力
print(f'{a+b+c} {s}')
