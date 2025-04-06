
import ffmpeg

(
    ffmpeg
    .input('images/*.png', pattern_type='glob', framerate=25)
    .output('reel.mp4', crf=20, preset='slower', movflags='faststart', pix_fmt='yuv420p')
    .run()
)