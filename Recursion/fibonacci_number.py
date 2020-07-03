#elegant solution
def get_fib(position):
    if position < 2:
        return position    
    return get_fib(position-2)+ get_fib(position-1)

def fib_num(prev_2, prev_1, N):
    if N == 0:
        return prev_1+prev_2
    curr = prev_2+prev_1
    prev_2 = prev_1
    prev_1 = curr
    return fib_num(prev_2, prev_1, N-1)

def fib(self, N: int) -> int:
    if N <2:
        return N
    return fib_num(0,1, N-2)
        