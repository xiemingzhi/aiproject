import torch
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)

"""Next, let's move the pipeline to GPU to have faster inference."""

pipe = pipe.to("cuda")

"""And we are ready to generate images:"""

#prompt = "a photograph of an astronaut riding a horse"
#image = pipe(prompt).images[0]  # image here is in [PIL format](https://pillow.readthedocs.io/en/stable/)
prompt = "a photograph of an astronaut riding a horse"
image = pipe(prompt, height=256, width=256).images[0]

# Now to display an image you can either save it such as:
image.save(f"astronaut_rides_horse.png")

