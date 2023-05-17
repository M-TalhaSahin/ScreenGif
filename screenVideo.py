import numpy as np
from PIL import ImageGrab
import matplotlib.widgets as widgets
import matplotlib.pyplot as plt
import cv2
import time

global loc

#  SETTINGS
FPS = 10
SECONDS = 3

#  clik event for plot screen
def onselect(eclick, erelease):
    if eclick.ydata > erelease.ydata:
        eclick.ydata, erelease.ydata = erelease.ydata, eclick.ydata
    if eclick.xdata > erelease.xdata:
        eclick.xdata, erelease.xdata = erelease.xdata, eclick.xdata
    updateLoc((eclick.xdata, eclick.ydata,  erelease.xdata, erelease.ydata))
    #print(loc)
    plt.close()


def updateLoc(locTemp):
    globals()["loc"] = locTemp


im = ImageGrab.grab()
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
arr = np.asarray(im)
plt_image = plt.imshow(arr)
rs = widgets.RectangleSelector(ax, onselect, props=dict(facecolor='blue', edgecolor='black', alpha=0.5, fill=True))
plt.show()

arr = []
for i in range(FPS * SECONDS):
    img = ImageGrab.grab(bbox=loc)
    arr.append(img)
    time.sleep((1 / FPS) - 0.05)

print("Extracting..")
arr[0].save("array.gif", save_all=True, append_images=arr[1:], duration=1000*(1 / FPS), loop=0)
del arr
cv2.destroyAllWindows()
