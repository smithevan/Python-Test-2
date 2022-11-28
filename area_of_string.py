##area of a string
import math
sample_string = "j"

def area_of_string(initial_string):
    def string_length(input_string):
        length = len(input_string)
        return length
    radius = float(string_length(initial_string))
    pi_length = math.pi * (radius ** 2)
    
    return pi_length

print (area_of_string(sample_string)) 

    


