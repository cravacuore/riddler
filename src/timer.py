class Timer():

    def __init__(self, anIO, aCPU, aQuantum):
        self.io = anIO
        self.cpu = aCPU
        self.quantum = aQuantum
        self.acc = 0

    def clock(self):
        if self.acc < self.quantum:
            self.cpu.execute()
            self.io.execute()
            self.acc += 1
        else:
            self.cpu.irq.contextSwitch()

    def setAcc(self, anAcc):
        self.acc = anAcc

