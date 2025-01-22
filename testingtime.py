import time, pygame
from config import *

def time():
    # Initialize Pygame
    pygame.init()

    # Screen setup
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("In-Game Time Example")

    # Font for displaying time
    font = pygame.font.Font(None, 74)

    # Clock for managing time
    clock = pygame.time.Clock()

    # Tracks elapsed real time (in milliseconds)
    elapsedRealTime = 0

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get the time elapsed since the last frame in milliseconds
        deltaTime = clock.get_time()
        elapsedRealTime += deltaTime

        # Convert real elapsed time into in-game time
        elapsedGameTime = (elapsedRealTime / 1000) * (24 * 60 * 60 / DAY_DURATION)  # Scale to a 24-hour day
        gameHour = (START_HOUR + int(elapsedGameTime // 3600)) % 24
        gameMinute = int((START_MINUTE + (elapsedGameTime % 3600) // 60) % 60)

        # Format in-game time as hh:mm
        timeString = f"{gameHour:02}:{gameMinute:02}"

        # Render the time
        timeSurface = font.render(timeString, True, (255, 255, 255))  # White text
        timeRect = timeSurface.get_rect(center=(200, 150))

        # Draw everything
        screen.fill((0, 0, 0))  # Clear the screen with black
        screen.blit(timeSurface, timeRect)

        pygame.display.flip()

        # Limit frame rate
        clock.tick(60)

    pygame.quit()