# Python developent 1
# Start the basic game set up
# Set up display

# Access the pygame library
import pygame 

# need to initialize pygame
# in order to use any of its
# methods.
pygame.init()

# lets set up the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy'

# setting a color for the bg
# take note that tuples are used
# to identify a color (r,g,b)
AQUA_COLOR = (127, 255, 212)
ORANGE_COLOR = (255, 165, 0)
BLACK_COLOR = (0, 0, 0)

# clock & frames per second 
clock = pygame.time.Clock()
TICK_RATE = 60

# var will be used to check if
# game is completed
is_game_over = False

# now lets create a game window
# and pass it through a var
# like so:

# passing a tuple of screen width and 
# screen height through set_mode 
# to set up the screen
# # # # # # CREATING WINDOW # # # # # # 
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# screen is filled with aqua color
game_screen.fill(AQUA_COLOR) 
# display screen title
pygame.display.set_caption(SCREEN_TITLE)

# load a sprite 
player_image = pygame.image.load('images/player.png')
player_image = pygame.transform.scale(player_image, (50,50))


# Game loop
# The loop gives the game continuity
# until game is over.

while not is_game_over:

	# a loop that gets all of the events
	# currently taking place. 
	# mouse moving/clicks, keystrokes, etc..
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_game_over = True
		print(event)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# inserting sprite in game window.
	# we will use blit to complete this
	# blit(source_image, destination, area=None, special_flags = 0)
	# only concearned about source & destination, disregard the
	# other parameters.
	game_screen.blit(player_image, (375,375))


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
	# rendering
	# this updates the graphics in the game
	pygame.display.update()
	
	# tick the clock to update everything within game
	clock.tick(TICK_RATE)

# quit pygame and pgrm
pygame.quit()
quit()



