from gpiozero import DistanceSensor
#Start a queue to record the data
distance = []
ultrosonic = DistanceSensor(echo=17, trigger=4)

#function to get rid of redundant distance
def pop_amount(amount):
        for x in range(amount):
                distance.pop()


while True:
	ultrosonicDistance = ultrosonic.distance
	distance.append(ultrosonicDistance)
	#Manage the queue
	if len(distance)>= 60:
		pop_amount(50)
	#pop the first one to ensure precision
	print(distance[0])
	if ultrosonicDistance > distance[0]:
		print('closing!!!!')
		exit()


