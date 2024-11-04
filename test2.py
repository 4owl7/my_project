def valid_utf8(data):
    # 记录当前字符还需要的字节数
    remaining_bytes = 0

    for byte in data:
        # 只保留低8位
        byte = byte & 0xFF

        if remaining_bytes == 0:
            # 判断字节数
            if (byte >> 5) == 0b110:  # 2字节字符
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3字节字符
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4字节字符
                remaining_bytes = 3
            elif (byte >> 7) != 0:  # 非1字节字符的开头
                return False
        else:
            # 检查延续字节是否以10开头
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1

    return remaining_bytes == 0

# 测试
data1 = [197, 130, 1]
data2 = [235, 140, 4]
print(valid_utf8(data1))  # 输出: True
print(valid_utf8(data2))  # 输出: False
