
def genPrimes():

    prime_list = [2]
    
    def is_a_prime(current_num):
        for num in prime_list:
            if current_num % num == 0:
                return False
        return True

    yield prime_list[0]
    candidate_num = prime_list[-1]
    while True:
        next = candidate_num + 1
        candidate_num += 1
        if is_a_prime(candidate_num):
            yield candidate_num
            prime_list.append(candidate_num)

