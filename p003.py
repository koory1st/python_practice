# encoding: UTF-8

# 文件操作
import sys
# 读操作
txt = open("temp.txt")
print(txt.read())

# 写操作
target = open("temp.txt", 'w', encoding="utf-8")
target.write("大幅度\n")

target.write("abcde\n")
target.write("12345")
target.close()
