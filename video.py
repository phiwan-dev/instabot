
import ffmpeg
import os

# note for variable naming:
# image = ai generated image
# frame = video frame
# length = duration in seconds

# Define FFmpeg processing
class Video:
    def __init__(self, id: int):
        self.id = id
        self.image_dir = os.path.expanduser(f"images/{id}")
        self.output_fps = 30

    # main video
    def render_main(self):
        main_lenght: int = 42-2     # length of the main part of the reel
        image_length: float = 2.0   # duration of each image is displayed
        zoom_level: float = 1.001
        (
            ffmpeg.input(os.path.join(self.image_dir, "*.png"), pattern_type="glob", loop=1)
            # upscale to fix jitter from zoom
            .filter(
                "scale",
                w="5000",
                h="-1",  # maintain aspect ratio
            )
            # zoom per image, zoom variable resets every input image
            .filter("zoompan",
                    z=f"zoom*{zoom_level}",
                    d=self.output_fps * image_length,    # d = duration of each image
                    x="iw/2-(iw/zoom/2)",
                    y="ih/2-(ih/zoom/2)",
                    s="720x1280")
            .output(f"images/{self.id}/reel_main.mp4", vcodec="libx264", r=self.output_fps, pix_fmt="yuv420p", t=main_lenght)  # H.264 codec
            .run(overwrite_output=True)
        )

    # fast intro
    def render_intro(self):
        intro_length: float = 1.9
        image_length: float = 0.2
        zoom_level: float = 1.01
        (
            ffmpeg.input(os.path.join(self.image_dir, "*.png"), pattern_type="glob", loop=1)
            # upscale to fix jitter from zoom
            .filter(
                "scale",
                w="5000",
                h="-1",  # maintain aspect ratio
            )
            # zoom per image, zoom variable resets every input image
            .filter("zoompan",
                    z=f"zoom*{zoom_level}",
                    d=self.output_fps * image_length,    # d = duration of each image
                    x="iw/2-(iw/zoom/2)",
                    y="ih/2-(ih/zoom/2)",
                    s="720x1280")
            .output(f"images/{self.id}/reel_intro.mp4", vcodec="libx264", r=self.output_fps, pix_fmt="yuv420p", t=intro_length)
            .run(overwrite_output=True)
        )

    def render_total(self):
        intro = ffmpeg.input(f"images/{self.id}/reel_intro.mp4")
        main = ffmpeg.input(f"images/{self.id}/reel_main.mp4")
        video = ffmpeg.concat(intro, main, v=1, a=0)
        audio = ffmpeg.input(f"images/{self.id}/audio.wav")
        ffmpeg.output(video,
            audio.audio, 
            f"images/{self.id}/reel_total.mp4", 
            shortest=None,  # Stops encoding when the shortest input ends
            vcodec="libx264",  # Avoid re-encoding video
            acodec="aac"    # Encode audio to AAC
        ).run(overwrite_output=True)

