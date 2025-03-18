import math

# Noktaların tanımlanması
points = [(2, 3), (5, 5), (1, 1), (7, 9), (3, 4)]

# Öklid mesafesi hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Mesafeleri hesaplama ve distances listesine ekleme
distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):  # aynı noktaları tekrar hesaplamamak için i+1'den başlıyoruz
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)
        print(f"{points[i]} ile {points[j]} arasındaki mesafe: {distance:.2f}")

# Minimum mesafeyi bulma
min_distance = min(distances)
print(f"\nMinimum Öklid mesafesi: {min_distance:.2f}")
