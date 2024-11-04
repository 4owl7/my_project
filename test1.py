def gray_code(n):
    result = []
    for i in range(2 ** n):
        # 生成格雷码
        gray = i ^ (i >> 1)
        result.append(gray)
    return result

# 测试
n = 2
print(gray_code(n))
n=1
print(gray_code(n))
