#!/usr/bin/env python3

class Shoe:
    condition = "New"
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

#-------------Size        
    # size getter
    def get_size(self):
        return self._size
    
    #size setter
    def set_size(self,size):
        if type(size) != int:
            print("size must be an integer")
        else:
            self._size = size
            print(f"Set size: {size}")
    
    #property
    size = property(get_size,set_size)

#---------condition
    def cobble(self):
        print ("Your shoe is as good as new!")

stan_smith = Shoe("Adidas", 9)
stan_smith.cobble