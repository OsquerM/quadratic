from math import sqrt


def run(a: int, b: int, c: int) -> tuple:
    #TODO
    #Ambas opciones son viables 
    # x1 = (-b + ((b**2) - (4 * a * c)) ** 0.5)/ (2 * a)
    x1 = (-b + sqrt((b**2) - (4 * a * c)))/ (2 * a)

    x2 = (-b - ((b**2) - (4 * a * c)) ** 0.5)/ (2 * a)
    return x1, x2

#Representar una ecuacion de segundo grado 

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
