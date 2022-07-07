a = "hello welcome to java 2 blog"
a1 = ""
for i in range(len(a)):
    if a[i] == ' ':
        a1 = a1 + '_'
    else:
        a1 = a1 + a[i]
print(a1)    