
import ffmpeg

seconds_per_image = 3

# Define FFmpeg processing
(
    ffmpeg
    .input("images/*.png", pattern_type="glob", framerate=1/seconds_per_image)  # 1 frame per second (each image lasts 1s)
    .output("reel.mp4", vcodec="libx264", r=30, pix_fmt="yuv420p")  # H.264 codec, 30 fps
    .run(overwrite_output=True)
)