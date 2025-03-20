word=input("Enter a word")
char=input("Enter a character")
count=0

for i in word:
    if i==char:
        count=count+1

print(char,"occurred",count,"times in",word)
    