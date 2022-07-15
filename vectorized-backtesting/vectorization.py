import numpy as np

if __name__ == '__main__':
    v = [1, 2, 3, 4, 5]
    sm = [2 * i for i in v]
    print(sm)
    print(2 * v)
    a = np.array(v)
    print(a)
    print(f'Type of a: {type(a)}')
    print(2 * a)
    # Array 2D
    arr2D = np.arange(12).reshape((4, 3))
    print(arr2D)
    print(arr2D * 2)
    print(arr2D ** 2)
    # Sum array
    print(f'Sum array {a.mean()}')
    print(f'Sum array {np.mean(a)}')
    # Mean of Axis = 0
    print(f'Mean of Axis = 0 {np.mean(arr2D, axis=0)}')
    # Mean of Axis = 1
    print(f'Mean of Axis = 1 {np.mean(arr2D, axis=1)}')
