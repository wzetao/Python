user_name = "Charlie"
user_age = 8
# 同时输出多个变量和字符串
print("读者名：", user_name, "年龄：", user_age, sep = "|")
# 同时输出多个变量和字符串，指定分隔符
print("读者名:" , user_name, "年龄:", user_age, sep='|')
print(40, '\t', end="")
print(50, '\t', end="")
print(60, '\t', end="")
f = open("poem.txt", "w") # 打开文件以便写入
print('沧海月明珠有泪', file=f)
print('蓝田日暖玉生烟', file=f)
f.close()