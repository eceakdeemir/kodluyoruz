
points = [(1,2),(2,3),(3,4)]

def euclideanDistance(coordinate1,coordinate2):
    return pow(pow(coordinate1[0] - coordinate2[0],2) + pow(coordinate1[1] - coordinate2[1],2),0.5)

distances = []

for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i],points[j]))

print(min(distances))