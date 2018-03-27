from screeninfo import get_monitors
from PIL import Image, ImageDraw
import datetime
import math

def translateHours ( h ):
    return ((h+11)%12+1);

def translateMinutes ( m ):
    return (math.floor((m%60)/5));

def paintTime( t, pos=0, val=0, stack=[] ):
    s = False;
    for i in range (pos, 5):
        if val+values[i] == t:
            val+=values[i]
            stack[i] = values[i]
            return True;
        if val+values[i] < t:
            val += values[i]
            stack[i] = values[i]
            s = s or paintTime(t, i+1, val,stack)
            if s:
                return True;
            val -=values[i]
            stack[i] = 0
        if val+values[i] > t:
            break;
    return s;

def calculateTime():
    hoursPaint=[0,0,0,0,0]
    paintTime(hours,0,0,hoursPaint)
    minutesPaint=[0,0,0,0,0]
    paintTime(minutes,0,0,minutesPaint)
    for i in range(5):
        if hoursPaint[i] != 0:
            if minutesPaint[i] != 0:
                painting[i]=bothColor
            else:
                painting[i]=hourColor
        else:
            if minutesPaint[i] != 0:
                painting[i]=minuteColor

def createImage():
    img = Image.new("RGB", (monitor.width,monitor.height), "white")
    draw = ImageDraw.Draw(img)
    for i in range(5):
        draw.polygon(coordinates[i],painting[i],borderColor)
    img.save("fibonacciClock.jpg")

monitor = get_monitors()[0]
moduleW = round(monitor.width / 8)
moduleH = round(monitor.height / 5)

hourColor = (255,0,0)
minuteColor = (0,255,0)
bothColor = (0,0,255)
emptyColor = (0,0,0)
borderColor = "black"

now = datetime.datetime.now()
hours = now.hour
minutes = now.minute

values = [1,1,2,3,5]
painting = [emptyColor,emptyColor,emptyColor,emptyColor,emptyColor]

hours = translateHours(hours)
minutes = translateMinutes(minutes)

coordinates=[
    [
        (moduleW*2,0),
        (moduleW*3,0),
        (moduleW*3,moduleH),
        (moduleW*2,moduleH)
    ],
    [
        (moduleW*2,moduleH),
        (moduleW*3,moduleH),
        (moduleW*3,moduleH*2),
        (moduleW*2,moduleH*2)
    ],
    [
        (0,0),
        (moduleW*2,0),
        (moduleW*2,moduleH*2),
        (0,moduleH*2)
    ],
    [
        (0,moduleH*2),
        (moduleW*3,moduleH*2),
        (moduleW*3,moduleH*5),
        (0,moduleH*5)
    ],
    [
        (moduleW*3,0),
        (moduleW*8,0),
        (moduleW*8,moduleH*5),
        (moduleW*3,moduleH*5)
    ]
]

calculateTime()
createImage()
