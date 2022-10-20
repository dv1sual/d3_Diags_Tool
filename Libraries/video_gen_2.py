import ffmpeg
import os

image_folder = 'D:\\d3 Projects\\diag_start_Trinity_2022\\d3 Projects\\start\\objects\\VideoFile\\test patterns'
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
(
    ffmpeg
    .input(image_folder, framerate=25)
    .filter('deflicker', mode='pm', size=10)
    .filter('scale', size='3840:2160', force_original_aspect_ratio='increase')
    .output('movie.mov', vcodec='hap', crf=20, preset='slower', movflags='faststart', pix_fmt='rgba')
    .run()
)