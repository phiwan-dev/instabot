
from kokoro import KPipeline
import soundfile
import os
import numpy as np

pipeline = KPipeline(lang_code='a', repo_id='hexgrad/Kokoro-82M')
text = '''
Hey everyone, and welcome back to my channel! Today, I'm so excited to dive into a concept that's been inspiring me lately: Art Nouveau! It's a style that just oozes elegance, nature, and a touch of magic. I'm exploring this through a slideset focusing on two gorgeous colors: a deep, lush Moss Green and a dreamy, ethereal Amethyst Dream. I love how these colors together evoke a sense of ancient forests meeting twilight skies. It's all about that flow, that organic movement you see so beautifully in Art Nouveau. The Moss Green really grounds the design, bringing in that connection to nature – think vines, leaves, and the feeling of being surrounded by growth. And the Amethyst Dream? That’s the touch of fantasy, the shimmer of moonlight, the feeling of something otherworldly. I wanted to capture that balance – that groundedness and that dreaminess. Look at how these lines curve and flow! That’s a hallmark of Art Nouveau. It’s not about sharp angles or rigid structures; it’s about embracing the natural forms around us. I tried to incorporate that fluidity into every element of this slideset. I really hope this slideset inspires you to explore your own creativity! Whether you're a designer, an artist, or just someone who appreciates beauty, I think there's something truly special about Art Nouveau. What do you think of this color combination? Let me know in the comments below! Thanks for watching! Don't forget to like and subscribe for more creative explorations. Until next time!
'''

#voices: list[str] = ["af_alloy", "af_aoede", "af_bella", "af_heart", "af_jessica", "af_kore", "af_nicole", "af_nova", "af_river", "af_sarah", "af_sky"]
voices: list[str] = ["af_heart", "af_bella"]

if not os.path.exists('audio'):
    os.makedirs('audio', exist_ok=True)

for voice in voices:

    audios = []
    generator = pipeline(text=text, voice=voice)
    for (letters, phonemes, audio) in generator:
        audios.append(audio)

    concatenated = np.concatenate(audios, axis=0)
    soundfile.write(f'audio/{voice}.wav', concatenated, 24000)

