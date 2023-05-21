def s_box(input_data):
    constants = [
        [0x1, 0x0, 0x3, 0x2, 0x5, 0x4, 0x7, 0x6],
        [0x6, 0x7, 0x4, 0x5, 0x2, 0x3, 0x0, 0x1],
        [0x3, 0x2, 0x1, 0x0, 0x7, 0x6, 0x5, 0x4],
        [0x4, 0x5, 0x6, 0x7, 0x0, 0x1, 0x2, 0x3]
    ]
    
    for i in range(2):
        t1 = (input_data & 0xF0) >> (4 * i)  # перша тетрада
        t2 = input_data & 0x0F  # друга тетрада
    
    output_data = (constants[i][t1] << 4) | constants[i][t2]
    return output_data

a = s_box(1)
b = s_box(a)

print(a)
print(b)

