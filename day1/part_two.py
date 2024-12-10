from numpy import loadtxt

data = loadtxt("input.txt", dtype=int).T
left, right = data

left_keys = set(left)
appearance_map = {key: 0 for key in left_keys}

counter = 0
for val in right:
    try:
        appearance_map[val] += 1
    except KeyError:
        counter += 1

sum = 0
for val in left:
   sum = sum + appearance_map[val] * val

print(f"Result: {sum}")
