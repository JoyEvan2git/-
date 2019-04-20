import pygame.font
from pygame.sprite import Group

from ship import Ship
class Scoreboard():
	def __init__(self,ai_settings,screen,stats):
		self.ai_settings = ai_settings
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.stats = stats
		
		self.prep_ships()
	def prep_ships(self):
		self.ships = Group()
		for ship_number in range(self.stats.ship_left+1):
			ship = Ship(self.ai_settings,self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
	def show_score(self):
		self.ships.draw(self.screen)