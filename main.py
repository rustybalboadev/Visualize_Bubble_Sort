import random
import time
x = input("random or choice: ")
if x == 'random':
    list_size = int(input("How big of a list? "))
    bubbles = []
    for x in range(1,list_size):
        bubbles.append(x)
    random.shuffle(bubbles)
elif x == 'choice':
    bubblesInput = input("Make the list of numbers: ")
    bubbles = bubblesInput.split(',')
    bubbles = list(map(int, bubbles))
last_num = 0
times = 0
start = time.time()
while times != len(bubbles):
    for x in range(0, len(bubbles)):
        if last_num > bubbles[x] and x != 0:
            bubble1 = bubbles[x-1]
            bubble2 = bubbles[x]
            bubbles[x] = bubble1
            bubbles[x-1] = bubble2
            print("Switched! New List: {}".format(bubbles))
        else:
            last_num = bubbles[x]
    times += 1
end = time.time()
print("DONE FINISHED IN {} sec WITH A LIST SIZE OF {} Switched a total of {} times".format(end - start, len(bubbles), times))
print(bubbles)
