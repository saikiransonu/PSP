    import numpy as np
    x = np.array([[1., 2., 3.], [4., 5., 6.]])
    y = np.array([[6., 23.], [-1, 7], [8, 9]])
    print(x)
    print(y)
    print(x.dot(y))
    print(np.dot(x, y))
    print(np.dot(x, np.ones(3)))
