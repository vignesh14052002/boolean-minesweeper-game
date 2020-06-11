import numpy as np
import random
def createmines(n):
	global a,c,d
	a=np.zeros((n,n))
	c=a.copy()
	d=int((n*n)*(d/100))
	for i in range(d):
		while True:
			x=random.randint(0,n-1)
			y=random.randint(0,n-1)
			if a[x][y]!=1:
				a[x][y]=1
				break
	a=a.astype(int)
	c=c.astype(int)
def errorcheck():
	global x,y,n,i
	while x>=n or y>=n:
		print('index out of range , enter between 00 and ',n,n)
		i=str(input('enter position again'))
		x,y=int(i[0]),int(i[1])
	while c[x][y]==1:
		print('already checked')
		i=str(input('enter position again'))
		x,y=int(i[0]),int(i[1])
		
replay=True
while replay:	
	n=int(input('enter board size(single digit is preferrable)'))
	print('score is based on difficuilty level')
	d=int(input('enter difficuilty level (10-99)'))

	createmines(n)
	score=0
	while True:
		print(c)
		i=str(input('enter position'))
		x,y=int(i[0]),int(i[1])
		errorcheck()
		if a[x][y]!=1:
			c[x][y]=1
			score+=d
		else:
			print('game over')
			print('your score ',score)
			print('mines',a,sep='\n')
			re=str(input('enter r for replay'))
			if re!='r':
				replay=False
			break
		
	
			
		
	