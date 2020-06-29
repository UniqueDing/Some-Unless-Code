original = 'abxabcabcaby'
pattern = 'abcaby'
next = [0,]

j = 0
i = 1
while i < len(pattern):
    if pattern[i] == pattern[j]:
        j += 1
        next.append(j)
    elif j == 0:
        next.append(next[0])
    else:
        j = next[j-1]
        i -= 1
    i += 1

i = 0
j = 0
while i < len(original):
    if j == len(pattern):
        break
    if original[i] == pattern[j]:
        j += 1
    else:
        j = next[j]
    i += 1

print(original)
print(pattern)
print(next)
print(i - len(pattern) + 1)
