from threading import Thread
import time
import array
from ola.ClientWrapper import ClientWrapper

class DMX(Thread):
    def __init__(self, lights, effects):
        super().__init__()
        self.lights = lights
        self.running = False
        self.array = array.array('B', [0]*512)
        self.effects = effects
        self.bpm = 30

    def run(self):
        self.wrapper = ClientWrapper()
        self.running = True
        while self.running:
            self.computeEffects()
            self.computeDMX()
            self.sendDMX()
            time.sleep(50e-3)
            # time.sleep(1)

    def stop(self):
        self.running = False

    def computeEffects(self):
        t = time.perf_counter()
        effect_duration = 60/self.bpm
        t0_1 = (t%effect_duration)/effect_duration
        for effect in self.effects:
            effect(t0_1)

    def computeDMX(self):
        self.array = array.array('B', [0]*512)
        for l in self.lights:
            l.writeDMX(self.array)

    def sendDMX(self):
        client = self.wrapper.Client()
        universe = 0
        client.SendDmx(universe, self.array, lambda x: self.wrapper.Stop())
        self.wrapper.Run()

