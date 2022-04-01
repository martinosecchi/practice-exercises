"""
You are planning production for an order. You have a number of machines that each have a fixed number of days 
to produce an item. Given that all the machines operate simultaneously, 
determine the minimum number of days to produce the required order.
"""

def min_time(machines: list, goal: int) -> int:
    # # day by day approach
    # # days      -  1 2 3 4 5 6 7 8 9 10
    # # machine 0 -  0 1 0 1 0 1 0 1 0 1
    # # machine 1 -  0 0 1 0 0 1 0 0 1 0
    # # machine 2 -  0 1 0 1 0 1 0 1 0 1
    # # tot products 0 2 3 5 5 8 8 10 11 13
    # day = 0
    # while goal > 0:
    #     day += 1
    #     for machine in machines:
    #         if day % machine == 0:
    #             goal -= 1
    # return day
    
    # # production days only approach
    # # 2, 3, 2 - 0p
    # # 4, 3, 4 - 2p - day 2
    # # 4, 6, 4 - 3p - day 3
    # # 6, 6, 6 - 5p - day 4
    # # 8, 9, 8 - 8p - day 6
    # # 10, 9, 10 - 10p - day 8
    # m = len(machines)
    # n_products = 0
    # today = 0
    # production_days = [d for d in machines]
    # while n_products < goal:
    #     today = min(production_days)
    #     for i in range(m):
    #         p_day = production_days[i]
    #         machine_time = machines[i]
    #         if p_day == today:
    #             production_days[i] += machine_time
    #             n_products += 1
    #        
    # return today

    # search approach
    n = len(machines)
    min_days = int(goal / n + 1) * min(machines)
    max_days = int(goal / n + 1) * max(machines)

    
    def get_production_by_day(day):
        return sum([int(day / m) for m in machines])
    
    def binary_search(start, end):
        if start == end: 
            return start
    
        today = start + int((end - start) / 2)
        
        current_prod = get_production_by_day(today)
        prev_prod = get_production_by_day(today - 1)
        
        if current_prod >= goal and prev_prod < goal:
            return today
        elif current_prod >= goal and prev_prod >= goal:
            return binary_search(start, today - 1)
        else:  # current_prod < goal
            return binary_search(today + 1, end)
    
    return binary_search(min_days, max_days)


def test_from_file():
    f = open("min_time.in.txt", "r")
    n, goal = f.readline().split(" ")
    n, goal = int(n), int(goal)
    machines = [int(m) for m in f.readline().split(" ")]
    f.close()

    f = open("min_time.out.txt", "r")
    expected_result = int(f.readline())
    f.close()

    result = min_time(machines, goal)
    assert result == expected_result, f"Wrong result: {result}. Expected: {expected_result}"


# assert min_time([2, 3], 5) == 6
# assert min_time([1, 3, 4], 10) == 7
# assert min_time([2, 3, 2], 10) == 8
# assert min_time([4, 5, 6], 12) == 20
test_from_file()
