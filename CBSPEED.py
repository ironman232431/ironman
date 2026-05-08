# Read the threshold X and current speed Y
x, y = map(int, input().split())

# Check if current speed is above the limit
if y > x:
    print("YES")
else:
    print("NO")
