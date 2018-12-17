from color import *

def rescale(x, mini=0, maxi=100, bit=8):
    return max(0, min(2**bit-1, int((x-mini)/(maxi-mini)*(2**bit))))

class Wash:
    def __init__(self, channel):
        self.channel = channel
        self.color = Color(1.0, 1.0, 1.0)
        self.dimmer = 100.0
        self.pan = 0.0
        self.tilt = 0.0
        self.speed = 0
        self.maxPan = 540.0
        self.maxTilt = 230.0
        self.zoom = 100.0

    def writeDMX(self, arr):
        pan = rescale(self.pan, 0, self.maxPan, 16)
        tilt = rescale(self.tilt, 0, self.maxTilt, 16)
        arr[self.channel-2 + 1] = pan // (2**8)
        arr[self.channel-2 + 2] = pan %  (2**8)
        arr[self.channel-2 + 3] = tilt // (2**8)
        arr[self.channel-2 + 4] = tilt %  (2**8)
        arr[self.channel-2 + 5] = rescale(self.speed)
        for i in range(4):
            arr[self.channel-2 + 6+4*i] = rescale(self.color.r, 0, 1)
            arr[self.channel-2 + 6+4*i+1] = rescale(self.color.g, 0, 1)
            arr[self.channel-2 + 6+4*i+2] = rescale(self.color.b, 0, 1)
            # arr[self.channel-2 + 6+4*i+3] = 255
        arr[self.channel-2 + 25] = rescale(self.dimmer)
        arr[self.channel-2 + 27] = rescale(self.zoom)
        arr[self.channel-2 + 26] = 20 #shutter
