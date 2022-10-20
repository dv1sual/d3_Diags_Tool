import ffmpeg

(
    ffmpeg
    .input('D:\\d3 Projects\\diag_start_Trinity_2022\\d3 Projects\\start\\objects\\VideoFile\\test patterns\D3_test_16-9.png', framerate=25)
    .filter('deflicker', mode='pm', size=10)
    .filter('scale', size='3840:2160', force_original_aspect_ratio='increase')
    .output('movie.mov', vcodec='hap', crf=20, preset='slower', movflags='faststart', pix_fmt='rgba')
    .run()
)