N = int(input())

Fibonacci = []
Fibonacci.append(0)
Fibonacci.append(1)
for i in range(0, N+1):
    Fibonacci.append(Fibonacci[i]+Fibonacci[i+1])

print(Fibonacci[N])