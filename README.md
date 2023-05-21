# Ralization S and P Block in Cryptography


S-block


We divide the input data into two tetrads: the first tetrad (higher bit) and the second tetrad (younger bit).
We apply a direct transformation using the table of constants:
We take the value of the first notebook and find the corresponding line in the table of constants.
Using the value of the second notebook, we select the value of the column corresponding to this row.
We combine the obtained values, shift them to the left by 4 bits and store them as the output data of the S-block.
Repeat steps 1-2 for the second notebook.
We combine the obtained values from the first and second tetrads into one number and return it as the output data of the S-block.


S-block (reverse conversion)


We divide the output data of the S-block into two tetrads: the first tetrad (higher bit) and the second tetrad (younger bit).
We apply the inverse transformation using the inverse table of constants:
We take the value of the first notebook and find the corresponding line in the reverse table of constants.
Using the value of the second notebook, we select the value of the column corresponding to this row.
We combine the obtained values, shift them by 4 bits to the left and store them as the output data of the reverse S-block.
Repeat steps 1-2 for the second notebook.
We combine the obtained values from the first and second tetrads into one number and return it as the output data of the reverse S-block.


P block


We take input data.
With the help of the P-block table, we convert each bit of the input data into a new position:
We copy the input data bit to the new position specified in the P-block table.
We combine the received bits into one number and return it as the output data of the P-block.


P block (reverse conversion)


We take the output data of the P-block.
With the help of the reverse table of the P-block, we convert each bit of the output data into the initial position:
We copy the bit of the output data to the initial position specified in the reverse table of the P-block.
We combine the received bits into one number and return it as the output data of the reverse P-block
