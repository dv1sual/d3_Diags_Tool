import cv2
import os

image_folder = 'D:\\d3 Projects\\diag_start_Trinity_2022\\d3 Projects\\start\\objects\\VideoFile\\test patterns'
video_name = 'video.MOV'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()