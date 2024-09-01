import sys
#passing int into a function passes a copy not the same instance
def inc(n):
    n = n + 6

n = 10

#print(n)
#inc(n)
#print(n)
#inc(n)
#print(n)
#inc(n)
#print(n)


class cls():
    def __init__(self):
        self.value = 5

def incClass(clas):
    clas.value = clas.value + 3

class1 = cls()

print(class1.value)
incClass(class1.value)
print(class1.value)