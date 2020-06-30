def recursive_sum(number, total):
    if number == 0:
        return total
  
    total += number % 10
    number = number // 10
    return recursive_sum(number, total)

def main():
    number = 1234
    total = 0
    return recursive_sum(number, total)