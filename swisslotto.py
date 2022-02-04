import random
from threading import Thread
from time import perf_counter

def draw_numbers():
    numbers = random.sample(range(1, 42), 6)
    return numbers

def draw_bonus_number():
    bonus = random.randint(1, 6)
    return bonus

def lists_are_equal(l1, l2):
    lst1 = list(l1)
    lst2 = list(l2)
    lst1.sort()
    lst2.sort()
    if lst1 == lst2:
        return True
    return False

def is_jackpot(numbers_drawn, bonus_drawn):
    if lists_are_equal(numbers_drawn, numbers_guessed) and bonus_drawn == bonus_guessed:
        return True
    return False

def draw_until_jackpot():
    count = 1
    number_hit = False
    timer_start = perf_counter()
    while not number_hit:
        numbers_drawn = list(map(int, draw_numbers()))
        bonus_drawn = draw_bonus_number()
        if is_jackpot(numbers_drawn, bonus_drawn):
            number_hit = True
        else:
            count = count + 1
    timer_stop = perf_counter()
    run_time = timer_stop - timer_start
    result.append(count)
    print(f"jackpot! attempts: {count}, time: {run_time}s")

def run():
    for i in range(number_of_samples):
        print(f"run #{i+1}")
        draw_until_jackpot()

def run_on_multiple_threads():
    threads: list[Thread] = []
    for i in range(number_of_samples):
        name = f"thread-lotto-{i+1}"
        thread = Thread(target=draw_until_jackpot, name=name)
        threads.append(thread)

    for thread in threads:
        thread.start()
        print(f"started {thread.name}")
    
    for thread in threads:
        thread.join()

def get_average_from_ints(int_list: list[int]):
    return sum(int_list) / len(int_list)

if __name__ == "__main__":
    print("START")
    result: list[int] = []
    number_of_samples = 3
    numbers_guessed = [4, 6, 12, 17, 23, 24]
    bonus_guessed = 5
    try:
        #run()
        run_on_multiple_threads()
        
        print(result)
        print(f"average out of {number_of_samples} sample(s): {get_average_from_ints(result)}")
    finally:
        print("END")