import os
import gc
import torch
from diffusers import FluxPipeline
from diffusers import FluxTransformer2DModel
from diffusers import BitsAndBytesConfig as DiffusersBitsAndBytesConfig
from transformers import BitsAndBytesConfig as TransformersBitsAndBytesConfig
from transformers import T5EncoderModel

class Flux:

    def __init__(self) -> None:
        quant_config = TransformersBitsAndBytesConfig(load_in_8bit=True,)
        text_encoder_2_8bit = T5EncoderModel.from_pretrained(
            "flux1-schnell",
            subfolder="text_encoder_2",
            quantization_config=quant_config,
            torch_dtype=torch.float16,
        )

        quant_config = DiffusersBitsAndBytesConfig(load_in_8bit=True,)
        transformer_8bit = FluxTransformer2DModel.from_pretrained(
            "flux1-schnell",
            subfolder="transformer",
            quantization_config=quant_config,
            torch_dtype=torch.float16,
        )

        pipe = FluxPipeline.from_pretrained(
            "black-forest-labs/FLUX.1-schnell",
            transformer=transformer_8bit,
            text_encoder_2=text_encoder_2_8bit,
            torch_dtype=torch.float16,
        )
        pipe.enable_model_cpu_offload()
        self.pipe = pipe


    def generate_image(self, prompt: str, save_path: str = "images/test.png") -> None:
        pipe_kwargs = {
            "prompt": prompt,
            "guidance_scale": 3.5,
            "num_inference_steps": 10,
            "height": 1024,
            "width": 1024,
        }
        image = self.pipe(**pipe_kwargs).images[0] # type: ignore
        if not os.path.exists(save_path):
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
        image.save(save_path)


    def clear_memory(self) -> None:
        del self.pipe
        gc.collect()
        torch.cuda.empty_cache()


def test_gc() -> None:
    from time import sleep
    flux = Flux()
    flux.generate_image("A beautiful landscape with mountains and a river.")
    flux.clear_memory()
    # check if memory usage is low
    sleep(5)
