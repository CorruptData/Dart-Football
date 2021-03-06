import pygame, os
from pygame.locals import *
from datetime import datetime

class Text:
	def __init__(self, text, x, y, font, size, color=None, max_width = None, scrolling = False, clickable = False, action = None):
		self.x = x
		self.y = y
		self.scroll_ticker = 0
		self.coords = (x, y)
		self.text = text.lower()
		self.tlen = len(self.text)
		self.size = size
		self.font = pygame.font.Font(font, size)
		
		self.max_width = max_width
		self.scrolling = scrolling
		
		if color == None:
			self.color = (0,0,0)
		else:
			self.color = color
		
		self.render = self.font.render(self.text, True, self.color)
		self.rect = self.render.get_rect()
		self.height = self.rect.height
		self.width = self.rect.width
		
		if self.max_width == None:
			#arbitrarily large number
			self.max_width = self.width
		
		self.clickable = clickable
		self.action = action
		self.calls = 0

	def draw(self, DS):
		self.calls+=1
		if not self.calls%30 and self.scrolling:
			self.c+=1
			if self.scroll_ticker== self.tlen:
				self.scroll_ticker = 0
		i = 0
		le = self.scroll_ticker
		while ((i+.7)*self.size*.5)<self.max_width and self.scrolling or not self.scrolling and le<self.tlen:
			char = self.text[le]
			self.render = self.font.render(char, True, self.color)
			if char is '.' or char is ':' or char is 'i':
				DS.blit(self.render, ((self.x+i*self.size*.6),self.y))
				i+=.6
			elif char is '1':
				DS.blit(self.render, ((self.x+i*self.size*.6)+self.size*.27,self.y))
				i+=1
			else:
				DS.blit(self.render, (self.x+i*self.size*.6,self.y))
				i+=1
			le+=1
			if le >= self.tlen and self.scrolling:
				le = 0
			"""
		for i in range(len(self.text)):
			self.render = self.font.render(self.text[i], True, self.color)
			DS.blit(self.render, (self.x+i*self.size*.5,self.y))"""
		
	def set_coords(self, xy):
		self.coords = xy
	
	def checkclick(self, mousex, mousey):
		return (self.y+self.height > mousey > self.y and 
				self.x+self.width > mousex > self.x)
	
	def set_text(self, new_str):
		self.text = new_str
		self.tlen = len(self.text)
		self.render = self.font.render(self.text, True, self.color)
		self.rect = self.render.get_rect()
		self.height = self.rect.height
		self.width = self.rect.width
		self.scroll_ticker = 0
		