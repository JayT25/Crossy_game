
# Access the pygame library
import pygame 

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

# clock
clock = pygame.time.Clock()

class Game:
	# clock & frames per second 
	TICK_RATE = 60

	def __init__(self, title, width, height):
		self.title = title
		self.width = width
		self.height = height
		# passing a tuple of screen width and 
		# screen height through set_mode 
		# to set up the screen
		# # # # # # CREATING WINDOW # # # # # # 
		self.game_screen = pygame.display.set_mode((width, height))
		# screen is filled with aqua color
		self.game_screen.fill(AQUA_COLOR) 
		# display screen title
		pygame.display.set_caption(SCREEN_TITLE)

	def run_game_loop(self):
		# Game loop
		# The loop gives the game continuity
		# until game is over.
		is_game_over = False

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
			#game_screen.blit(player_image, (375,375))


		# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
			# rendering
			# this updates the graphics in the game
			pygame.display.update()
			
			# tick the clock to update everything within game
			clock.tick(self.TICK_RATE)



# need to initialize pygame
# in order to use any of its
# methods.
pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()


# End of game loop

# quit pygame and pgrm
pygame.quit()
quit()

# load a sprite 
#player_image = pygame.image.load('images/player.png')
#player_image = pygame.transform.scale(player_image, (50,50))



