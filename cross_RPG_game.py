
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

# initialize font
pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class Game:
	# clock & frames per second 
	TICK_RATE = 60

	def __init__(self, image_path, title, width, height):
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

		# load the image from path 
		background_image = pygame.image.load(image_path)

		# scale up the background image
		# to game screen width & height 
		self.image = pygame.transform.scale(background_image, (width, height))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 	

	def run_game_loop(self, level_speed):
		# Game loop
		# The loop gives the game continuity
		# until game is over.
		is_game_over = False
		did_win = False
		direction = 0
		enemy_count = 3

		player_character = PlayerCharacter ('images/player.png', 375, 700, 50, 50)
		
		enemies = []
		
		enemies.append(EnemyCharacter('images/enemy.png', 120, 600, 50, 50))
		enemies.append(EnemyCharacter('images/enemy.png', self.width -40, 400, 50, 50))
		enemies.append(EnemyCharacter('images/enemy.png', 220, 200, 50, 50))
		
		for x in range(len(enemies)):
			enemies[x].SPEED *= level_speed
		
		
		treasure = GameObject('images/treasure.png', 375, 50, 50, 50)
		


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
			# blit background image to screen
			self.game_screen.blit(self.image, (0,0))

			# draw treasure
			treasure.draw(self.game_screen)

			# update and draw character positioning
			player_character.move(direction)
			player_character.draw(self.game_screen)

			#update and draw enemy positioning
			for x in range(enemy_count):
				enemies[x].move(self.width)
				enemies[x].draw(self.game_screen)
			#enemy_character.move(self.width)
			#enemy_character.draw(self.game_screen)
			
				# Check collision with enemy
				# game over if true, player lost
				if player_character.detectCollision(enemies[x]):
					is_game_over = True
					did_win = False
					
					# Render game over display text after lost
					text = font.render('GAME OVER!', True, ORANGE_COLOR)
					
					# blit it to game_screen
					self.game_screen.blit(text, (300, 350))
					
					# update display to show text
					pygame.display.update()
					
					# wait a second
					clock.tick(1)
					break

			# Check collision with treasure
			# player wins, game over
			if player_character.detectCollision(treasure):
				is_game_over = True
				did_win = True

				# Render game over display text after lost
				text = font.render('YOU WON!', True, ORANGE_COLOR)
				
				# blit it to game_screen
				self.game_screen.blit(text, (275, 350))
				
				# update display to show text
				pygame.display.update()
				
				# wait a second
				clock.tick(1)
				break


			# rendering
			# this updates the graphics in the game
			pygame.display.update()
			
			# tick the clock to update everything within game
			clock.tick(self.TICK_RATE)

		# if player wins, allow the player to
		# play again. else, exit game.
		if did_win:
			self.run_game_loop(level_speed+0.5)
			
		else:
			return
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

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
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
	
	# Draw the game object by blitting
	def draw(self, background):
		background.blit(self.image, (self.x_pos, self.y_pos))
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #	
	
	def detectCollision(self, other_object):
		if (self.y_pos >= other_object.y_pos - other_object.height/1.5) and (self.y_pos <= other_object.y_pos + other_object.height/1.5):
				if (self.x_pos >= other_object.x_pos - other_object.width/1.5) and (self.x_pos <= other_object.x_pos + other_object.width/1.5):
					return True
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# class for a playable character in game
class PlayerCharacter(GameObject):

	# speed at which the character will move
	SPEED = 10

	def __init__(self, image_path, x, y, width, height):
		super().__init__(image_path, x, y, width, height)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class EnemyCharacter(GameObject):

	# speed at which the character will move
	SPEED = 10

	def __init__(self, image_path, x, y, width, height):
		super().__init__(image_path, x, y, width, height)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

	# Enemy will be moving left and right
	def move(self, max_width):

		# if the enemy is at the far left bound
		# change directions
		if self.x_pos <= 20:
			self.SPEED = abs(self.SPEED)

		elif self.x_pos >= max_width - 50:
			self.SPEED = -abs(self.SPEED)

		self.x_pos += self.SPEED
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

		






# initialize pygame
# to use any of its methods.
pygame.init()

new_game = Game('images/background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop(1)


# quit pygame and pgrm
pygame.quit()
quit()

# load a sprite 
#player_image = pygame.image.load('images/player.png')
#player_image = pygame.transform.scale(player_image, (50,50))



