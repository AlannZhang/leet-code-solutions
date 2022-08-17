# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

def fizzBuzz(n: int) -> list[str]:
    list = []

    for x in range(1, n+1):
        if x%3 == 0 and x%5 == 0:
            list.append("FizzBuzz") 
        elif x%5 == 0:
            list.append("Buzz")
        elif x%3 == 0:
            list.append("Fizz")
        else:
            list.append(str(x))

    return list
