
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
		direction = 0

		player_character = PlayerCharacter ('images/player.png', 375, 700, 50, 50)
		enemy_character = EnemyCharacter('images/enemy.png', 20, 400, 50, 50)

		while not is_game_over:

			# a loop that gets all of the events
			# currently taking place. 
			# mouse moving/clicks, keystrokes, etc..
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					is_game_over = True
				
				# Detect if any key is pressed down
				elif event.type == pygame.KEYDOWN:
					
					# Traverse up if up key is pressed
					if event.key == pygame.K_UP:
						direction = 1

					# Traverse down if down key is pressed
					elif event.key == pygame.K_DOWN:
						direction = -1

				# Detect if a key is released
				elif event.type == pygame.KEYUP:
					
					# stop moving if key is released
					if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
						direction = 0
				print(event)

			#redraw screen
			self.game_screen.fill(AQUA_COLOR)

			# update and draw character positioning
			player_character.move(direction)
			player_character.draw(self.game_screen)

			#update and draw enemy positioning
			enemy_character.move(self.width)
			enemy_character.draw(self.game_screen)

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

class GameObject:

	def __init__(self, image_path, x, y, width, height):
		# load a sprite 
		object_image = pygame.image.load(image_path)
		
		# Scale image up 
		self.image = pygame.transform.scale(object_image, (width,height))
		
		self.x_pos = x
		self.y_pos = y
		self.width = width
		self.height = height

	# Draw the game object by blitting
	def draw(self, background):
		background.blit(self.image, (self.x_pos, self.y_pos))

# class for a playable character in game
class PlayerCharacter(GameObject):

	# speed at which the character will move
	SPEED = 10

	def __init__(self, image_path, x, y, width, height):
		super().__init__(image_path, x, y, width, height)

	# direction = is the player moving up or down?
	def move(self, direction):
		# if the direction is greater than 0
		# move up
		# if y_pos is less than 0, stop.
		if direction > 0 and self.y_pos > 20:
			self.y_pos -= self.SPEED
		
		# if greater than 0
		# move down
		# if y_pos is greater than 700 stop.
		elif direction < 0 and self.y_pos < 700:
			self.y_pos += self.SPEED
			
class EnemyCharacter(GameObject):

	# speed at which the character will move
	SPEED = 10

	def __init__(self, image_path, x, y, width, height):
		super().__init__(image_path, x, y, width, height)

	# Enemy will be moving left and right
	def move(self, max_width):

		# if the enemy is at the far left bound
		# change directions
		if self.x_pos <= 20:
			self.SPEED = abs(self.SPEED)

		elif self.x_pos >= max_width - 50:
			self.SPEED = -abs(self.SPEED)

		self.x_pos += self.SPEED

		






# initialize pygame
# to use any of its methods.
pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()


# quit pygame and pgrm
pygame.quit()
quit()

# load a sprite 
#player_image = pygame.image.load('images/player.png')
#player_image = pygame.transform.scale(player_image, (50,50))



