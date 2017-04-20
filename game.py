
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

#To make things easier, create a key dictionary...
keys = {
	"right": 275,
	"left": 276,
	"up": 273,
	"down": 274
}

# Create a 'keys down' dictionary
keys_down = {
	"right": False,
	"left": False,
	"up": False,
	"down": False
}

#Create a hero dictionary...
hero = {
	"x": 100,
	"y": 100,
	"speed": 20
}


#	Create a tuple (which is necessary for pygame)...
screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)

#	Whatever you put in here shows up at the top of the window when the game is opened...
pygame.display.set_caption("Goblin Chase")

#	Load the images...
background_image = pygame.image.load('images/background.png')
hero_image = pygame.image.load('images/koopa.png')

# Resize hero
hero_image_scaled = pygame.transform.scale(hero_image, (40,40))

#4. Create the game loop (while 1)...

#/////////////////////////////////
#/////////MAIN GAME LOOP//////////
#/////////////////////////////////

game_on = True

while game_on: 	# We are inside the main game loop. It will run as long as game_on is true.
#5. Add a quit event..

#---EVENTS----
	#Looping through all events that happened this game loop cycle 
	for event in pygame.event.get():
		#If the user has clicked on the red X to leave the game, 
		if event.type == pygame.QUIT:
			#Update our boolean so pygame can escape the loop
			game_on = False
		elif event.type == pygame.KEYDOWN:
			if event.key == keys ["up"]:
				# print "User pressed up!"
				keys_down["up"] = True
			elif event.key == keys ["down"]:
				# print "User pressed down!"
				keys_down["down"] = True
			elif event.key == keys ["left"]:
				# print "User pressed left!"
				keys_down["left"] = True
			elif event.key == keys ["right"]:
				# print "User pressed right!"
				keys_down["right"] = True
		elif event.type == pygame.KEYUP:
			# print "The user let go of a key"
			if event.key == keys["up"]:
				# The user let go of a key, and that key was the up arrow...
				keys_down["up"] = False
			if event.key == keys["down"]:
				keys_down["down"] = False
			if event.key == keys["left"]:
				keys_down["left"] = False
			if event.key == keys["right"]:
				keys_down["right"] = False

	# Update hero position
	if keys_down["up"]:
		hero["y"] -= hero["speed"]
	elif keys_down["down"]:
		hero["y"] += hero["speed"]
	if keys_down["left"]:
		hero["x"] -= hero["speed"]
	elif keys_down["right"]:
		hero["x"] += hero["speed"]


# 6. Screen fill (pass bg_color)
	#---RENDER---
	#blit (block image transfer) takes 2 arguments
		# 1. What?
		# 2. Where?  Note: (0,0) is the top right corner of the screen
	pygame_screen.blit(background_image, [0,0])

	#Draw the hero
	pygame_screen.blit(hero_image, [hero["x"],hero["y"]])

# 7. Flip the screen and start over (otherwise hero will appear to disappear, but will be behind the background image)
	pygame.display.flip()