def print_triangular_numbers(n):
    trinum=1
    for num in range(n):
        print(num+1,trinum)
        trinum=num+trinum+2
print_triangular_numbers(5)
