import pandas as pd
import numpy as np
from cv2 import cv2
import glob
import imutils
from imutils import paths
import os
import os.path

captcha_image = 'aaw7e.png'
# Load the image and convert it to grayscale
image = cv2.imread(captcha_image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)