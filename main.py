import cv2
import glob

from camera import calibrate_camera, load_K, save_camera_props
from image import process_img_folder
from helpers import plot_img
from cloud import save_point_cloud, plot_point_cloud, plot_point_cloud_colorless
import counter

counter.init()

# Threshold
num_keep = 50

# Choose data and transform
data_sets = ["cactus_light_3_21", "cactus_light_4_2", "starbucks_4_9", "pincushion_4_13", "penguin_4_17", "cube_4_20", "pokemon_4_19"]
data = data_sets[0]
transform_options = ["SIFT", "ORB", "FLANN"]
transform = transform_options[0]
print("\n" + "-" * 60)
print("Processing " + data + " Data")
print("Using " + transform + " Transform")

# Parameters
if data == "pokemon_4_19":
    num_cameras = 18  # number of sequential images
    degree = 20       # degree of rotation between images
    distance = 175    # based on the turntable setup
    height = 0        # based on the turntable setup
else:
    num_cameras = 36  # number of sequential images
    degree = 10       # degree of rotation between images
    distance = 165.1  # based on the turntable setup
    height = 0        # based on the turntable setup
save_camera_props(num_cameras, degree, distance, height)

#! 1. calibrate and store camera parameters
print("-" * 60)
# note: take a few pictures of the OpenCV chessboard with source camera
# this only has to be done if no parameters are saved, 
# since the parameters will be saved upon first calibration
# calibrate_camera()

#! 2. calculate and store camera positions from Turntable properties
print("\n" + "-" * 60)
print("Calculating and Storing Camera Properties")
# note: settings taken from physical turntable setup.
# this function will only need to be called once, it is saved after calculation

#! 3. process a folder of images
print("\n" + "-" * 60)
print("Processing Images into Point Cloud")

folder = data + "\PNG" # where the source images are stored
loop = True     # True iff images are taken in a loop 
cloud_pts, cloud_rgb = process_img_folder(folder, loop)

#! 4. save and store the results
print("\n" + "-" * 60)
print("Saving Point Cloud")
save_point_cloud(cloud_pts, cloud_rgb, "prinplup")
plot_point_cloud(cloud_pts, cloud_rgb)