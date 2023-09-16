matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
new_matrix = lambda x: x**2
squared_matrix = [[new_matrix(x)for x in row]for row in matrix]
print(squared_matrix)
print(matrix)