# stable-diffusion-example 

install miniconda 
create aiproject env 

```
conda list
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
```

cd stable-diffusion-example 
make sure torch gpu is working 
python torch-test.py 

run example 
```
python stable-diffusion-test.py 
```

# stable-diffusion-optimized 

requirements gpu with 8gb

install miniconda 
cd stable-diffusion-optimized 
create ldm env 
```
conda env create -f environment.yaml
conda activate ldm
```

download models 
git clone https://huggingface.co/CompVis/stable-diffusion-v-1-1-original
mv stable-diffusion-v-1-1-original models/ldm/stable-diffusion-v1/

for gpu with 4gb  
run txt2img 
```
python optimizedSD/optimized_txt2img.py --prompt "Cyberpunk style image of a Tesla car reflection in rain" --H 256 --W 256 --seed 27 --n_iter 2 --n_samples 5 --ddim_steps 50 --precision full
```
