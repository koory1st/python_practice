# encoding: UTF-8
# 此处需要加上上面的这句，否则在terminal里会出现异常

#  
# 参数例子
# 

# 整形
a = 1
print(a)

# 浮点
b = 1.2e2
print(b)

# 转义
c = 'I\'m ok'
print(c)

# 换行
d = r'''hello 
world'''
print(d)

print("aaaa", "123131", "hahahah")

# 替换变量 f
print(f"test {d}")
name = 'gu'
hello = f'hello {name}'
print(hello)
hilarious = False

# 替换变量 .format
joke_evaluation = "Isn't that joke so funny?! {}, {}"
print(joke_evaluation.format(hilarious, d))

# 字符串链接
w = "This is the left side of..."
e = "a string with a right side."
print(w + e)

# 重复字符串
print("." * 10)