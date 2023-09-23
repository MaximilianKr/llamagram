# Specify the path to the downloaded GGUF model file
# e.g. Llama2-7b
model_path = "models/llama-2-7b.Q5_K_M.gguf"


# Specify the context length (max. number of tokens)
# Default for most Llama models is 2048
# It must be enough to account for question/prompt and response
n_ctx = 4096


# If GPU support is enabled ('BLAS = 1'), adjust the values below based on your model and available VRAM
# Parameters will be ignored when running CPU support only ('BLAS = 0')
n_gpu_layers = 50	# e.g. llama-2-7b.Q5_K_M.gguf has 34 layers which can be offloaded to GPU, number can be set higher
n_batch = 1024		# number should be between 1 and 'n_ctx'
