# 평균 구하기
points = [80, 75, 55]
avg = 0

for point in points:
    avg += point

avg /= len(points)
print(avg)

avg = sum(points, 0.0) / len(points)
print(avg)
