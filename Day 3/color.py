class Color:
    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b

    # @classmethod often used as alternatice constructors
    @classmethod
    def from_hex(cls, hexcode):
        hexcode = hexcode.lstrip('#')
        r = int(hexcode[1:3], 16)
        g = int(hexcode[3:5], 16)
        b = int(hexcode[5:7], 16)
        return cls(r, g, b)

c = Color.from_hex("#1e90ff")
print(c.r, c.g, c.b)
