import sys
import math
import statistics

def find_modes(numbers):
    freqencies = dict()

    for num in numbers:
        freq = freqencies.get(num, 0)
        freqencies[num] = freq +1 
    
    maxFreq = max(freqencies.values())
    modes = []
    for num in freqencies:
        if freqencies[num] == maxFreq:
            modes.append(num)
    return sorted(modes)

if __name__ == "__main__":
    argv = sys.argv[1:]
    
    numbers = [ int(num) for num in argv ]
    print("your input (in ascending order): {}".format(sorted(numbers)))
    print("sum: {:.2f}".format(sum(numbers)))
    print("mean: {:.2f}".format(statistics.mean(numbers)))
    print("med: {:.2f}".format(statistics.median(numbers)))
    print("min: {:.2f}".format(min(numbers)))
    print("max: {:.2f}".format(max(numbers)))
    print("std: {:.2f}".format(statistics.stdev(numbers)))
    print("mode: {}".format(find_modes(numbers)))
    

