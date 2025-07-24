
#import torch
#import gc
from time import sleep
from word import Post
from flux_quantized import Flux
from audio import AudioGenerator
from video import Video


#gc.collect()
#torch.cuda.empty_cache()


# word
    # image prompts
    # caption
    # perhaps comment
    # vlog script
my_post = Post(236)
my_post.choose()
print(my_post)
my_post.generate_text()
print("caption:")
print(my_post.caption+"\n")
print("comment:")
print(my_post.comment+"\n")
print("transcript:")
print(my_post.transcript+"\n")
my_post.save()


# flux
    # images
sleep(3)
flux = Flux()
for i in range(my_post.len):
    flux.generate_image(my_post.flux_prompts[i], f"images/{my_post.id}/{i}.png")
flux.clear_memory()
print("Generated images\n")
sleep(3)


# audio
    # audio
audio_generator = AudioGenerator()
audio = audio_generator.run(my_post.transcript, "af_bella")
audio_generator.save(audio, f"images/{my_post.id}/audio.wav")
print(f"Generated audio\n")


# video
    # reel_intro
    # reel_main
    # reel_total
vid = Video(my_post.id)
vid.render_intro()
vid.render_main()
vid.render_total()
print("Generated video\n")


# api-instagram

