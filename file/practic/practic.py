# f = open('text.txt', 'r')
# print(f.read())

# for i in f:
#     print(i)

# print(f.readlines())
# f.close()

# with open('text.txt', 'r') as f:
#     print(*f)
f = open('../text.txt', 'a')
f.write('\nrim')
f.close()
f = open('../text.txt', 'r')
print(f.readlines())
f.close()