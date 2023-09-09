def operation(x, y):
    return(x * y)

def print_operation_table(oper, x, y):
    for i in range(1, x + 1):
        print(*[oper(i, j) for j in range(1, y + 1)])

print_operation_table(operation, 6, 6)

