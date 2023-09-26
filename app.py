#Design Pattern/Clean code
#DRY - DO NOT REPEAT YOURSELF

j = 0
for i in range(1,50):
    if i % 2 != 0:
        continue
    print(j)
    j += i
print(j)

#git add, git commit - stage//snapshot

