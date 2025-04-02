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


if __name__ == "__main__":
    flux = Flux("./flux1-schnell")
