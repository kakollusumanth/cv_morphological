import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread(r'C:\smarties.png',0)
_,mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernal=np.ones((5,5),np.uint8)
dilation=cv2.dilate(mask,kernal,iterations=1)
erosion=cv2.erode(mask,kernal,iterations=1)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)# Erosion followed by Dilation
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)# Dilation followed by Erosion
mg=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)#dilation minus erosion
bh=cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernal)
th=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)#think so mask minus opening
add=cv2.add(mg,erosion)
titles=['image','mask','dil','erosion','opening','closing','mg','bh','th']
images=[img,mask,dilation,erosion,opening,closing,mg,bh,th]
for i in range(9):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()    
