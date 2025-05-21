
import ffmpeg
import os

# note for variable naming:
# image = ai generated image
# frame = video frame
# length = duration in seconds

image_dir: str = os.path.expanduser("~/nextcloud/instabot/images/209")
output_fps: float = 30

# main part of the video
main_lenght: int = 22-2     # length of the main part of the reel
image_length: float = 2.0   # duration of each image is displayed
zoom_level: float = 1.001

# Define FFmpeg processing
# main video
(
    ffmpeg.input(os.path.join(image_dir, "*.png"), pattern_type="glob", loop=1)
    # upscale to fix jitter from zoom
    .filter(
        "scale",
        w="5000",
        h="-1",  # maintain aspect ratio
    )
    # zoom per image, zoom variable resets every input image
    .filter("zoompan",
            z=f"zoom*{zoom_level}",
            d=output_fps * image_length,    # d = duration of each image
            x="iw/2-(iw/zoom/2)",
            y="ih/2-(ih/zoom/2)",
            s="720x1280")
    .output("reel_main.mp4", vcodec="libx264", r=output_fps, pix_fmt="yuv420p", t=main_lenght)  # H.264 codec
    .run(overwrite_output=True)
)


# fast intro
intro_length: float = 1.9
image_length = 0.2
zoom_level = 1.01
(
    ffmpeg.input(os.path.join(image_dir, "*.png"), pattern_type="glob", loop=1)
    # upscale to fix jitter from zoom
    .filter(
        "scale",
        w="5000",
        h="-1",  # maintain aspect ratio
    )
    # zoom per image, zoom variable resets every input image
    .filter("zoompan",
            z=f"zoom*{zoom_level}",
            d=output_fps * image_length,    # d = duration of each image
            x="iw/2-(iw/zoom/2)",
            y="ih/2-(ih/zoom/2)",
            s="720x1280")
    .output("reel_intro.mp4", vcodec="libx264", r=output_fps, pix_fmt="yuv420p", t=intro_length)
    .run(overwrite_output=True)
)



intro = ffmpeg.input("reel_intro.mp4")
main = ffmpeg.input("reel_main.mp4")
video = ffmpeg.concat(intro, main, v=1, a=0)
audio = ffmpeg.input("audio/af_bella.wav")
ffmpeg.output(video,
    audio.audio, 
    'reel_total.mp4', 
    shortest=None,  # Stops encoding when the shortest input ends
    vcodec="libx264",  # Avoid re-encoding video
    acodec='aac'    # Encode audio to AAC
).run(overwrite_output=True)

