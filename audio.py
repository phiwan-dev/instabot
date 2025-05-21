
from kokoro import KPipeline
import soundfile
import os
import numpy as np
from torch import FloatTensor


class AudioGenerator:

    def __init__(self):
        self.pipeline = KPipeline(lang_code='a', device="cuda", repo_id='hexgrad/Kokoro-82M')


    def run(self, text: str, voice: str) -> np.ndarray:
        audios: list[FloatTensor]= []
        generator = self.pipeline(text=text, voice=voice, speed=1.1)
        for (letters, phonemes, audio) in generator:
            audios.append(FloatTensor(audio))
        return np.concatenate(audios, axis=0)


    def save(self, audio: np.ndarray, path: str) -> None:
        # get folder name without file name
        folder: str = "/".join(path.split("/")[0:-1])
        if not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
        
        soundfile.write(path, audio, 24000)
        

#text = '''Imagine a space that breathes. A place where the clean lines of modern design meet the organic warmth of the prairie. That's Prairie Modern Revival.
#We're drawing inspiration from Frank Lloyd Wright's iconic style – think horizontal emphasis, connection to nature – but giving it a fresh, contemporary feel. Think natural materials, warm wood tones, and a sense of spaciousness.
#And to really bring this concept to life? We’re loving Magnolia Silk. This soft, creamy hue is the perfect complement. It’s like sunlight filtering through a field of blossoms, bringing a sense of serenity 
#and understated elegance.
#Prairie Modern Revival with a touch of Magnolia Silk – a space that feels both grounded and effortlessly chic.'''
text = '''
welcome to Rustic Contemporary in Lime Green!


Tired of beige? Go bold. Go Lime Green Rustic Contemporary! Imagine raw textures meeting fresh, vibrant hues. Cozy warmth with a pop of unexpected zest! It's about bringing the outside in, with a modern twist. Effortlessly chic, uniquely you.

Follow us for more!'''

#all_voices: list[str] = ["af_alloy", "af_aoede", "af_bella", "af_heart", "af_jessica", "af_kore", "af_nicole", "af_nova", "af_river", "af_sarah", "af_sky"]
voices: list[str] = [ "af_bella", "af_heart" ]
if __name__ == "__main__":
    audio_generator = AudioGenerator()
    for voice in voices:
        audio = audio_generator.run(text, voice)
        audio_generator.save(audio, f"audio/{voice}.wav")
        print(f"Generated {voice} audio")


