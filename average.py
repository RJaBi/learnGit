import numpy as np
def mean(array):
    count=0
    sum = 0
    for x in array:
        sum = sum + x
        count = count + 1
    return float(sum)/float(count)
def main():
    data = np.array([1.0, 2.0, 3.0, 4.0])
    ave = mean(data)
    stdDev = np.std(data)
    print(data, 'ave:',ave, 'std.dev:',stdDev)
if __name__ == '__main__':
    main()
