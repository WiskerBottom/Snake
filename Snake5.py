import pygame, random, time

pygame.display.init

width=700
height=700
screen=pygame.display.set_mode([width, height])

clock = pygame.time.Clock()

run = True


snakeX=100
snakeY=100
foodX = random.randint(2,10)
foodY = random.randint(2,10)
direction="right"
x = 0
length = 1
# length of tail
possitionpast = [0,0]

while run:
	#time.sleep(0.1)
	pygame.time.delay(100)
	x = x + 1
	if x == 5:
		x=0 #this x allows the keys to be polled faster than the screen updates

		counter = 0
		print("Length of possitionpast/2: " + str(len(possitionpast)/2))
		print("value of length: " + str(length))
		#print(possitionpast)
		while (len(possitionpast)/2) > length:
			print("Removing past positions")
			possitionpast.remove(possitionpast[counter])
			possitionpast.remove(possitionpast[counter])
			counter += 2

		possitionpast.append(snakeY)
		possitionpast.append(snakeX)

		if direction == "left":
			snakeX = snakeX - 50
			directionX = -50
		elif direction == "right":
			snakeX = snakeX + 50
			directionX = 50
		elif direction == "up":
			snakeY = snakeY - 50
			directionY = -50
		elif direction == "down":
			snakeY = snakeY + 50
			directionY = 50
		
		if snakeX == foodX * 50 and snakeY == foodY * 50:
			print("chomp")
			length = length + 1
			foodX = random.randint(2,10)
			foodY = random.randint(2,10)

		for number in range(0, length):
			#print(possitionpast)
			#print("FoodX: " + str(foodX * 50))
			#print("FoodY: " + str(foodY * 50))
			#print("possitionpast X: " + str(possitionpast[y - number * 2 + 1]))
			#print("possitionpast Y: " + str(possitionpast[y - number * 2]))
			#print(number)
			if foodX * 50 == possitionpast[(len(possitionpast)-1) - number * 2] and foodY * 50 == possitionpast[((len(possitionpast)-1)-1) - number * 2]:
				print("food rerandomizing")
				foodX = random.randint(2,10)
				foodY = random.randint(2,10)			
		
		#print("Length possitionpast: " + str(len(possitionpast)))
		#print("Length: " + str(length))
		#if len(possitionpast)-1 > length:
		#	buffer = []
		#	for number in range(0,length):
		#		buffer.append(possitionpast[len(possitionpast)-(length-number)])
		#	
		#	print(buffer)
		#	print(possitionpast)
		#	exit()
		
		for possition in range(0, length):

			screen.fill((0,0,0))
			pygame.draw.rect(screen, (50,50,50), (100,100,500,500), 0) #Gray Background
			print("SnakeX: " + str(snakeX))
			print("SnakeY: " + str(snakeY))
			pygame.draw.rect(screen, (255,0,0), (snakeX,snakeY,50,50), 0) #Head

			for segment in range(0, length):
				IdentifierX = possitionpast[(len(possitionpast)-1) - segment * 2]
				IdentifierY = possitionpast[((len(possitionpast)-1)-1) - segment * 2]
				print("segmentX: "+ str(IdentifierX))
				print("segmentY: "+ str(IdentifierY))
				print("Length: " + str(length))
				#print(possitionpast)
				pygame.draw.rect(screen, (255,255,0), (IdentifierX, IdentifierY,50,50), 0)
				
				if snakeX == IdentifierX and snakeY == IdentifierY:
					print("ouchy")
					run = False
			pygame.draw.rect(screen, (0,0,255), (foodX * 50,foodY * 50,50,50), 0)	
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_LEFT]:
		direction = "left"
		
	elif keys[pygame.K_RIGHT]:
		direction = "right"
		
	elif keys[pygame.K_UP]:
		direction = "up"
		
	elif keys[pygame.K_DOWN]:
		direction = "down"

	pygame.display.update()



pygame.quit()
