Lenght= int(input())
width = int(input())
height = int(input())
taken_percent= float(input()) /100

volume = (Lenght * width * height) /1000
volume -= volume * taken_percent

print(f"{volume:.3f}")