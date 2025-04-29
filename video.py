
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
    # upscale to fix jitter from zoom
    .filter(
        'scale',
        w="5000",
        h='-1',  # maintain aspect ratio
        force_original_aspect_ratio='decrease'
    )
    .filter(
        'zoompan',
        z=f'min(zoom+0.001, 1.9)',          # Zoom factor expression. Constant means zoom TO this level over 'd' frames.
                                    # Can use expressions like 'min(zoom+0.001, 1.5)' for continuous zoom.
        x='(iw-iw/zoom)/2',     # X position expression (centers horizontally)
        y='(ih-ih/zoom)/2',     # Y position expression (centers vertically)
        d=15,                # Duration of the zoom/pan effect FOR EACH input frame, in number of OUTPUT frames.
        s="720x1280",          # Output frame size (WidthxHeight)
        fps="30"              # Frame rate of the output FROM THIS FILTER.
    )
    .output("reel_intro.mp4", vcodec="libx264", r=30, pix_fmt="yuv420p", t=intro_length)
    .run(overwrite_output=True)
)