
"""Given a circular list of gas stations, where we can go from a station i to the next i+1, 
and the last one goes back to the first one, find the index of the station from where to start 
to be able to traverse all the tations and go back to the starting one without running out of gas.
Every station gives some gas gas[i] and every station has a cost cost[i] to go to the next one.
The answer is guaranteed to be unique and if the station we look for doesn't exist we return -1
"""

def get_gas_station(gas: list, cost: list) -> int:
    n = len(gas)
    for i in range(n):
        if traverse_from(i, gas, cost) is True:
            return i
    return -1

def traverse_from(start: int, gas: list, cost: list) -> bool:
    n = len(gas)
    nett_gas = 0
    for i in range(start, n + start):
        station = i % n
        nett_gas += gas[station] - cost[station]
        if nett_gas < 0:
            return False

    return True

gas = [1, 5, 3, 3, 5, 3, 1, 3, 4, 5]
cost =[5, 2, 2, 8, 2, 4, 2, 5, 1, 2]
expected = 8
result = get_gas_station(gas, cost)
assert result == expected, f"Wrong answer, expected: {expected} but got {result}"
