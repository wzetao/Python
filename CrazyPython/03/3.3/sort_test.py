a_list = [3, 4, -2, -30, 14, 9.3, 3.4]
# 对列表元素排序
a_list.sort()
print(a_list) #[-30, -2, 3, 3.4, 4, 9.3, 14]
b_list = ['Python', 'Swift', 'Ruby', 'Go', 'Kotlin', 'Erlang']
# 对列表元素排序：默认按字符串包含的字符的编码大小比较
b_list.sort()
print(b_list) # ['Erlang', 'Go', 'Kotlin', 'Python', 'Ruby', 'Swift']

# 指定key为len，指定使用len函数对集合元素生成比较的键，
# 也就是按字符串的长度比较大小
b_list.sort(key=len)
print(b_list) # ['Go', 'Ruby', 'Swift', 'Erlang', 'Kotlin', 'Python']
# 指定反向排序
b_list.sort(key=len, reverse=True)
print(b_list) # ['Erlang', 'Kotlin', 'Python', 'Swift', 'Ruby', 'Go']


