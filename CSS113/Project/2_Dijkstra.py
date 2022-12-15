import math
def dijkstra(matrix, source, dest):
  distances = [math.inf for i in range(len(matrix))]
  visited = [False for i in range(len(matrix))]
  distances[source] = 0
  # เข้า node ที่ยังไม่ได้เข้า
  while False in visited:
    # หา node ที่ยังไม่ได้เข้าที่มีค่าน้อยที่สุด
    min_distance,min_index= math.inf,None
    for i in range(len(matrix)):
      if not visited[i] and distances[i] < min_distance:
        min_distance = distances[i]
        min_index = i
        print(min_index)
    if min_index is None:
      break
    # update ระยะทางของ node ที่ยังไม่ได้เข้า โดยเช็คว่า ระยะทางที่เข้ามาใหม่น้อยกว่าระยะทางเดิมหรือไม่ ถ้าน้อยกว่าให้เปลี่ยน ถ้าไม่ดึงตัวเดิม
    for i in range(len(matrix)):
      if matrix[min_index][i] != 0 and distances[i] > distances[min_index] + matrix[min_index][i]:
        distances[i] = distances[min_index] + matrix[min_index][i]
    # ทำให้ node ที่เข้าแล้วไม่เข้าใหม่
    visited[min_index] = True
    # หยุดเมื่อเข้า node ที่ต้องการ
    if visited[dest]:
      break
  return distances[dest]
num = int(input("How many Points do you have? :"))
print("Please Enter value of Adjacncy Matix (Ex.0 1 3 0)")
adjacency_matrix = [[int(i) for i in input().split()] for k in range(num)]
start = int(input("Enter the Start Point: "))
end = int(input("Enter the End Point: "))
distance = dijkstra(adjacency_matrix, start, end)
# print the shortest distance from node s to node d
print("The Shortest Path From Dijkstra's Algorithm at Point {} to Point {} is \033[4m\033[1m{}" .format(start,end,distance))
