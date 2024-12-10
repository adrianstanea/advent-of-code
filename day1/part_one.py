from numpy import loadtxt, sort, abs, sum

input_data = loadtxt("input.txt", dtype=int).T
input_data = sort(input_data)
left, right = input_data

diff = abs(left - right)
result = sum(diff)
print(f"Result: {result}")