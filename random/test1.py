words = ["hello", "world", "leona"]
process = []
for i in [w for w in words]:
    process.append(i)

print process.pop()
print process
print process.pop()
print process.pop()
print process

a_s = "abba"
for c in a_s:
    print c
