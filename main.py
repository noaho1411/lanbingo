import socket
import sys
import time
import bingo
import threading
import time

print(" ____  _                   _\n| __ )(_)_ __   __ _  ___ | |\n|  _ \\| | '_ \\ / _` |/ _ \\| |\n| |_) | | | | | (_| | (_) |_|\n|____/|_|_| |_|\\__, |\\___/(_)\n               |___/ ")
print("			  wow\n\n")
print("Hey", socket.gethostname() + "!\n")

def main():
	if "ost" in input("Host a game, or join a game? : "):
		print("\nOkay, setting up hosting\n")
		hostname = socket.gethostname()+".local"
		hsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		ip = s.getsockname()[0]

		port = input("Enter port (leave blank for default) : ")
		if port == "":
			port=1234
		try:
			hsocket.bind((hostname, int(port)))
		except Exception as e:
			print("\nConnection unsuccessful, please try again")
			print(e)
			main()
		print("\nConnection successful!\n")
		mx = input("Enter max players (default 4) : ")
		try:
			hsocket.listen(int(mx))
		except:
			hsocket.listen(4)

		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		print("Here is your connection information:\n\n")
		print("[ip] ",ip, "\t", "[port] ", port,"\n\n")
		thread = threading.Thread(target=srvrwait, args=(hsocket,))
		thread.start()
		#cont=input("Press enter to start... \n\n")
		#thread.interrupt()



	else:
		print("\nOkay, enter game information\n")

		ssocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		hostip = input("Enter server ip : ")
		port = int(input("Enter server port : "))
		try:
			ssocket.connect((hostip, port))
		except Exception as e:
			print("Connection unsuccessful, please try again")
			print(e)
			main()

		playercard = bingo.main()
		ssocket.send((str(socket.gethostname())).encode())
		f=False
		while not f:
			message=(ssocket.recv(1024)).decode()
			if "won!" in message:
				if socket.gethostname() in message:
					print("You won!\n")
				else:
					print(message)
					print("\n")
				quit()
			print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			if "welcome" in message:
				print(message)
			else:
				print("The number is",message)
			playercard,bingov = bingo.afterdraw(playercard,message)
			if bingov:
				time.sleep(.1)
				ssocket.send("win".encode()) 

		ssocket.send("win".encode())
def broadcast(message):
	for conn in connlist:
		conn.send((message).encode())

def onclient(conn,addr):
	bingonumbers=[]
	conn.settimeout(.25)
	with conn:
		conn.send("Welcome!\n".encode())
		cname = (conn.recv(1024)).decode()
		print("\n\n[client] "+cname+" has connected")
		while True:
			#WAIT FOR THING FOR X SECONDS
			message=""
			try:
				message = (conn.recv(1024)).decode()
			except:
				pass
			if "win" in message:
				print(cname + " won!")
				broadcast(cname + " won!")
				break
			else:
				temp,f=bingo.draw(bingonumbers)
				bingonumbers.append(temp[0])
				broadcast(f)
connlist=[]
def srvrwait(hsocket):
	global connlist
	while True:
		conn, addr = hsocket.accept()
		connlist.append(conn)
		threading.Thread(target=onclient,args=(conn,addr)).start()

if __name__ == "__main__":
	main()