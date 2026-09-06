# Generator function to yield days of the week

def days():
    d = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    i = 0
    while True:
        yield d[i]
        i = (i + 1) % 7

m = days()
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))

#Factorial of Number by Recursive Function

def fun(n):
    m = 1
    if n > 0:
        m = n * fun(n - 1)

    return m

print(fun(100))

# Fibonacci Series using Generator Function


def fib_term(n):
    a = 0
    b = 1
    for i in range(n + 1):
        
        yield a
        c = a + b
        a = b
        b = c

    
num = 10
for term in fib_term(num):
    print(term,end=" ")
    
        
