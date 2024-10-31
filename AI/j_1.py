from matplotlib import pyplot as plt
import cv2

name = input("enter file name: ")

choice = ['jpg','png']
option = int(input("enter file name(1.jpg or 2.png): "))
while option >2 or option<0:
    print("wrong opotion(file type is wrong)")
    option = int(input("enter file name(1.jpg or 2.png): "))

while True:
    try:
        with open (f"{name}.{choice[option-1]}") as file:
            a = 2
            break
    except FileNotFoundError:
        print("file not found!")
    option = int(input("enter file name(1.jpg or 2.png): "))
        
image = cv2.imread(f"{name}.{choice[option-1]}")
image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
model = cv2.CascadeClassifier("model.xml")
face = model.detectMultiScale(image)

x = face[0][0]
y = face[0][1]
z = face[0][2]
a = face[0][3]

image = cv2.rectangle(image , (x,y), (x+z,y+a) , (255,0,0) , 3)


print(face)
plt.imshow(image)
plt.show()