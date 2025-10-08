# Property with computation and setter validation

# Tempature class --> celsius --> fahrenheit --> error - Temp below absolute zero is not allowed

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not allowed!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32


t = Temperature(25)
print("Celsius:", t.celsius)
print("Fahrenheit:", t.fahrenheit)

t.celsius = 100
print("Updated Fahrenheit:", t.fahrenheit)

t.celsius = -300