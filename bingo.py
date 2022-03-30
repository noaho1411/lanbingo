import random

def main():
	global playercard
	cardnumbers=[]
	playercard=[[0 for i in range(5)] for i in range(5)]
	for i in range(0, 5):
		for x in range(0,5):
			while playercard[i][x] == 0:
				r=str(random.randint(1,75))
				if r not in cardnumbers:
					playercard[i][x] = r
			cardnumbers.append(playercard[i][x])

	return playercard

def draw(bingonumbers):
	bingonumber=0
	while bingonumber == 0:
		r=str(random.randint(1,75))
		if r not in bingonumbers:
			bingonumber = r
		bingonumbers.append(r)
	input("")
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	print("\nThe number is " + bingonumber + "!\n\nPress enter to get next number... ")
	#main.conn.send(bingonumber.encode())
	return bingonumbers,bingonumber


def afterdraw(playercard,bingonumber):
	bingo=False
	checknumber(playercard,bingonumber)
	printcard(playercard)
	if checkbingo(playercard):
		print("Yay! bingoooooooooooo\n")
		bingo=True
	return playercard,bingo


def checkbingo(playercard):
	for i in range(0,5):
		bingoX=True
		bingoY=True
		for x in range(0,5):
			if "x1" not in str(playercard[i][x].encode('unicode_escape')):
				bingoX=False
			if "x1" not in str(playercard[x][i].encode('unicode_escape')):
				bingoY=False
		if bingoX or bingoY:
			return True



def checknumber(playercard,bingonumber):
	for i in range(0,5):
		for x in range(0,5):
			if playercard[i][x] == bingonumber:
				fill([i,x],playercard)

def printcard(playercard):
	for x in playercard:
		print(*x , sep="\t")
		print("")

def fill(position, playercard):
	playercard[position[0]][position[1]] = '\033[92m' + playercard[position[0]][position[1]] + '\033[0m'


if __name__ == "__main__":
	main()