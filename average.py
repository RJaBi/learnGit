import numpy as np
def mean(array):
    return np.mean(array)
def main():
    data = np.array([1.0, 2.0, 3.0, 4.0])
    ave = mean(data)
    stdDev = np.std(data)
    print(data, 'ave:',ave, 'std.dev:',stdDev)
if __name__ == '__main__':
    main()
