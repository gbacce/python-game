
# 1. Include pygame
# 2. Init pygame
# 3. Create a screen with a size
# 4. Create the game loop (while 1)
# 5. Add a quit event (requires sys)
# 6. Screen.fill (pass bg_color)
# 7. Flip the screen and start over




# 1. Import pygame...

import pygame

# 2. Init pygame 
#	In order to use pygame, we have to run the init method...

pygame.init()

# 3. Create a screen with a size
#	Limit size to size of background image...


screen = {
	"height": 512,
	"width": 480
}

#	Create a tuple (which is necessary for pygame)...
screen_size = (screen['height'], screen['width'])
pygame_screen = pygame.display.set_mode(screen_size)

#	Whatever you put in here shows up at the top of the window when the game is opened...
pygame.display.set_caption("Goblin Chase")


#4. Create the game loop (while 1)...

game_on = True

while game_on: 	# We are inside the main game loop. It will run as long as game_on is true.
#5. Add a quit event..
	#Looping through all events that happened this game loop cycle 
	for event in pygame.event.get():
		#If the user has clicked on the red X to leave the game, 
		if event.type == pygame.QUIT:
			#Update our boolean so pygame can escape the loop
			game_on = False
