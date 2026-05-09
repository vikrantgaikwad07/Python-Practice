l1 = [1,2,3,4,5,6]

n = int(input("Enter the number of rotations: "))
rt = []

rt = l1[n:] + l1[:n]

print("Rotated List: ", rt)
