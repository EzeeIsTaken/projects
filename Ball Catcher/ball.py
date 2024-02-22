from drawable import Drawable
import pygame

class Ball(Drawable):

    # Constructor
    def __init__(self, x=0, y=0, radius=10, color=(0, 0, 0)):
        super().__init__(x, y)
        self.__color = color
        self.__radius = radius
        self.__xSpeed = 5
        self.__ySpeed = 5

    # Draws the ball
    def draw(self, surface):
        if self.isVisible(): 
            pygame.draw.circle(surface, self.__color, self.getLoc(), self.__radius)

    # Allows the ball to move
    def move(self):
        currentX, currentY = self.getLoc()
        newX = currentX + self.__xSpeed
        newY = currentY + self.__ySpeed 
        self.setX(newX)
        self.setY(newY)
        
        surface = pygame.display.get_surface()
        width, height = surface.get_size()

        if newX <= self.__radius or newX + self.__radius >= width:
            self.__xSpeed *= -1 

        if newY <= self.__radius or newY + self.__radius >= height: 
            self.__ySpeed *= -1

    def get_rect(self):
        location = self.getLoc()
        radius = self.__radius
        return pygame.Rect(location[0] - radius, location[1] - radius, \
            2 * radius, 2 * radius)
    
    # Getter/Setter methods
    def getColor(self):
        return self.__color
    
    def setColor(self, newColor):
        self.__color = newColor

    def getRadius(self):
        return self.__radius
    
    def setRadius(self, newRadius):
        self.__radius = newRadius
        
    def setXSpeed(self, newXSpeed):
        self.__xSpeed = newXSpeed
        
    def getXSpeed(self):    
        return self.__xSpeed
    
    def setYSpeed(self, newYSpeed):
        self.__ySpeed = newYSpeed
        
    def getYSpeed(self):    
        return self.__ySpeed