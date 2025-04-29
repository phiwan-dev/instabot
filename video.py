
import ffmpeg

total_lenght: int = 10   # Total length of the video in seconds
image_count: int = 4     # Number of images to include in the video
image_framerate: float = image_count / total_lenght

# Define FFmpeg processing
# main video
(
    ffmpeg
    .input("images/209/*.png", pattern_type="glob", framerate=image_framerate)  # 1 frame per second (each image lasts 1s)
    .output("reel_main.mp4", vcodec="libx264", r=30, pix_fmt="yuv420p")  # H.264 codec, 30 fps
    .run(overwrite_output=True)
)


# fast intro
intro_length: int = 2
image_framerate: float = 5
(
    ffmpeg
    .input("images/209/*.png", pattern_type="glob", framerate=image_framerate, loop=1)
    .output("reel_intro.mp4", vcodec="libx264", r=30, pix_fmt="yuv420p", t=intro_length)
    .run(overwrite_output=True)
)