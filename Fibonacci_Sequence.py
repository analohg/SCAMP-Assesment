    def fibonacci_recursive(n):
        if n == 0:
          return 0
        if n == 1:
          return 1
        else:
          return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    def fibonacci_sequence(n):
        for i in range(n):
        print(fibonacci_recursive(i))
