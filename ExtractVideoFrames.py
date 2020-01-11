import argparse
parser = argparse.ArgumentParser()
parser.add_argument('source_dir', action='store', 
                    help='Provide the path to the game to extract frames from')

parser.add_argument('source_name', action='store',
                    help='Provide the name of the game to cluster frames with')

parser.add_argument('write_dir', action='store', 
                    help='Provide the path to write the extracted frames to')
args = parser.parse_args()
print(args.source_dir)
print(args.write_dir)

import cv2
import imutils
import os
from PIL import Image
import numpy as np
import imageio

vc = cv2.VideoCapture(args.source_dir)
count = 1
success = 1
while success:
    success, frame = vc.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(frame)
    img = np.array(img.resize((180, 320), Image.NEAREST))
    imageio.imwrite(args.write_dir+'/'+args.source_name+'-'+str(count)+'.jpg',img)
    print(count)
    count += 1

vc.release()
print('Finished extracting: ' + str(count) + 'frames from: ' + str(args.source_dir))