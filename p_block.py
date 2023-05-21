def p_block_forward(input_data):
     table = [
          1, 5, 2, 0, 3, 7, 4, 6
     ]
     output_data = 0
     for i in range(8):
          tetrad = (input_data >> i) & 0x1
          output_data |= (tetrad << table[i])
     return output_data

def p_block_inverse(input_data):
    table_inverse = [
        3, 0, 2, 4, 6, 1, 7, 5
    ]
    output_data = 0
    for i in range(8):
        tetrad = (input_data >> i) & 0x1
        output_data |= (tetrad << table_inverse[i])
    return output_data