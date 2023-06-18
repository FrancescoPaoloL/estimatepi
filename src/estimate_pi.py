import random

def estimante_pi(n):
    m = 0
    areaSquare = 4 # beacuse the area of the square is 4 (2 * 2),
    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if x*x + y*y <=1: # x*x + y*y = 1 is the simplification of sqrt(x^2 + y^2), the hypot function. 
                          # For the unit circle, x*x + y*y = 1, 
                          # so we integrate the area inside the circle with hypot (x,y) <= 1.
            m += 1
    return areaSquare * m / n if n > 0 else 0


if __name__ == '__main__':
    '''
    In this example, the estimante_pi function is called with n=100000,
    meaning that 100,000 points will be generated and used to estimate the value of π.
    '''
    estimated_value_of_pi = estimante_pi(100000)
    print("Estimated value of pi:", estimated_value_of_pi)
