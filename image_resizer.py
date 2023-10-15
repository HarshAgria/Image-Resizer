import cv2
import os
import win32com.client as wincom
s=wincom.Dispatch("SAPI.SpVoice")
print("Welcome to the YoYo image resizer: ")
s.Speak("Welcome to the YoYo image resizer: ")

s.Speak("Enter the image name with its extension (it should be in the same directory): ")
source=str(input("Enter the image name with its extension (it should be in the same directory): "))

s.Speak("Enter the name of the image want to get after resizing source image:  ")
destination=str(input(f"Enter the name of the image want to get after resizing {source} image:  "))

s.Speak("Enter the percentage up to which you want to resize the image source :")
scale_percent=int(input(f"Enter the percentage up to which you want to resize the image {source} :"))

src= cv2.imread(source,cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",src)

# Calcutating the scale_percent of the source image
new_width = int(src.shape[1] * scale_percent/100)
new_height = int(src.shape[0] * scale_percent/100)

# dsize
# dsize=(new_width,new_height)

# Resize image
output =cv2.resize(src,(new_width,new_height))
# output =cv2.resize(src,(dsize))

cv2.imwrite(destination,output)
s.Speak(f"The output resized image will be created in the same directory as that of {source}")
print((f"The output resized image will be created in the same directory as that of {source}"))
# cv2.waitKey(0)