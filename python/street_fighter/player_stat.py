from pygame import font

class PlayerStat:
    def __init__(self, name, color, value = 100, minimum = 0, maximum = 100):
        self.name = name
        self.value = value
        self.color = color
        self.minimum = minimum
        self.maximum = maximum

    # increase the stat by an amount
    def increase(self, amount):
        self.value += amount

        if (self.value > self.maximum):
            self.value = self.maximum

        return self.value

    def reload(self):
        self.value= self.maximum

    # decrease the stat by an amount
    def decrease(self, amount):
        self.value -= amount

        if (self.value < self.minimum):
            self.value = self.minimum

        return self.value

    # checks if the stat is empty (at its minimum value)
    def isEmpty(self):
        return self.value == self.minimum

    # checks if the stat is full (at its maximum value)
    def isFull(self):
        return self.value == self.maximum

    # draws the stat bar on the specified window
    # NOTE: this does NOT update the display
    def drawBar(self, surface, x, y, width, height):
        fontSize = 20;
        drawFont = font.SysFont("arial", fontSize)
        
        text = drawFont.render(self.name.title() + ": " + str(self.value), True, (255, 0, 0))
        surface.blit(text, (x+(width/2)-(text.get_width()/2), y))
        
        ratio = width / self.maximum
        displayWidth = ratio * self.value;

        backColor = (100, 100, 100) # gray
        frontColor = self.color

        gap = 10;
        
        surface.fill(backColor, (x, y+fontSize+gap, width, height))
        surface.fill(frontColor, (x, y+fontSize+gap, displayWidth, height));
