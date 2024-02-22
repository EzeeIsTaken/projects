import pygame
from ball import Ball
from paddle import Paddle
from text import Text

# Initialize Pygame
pygame.init()

# Set up the game surface
surface_width = 800
surface_height = 600
surface = pygame.display.set_mode((surface_width, surface_height))

# Define colors
DREXEL_BLUE = (7, 41, 77)

# Create game objects
myBall = Ball(400, 300, 25, DREXEL_BLUE)
sizeOfBall = myBall.getRadius()
myPaddle = Paddle(200, 25, DREXEL_BLUE)
myScoreBoard = Text("Score: 0", 10, 10)
winText = Text("Congratulations, you've won! ", 235, 275)
lostText = Text("Sorry, looks like you lost. ", 235, 275)

# Initialize game variables
running = True
score = 0
extraPoints = 0

# Set up the game clock
fpsClock = pygame.time.Clock()

# Main game loop
while running:
    surface.fill((255, 255, 255))
    myBall.draw(surface)
    myPaddle.draw(surface)
    myScoreBoard.draw(surface)
    
    # Displays the current score
    myScoreBoard.setMessage("Score: " + str(score))

    # Checks if ball touches paddle
    if myBall.intersects(myPaddle):
        myBall.setYSpeed(myBall.getYSpeed()*-1)
        if score < 30:
            score += 1 + extraPoints
            
    # Check if the ball touches the bottom of the screen
    if myBall.getY() >= surface_height - myBall.getRadius():
        if score > -5:
            score -= 1
    
    # Display win or lose message based on the player's score
    if score >= 30:
        winText.draw(surface)
        # Draw a smiley face
        pygame.draw.rect(surface, DREXEL_BLUE, (400, 170, 20, 20))
        pygame.draw.rect(surface, DREXEL_BLUE, (440, 170, 20, 20))
        pygame.draw.rect(surface, DREXEL_BLUE, (400, 210, 60, 20))
        pygame.draw.rect(surface, DREXEL_BLUE, (390, 200, 20, 20))  
        pygame.draw.rect(surface, DREXEL_BLUE, (450, 200, 20, 20))
    elif score <= -5:
        lostText.draw(surface)
        # Draw a frowny face
        pygame.draw.rect(surface, DREXEL_BLUE, (400, 170, 20, 20))
        pygame.draw.rect(surface, DREXEL_BLUE, (440, 170, 20, 20))
        pygame.draw.rect(surface, DREXEL_BLUE, (400, 210, 60, 20))
        pygame.draw.rect(surface, DREXEL_BLUE, (390, 220, 20, 20))  
        pygame.draw.rect(surface, DREXEL_BLUE, (450, 220, 20, 20))
    else:
        myBall.move()
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Shrink the ball and adjust speed if Space key is pressed
            if (event.key == pygame.K_SPACE) and myBall.getRadius() > 10:
                extraPoints += 2
                myBall.setRadius(myBall.getRadius()-5)
                myBall.setXSpeed(myBall.getXSpeed()*1.5)
                myBall.setYSpeed(myBall.getYSpeed()*1.5)
    pygame.display.update()
    fpsClock.tick(60)
exit()