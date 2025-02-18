class furniture():

    def __init__(self, x, y, width, height, img, place):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = img
        self.map = place
    
    def draw(self):
        self.map.blit(self.img, (self.x, self.y))