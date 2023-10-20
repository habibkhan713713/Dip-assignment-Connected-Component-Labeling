import cv2
import numpy as np
pos = 50
result_image = cv2.imread('img.bmp')
result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2GRAY)

# Threshold the grayscale image to create a binary image
_, result_image = cv2.threshold(result_image, 128, 255, cv2.THRESH_BINARY)
label = 50
def find(label):
    if(dict[label] != label):
        dict[label] = find(dict[label])
    return dict[label]    

dict = {}
for i in range(1,result_image.shape[0]-1):
    for j in range(1,result_image.shape[1]-1):
        if (result_image[i][j] !=0 )  :
            left = result_image[i][j-1]
            top = result_image[i-1][j]
            dig1 = result_image[i-1][j-1]
            dig2 = result_image[i-1][j+1]
            temp = [left,top,dig1,dig2]
            non_zero = [x for x in temp if x!=0]
            if  not non_zero:
               result_image[i][j] = pos
               dict[pos] =  pos;
               pos=pos+1;
               
            else:
               mini = min(value for value in temp if value != 0)
               for n in non_zero :
                   if n != mini :
                       dict[n] = mini; 
               result_image[i][j] = mini
#second Pass 
for i in range(1,result_image.shape[0]-1):
    for j in range(1,result_image.shape[1]-1):
        if (result_image[i][j] !=0 )  :
            result_image[i][j] = find(result_image[i][j])    

# Create a dictionary to map labels to colors
# Create a dictionary to map labels to colors
color_dict = {}

# Iterate through the result_image and assign colors to labels
for i in range(1, result_image.shape[0] - 1):
    for j in range(1, result_image.shape[1] - 1):
        label = result_image[i][j]
        if label != 0 and label not in color_dict:
            color_dict[label] = np.random.randint(0, 256, 3)  # Generate random colors

# Create a new colored image using the label-to-color mapping
colored_image = np.zeros((result_image.shape[0], result_image.shape[1], 3), dtype=np.uint8)

for i in range(1, result_image.shape[0] - 1):
    for j in range(1, result_image.shape[1] - 1):
        label = result_image[i][j]
        if label != 0:
            colored_image[i][j] = color_dict[label]

cv2.imshow("Labeled Image", result_image)
cv2.imshow("Colored Result", colored_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

 

