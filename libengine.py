# 
# a game by Adam Binks

import pygame, input, game

def run():
	stateHandler = StateHandler()
	while True:
		stateHandler.update()


class StateHandler:
	"""handles menu and game state, runs boilerplate update code"""
	def __init__(self):
		self.data = Data()
		self.data.screen.fill((135, 206, 250))
		pygame.display.set_caption('Magus Operandi')

		self.gameHandler = game.GameHandler()


	def update(self):
		self.data.input.get()
		dt = self.data.FPSClock.tick()

		# update game/menu objs
		self.gameHandler.update(self.data, dt)

		pygame.display.update()



class Data:
	"""stores variables to be accessed in many parts of the game"""
	def __init__(self):
		self.WINDOWWIDTH, self.WINDOWHEIGHT = (1200, 800)
		self.screen = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))
		self.FPSClock = pygame.time.Clock()
		self.input = input.Input()


	def saveGame(self):
		pass


if __name__ == '__main__':
	run()