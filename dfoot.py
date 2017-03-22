from field import Field
from gpio_controller import GPIO_Controller
import pygame

#Screen size constants
SCREENWIDTH = 800
SCREENHEIGHT = 480
FULLSCREEN = False
led_font = 'advanced_led_board-7.ttf'
current_milli_time = lambda: int(round(time.time() * 1000))

#Start Pygame
pygame.init()
FPS = 30
fpsClock  = pygame.time.Clock()
if FULLSCREEN:
	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)
else:
	DS = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

pygame.display.set_caption("Dart Football")

input_ports = [18, 23, 24, 25, 8, 7, 12, 16, 20, 21,
				4, 17, 27, 11, 5, 6, 13, 19, 26]
				
input_chart = [ 1, 5, 10, 0, 0, 0, 0, 0, 0, 0,
				'yellow', -1, -5, 0, 0, 0, 0, 0, 0, 0,
				'touchdown', 'fumble', 'interception', 0, 0, 0, 0, 0, 0, 0,
				0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
				0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
				0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
				0, 0, 0, 0, 0, 0, 0, 0 ,0, 0,
				0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
				0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
				
field = Field()
gpio_controller = GPIO_Controller(input_ports)
exit = False

while not exit:
	active_ports = gpio_controller.poll()
	
quit	