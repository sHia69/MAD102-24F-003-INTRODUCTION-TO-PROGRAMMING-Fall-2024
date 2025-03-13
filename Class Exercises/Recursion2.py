# Write a Python program to generate the Fibonacci sequence up to a certain number using recursion.
def fibonacci_sequence(n):
          sequence = []
          a, b = 0, 1
          while a <= n:
                    sequence.append(a)
                    a, b = b, a + b
          return sequence

def main():
          num = int(input("Enter a number to generate the Fibonacci sequence up to: "))
          result = fibonacci_sequence(num)
          print("Fibonacci sequence up to", num, "is:", result)

if __name__ == "__main__":
          main()