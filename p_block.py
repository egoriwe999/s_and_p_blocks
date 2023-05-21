def p_block(input_data):
     p_table = [
          #1, 5, 2, 0, 3, 7, 4, 6
          3, 2, 1, 0, 7, 6, 5, 4
     ]
     output_data = 0
     for i in range(8):
          bit = (input_data >> i) & 0x1
          output_data |= (bit << p_table[i])
     return output_data

input_data = 47

a = p_block(input_data)
b = p_block(a)

print(a)
print(b)