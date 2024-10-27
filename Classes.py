class Cookie:
    def __init__(self,color) -> None:         #### Constructor
        self.color = color
    def set_shape(self, shape):               #### Method 1
        self.shape = shape
        return shape
    def cost(self, cost):                     #### Method 2
        self.cost = cost
        return cost
    
cookie_1 = Cookie('green')
cookie_2 = Cookie('Yellow')

cookie_1.set_shape("round")
cookie_1.cost(50)


print(f"The colour of cookie_1 is {cookie_1.color} and the shape is {cookie_1.shape} and price is {cookie_1.cost}")
     