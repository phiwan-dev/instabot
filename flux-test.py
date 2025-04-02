import torch
from diffusers import FluxPipeline
import creds


class Flux:
    def __init__(self, save_path: str) -> None:
        self.save_path = save_path

    def save_model(self, name: str = "black-forest-labs/FLUX.1-schnell"):
        from huggingface_hub import login
        login(token=creds.HUGGINGFACE_TOKEN)
        pipeline = FluxPipeline.from_pretrained(name, torch_dtype=torch.float16)
        pipeline.save_pretrained(self.save_path)

    def get_image(self, prompt: str):
            pipeline = FluxPipeline.from_pretrained(self.save_path, torch_dtype=torch.float16)
            pipeline.enable_sequential_cpu_offload()
            image = pipeline(
                prompt,
                guidance_scale=3.5,
                num_inference_steps=4,
                #generator=torch.Generator("cpu").manual_seed(0),
            ).images[0]
            image.save(f"./images/test.png")


if __name__ == "__main__":
    flux = Flux("./flux1-schnell")
    flux.get_image(prompt="a living room with a fireplace")
