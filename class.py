class Bicycle:

    def __init__(self, brand, type, wheel_size:str, color, weight): 
        self.brand = brand
        self.type = type
        self.wheel_size = wheel_size
        self.color = color
        self.weight = weight 

    def __repr__(self):
        return f"Bicycle = '{self.brand}', it is a '{self.type}' bike, and their wheel size are '{self.wheel_size}',colours are '{self.color}', and it weighs '{self.weight}'"
    
    def accelerate(self, speed):
        self.speed = speed 
    
User = Bicycle('Pinarello', 'Road', '700c', 'Red', '7.86kg')
print(User)