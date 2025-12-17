def pattern13(n):
    for i in range(1, n + 1):
        # Calculate the 'offset' for the current row using the formula
        row_start_offset = (i * (i - 1)) // 2
        
        for j in range(1, i + 1):
            # Each cell is the offset + its position in the row
            print(row_start_offset + j, end=" ")
        print()

pattern13(5)