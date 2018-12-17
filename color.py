import colorsys

class Color:
    def __init__(self):
        self.__init__(0, 0, 0)

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return "Color(" + repr(self.r) + ", " + repr(self.g) + ", " + repr(self.b) + ")"

    def fromHSV(self, h, s, v):
        (self.r, self.g, self.b) = colorsys.hsv_to_rgb(h, s, v)

    def toHSV(self):
        return colorsys.rgb_to_hsv(self.r, self.g, self.b)

    @property
    def h(self):
        return self.toHSV()[0]
    @h.setter
    def h(self, value):
        (h, s, v) = self.toHSV()
        self.fromHSV(value, s, v)

    @property
    def s(self):
        return self.toHSV()[1]
    @s.setter
    def s(self, value):
        (h, s, v) = self.toHSV()
        self.fromHSV(h, value, v)

    @property
    def v(self):
        return self.toHSV()[2]
    @s.setter
    def s(self, value):
        (h, s, v) = self.toHSV()
        self.fromHSV(h, s, value)

