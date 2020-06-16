# 以0x或0X开头的整形数值是十六进制形式大整数
hex_value1 = 0x13
hex_value2 = 0XaF
print("hex_value1的值为：", hex_value1)
print("hex_value2的值为：", hex_value2)

# 以0b或0B开头的整形数值是二进制形式大整数
bin_val = 0b111
print("bin_val的值为：", bin_val)
bin_val = 0B101
print("bin_val的值为：", bin_val)

# 以0o或0O开头的整形数值是八进制形式大整数
oc_val = 0o54
print("oc_val的值为：", oc_val)
oc_val = 0O17
print("oc_val的值为：", oc_val)

# 在数值中使用下画线
one_million = 1_000_000
print(one_million)
price = 234_234_234  # price实际的值为234234234
android = 1234_1234  # android实际的值为12341234
