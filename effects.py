class EffectHue:
    def __init__(self, wash):
        self.wash = wash

    def __call__(self, t):
        self.wash.color.h = t

