import matplotlib.pyplot as plt

def plot(X, y):
    plt.scatter(X,y,c='r',marker='x')
    plt.ylabel('Profit in $10,000s')
    plt.xlabel('Population of City in 10,000s')
    plt.show()