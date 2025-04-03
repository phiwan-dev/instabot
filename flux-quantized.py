import torch
from diffusers import FluxPipeline
from diffusers import BitsAndBytesConfig as DiffusersBitsAndBytesConfig
from transformers import BitsAndBytesConfig as TransformersBitsAndBytesConfig
from diffusers import FluxTransformer2DModel
from transformers import T5EncoderModel

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
    "black-forest-labs/FLUX.1-dev",
    transformer=transformer_8bit,
    text_encoder_2=text_encoder_2_8bit,
    torch_dtype=torch.float16,
    #device_map="balanced",
)
pipe.enable_model_cpu_offload()
pipe.to("cuda")

pipe_kwargs = {
    "prompt": "A cat holding a sign that says hello world",
    "guidance_scale": 3.5,
    "num_inference_steps": 4,
    "height": 1024,
    "width": 1024,
}

image = pipe(**pipe_kwargs).images[0]
image.save(f"./images/test.png")


