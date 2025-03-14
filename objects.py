class fruits:
    def __init__(self, size, color):
        print("This is a default method")
        self.size = size
        self.color = color
    
    # displaying the details
    def display_details(self):
        print("The size of the fruit is ", self.size)
        print("The color of the fruit is", self.color)

mango = fruits("medium", "orange")
mango.display_details()

     
        