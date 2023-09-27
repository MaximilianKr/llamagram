# Llamagram

A simple telegram bot for a chat instance with your local Llama model.

Utilising [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) 
and GGUF models for CPU and GPU support.

- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [GPU support](#gpu-skip-for-cpu-only)
  - [CPU & GPU](#cpu--gpu)
- [Usage](#usage)
- [Roadmap](#roadmap)

## Prerequisites

- Generate a bot on Telegram using [@BotFather](https://t.me/BotFather)
  - set a name for your bot and obtain the `token to access the HTTP API`
  - **place the API token in `botdata/credentials.py`**

- Get a GGUF model of your choice, for example from [TheBloke on Huggingface](https://huggingface.co/TheBloke)
  - tested with [llama2_7b_chat.Q4_K_M.gguf](https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF/blob/main/llama-2-7b-chat.Q4_K_M.gguf)
  - you should be able to use any GGUF model (not only Llama2) but might 
    have to adjust the initial prompt according the model used
  - **place the path to your model file in `botdata/settings.py`**
  
## Setup

- create and activate `virtual environment`
  ```
  # Windows
  python -m venv env
  .\env\Scripts\activate
  
  # Linux
  sudo apt install python3.10-venv
  python -m venv env
  source env/bin/activate
  ``` 
  
#### GPU (skip for CPU only)

- the following steps only cover `CUDA`, if you are not using an NVIDIA 
  GPU, follow the instructions on [llama-cpp-python Github](https://github.com/abetlen/llama-cpp-python#installation-with-hardware-acceleration)
- make sure `CUDA` is installed on your system or install it according to 
  [Official Docs](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html)

- install `llama-cpp-python` with GPU support
  ```
  # Windows
  $env:FORCE_CMAKE=1
  $env:CMAKE_ARGS="-DLLAMA_CUBLAS=on"
  pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir
  
  # Linux
  CMAKE_ARGS="-DLLAMA_CUBLAS=on"
  FORCE_CMAKE=1
  pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir
  ```

#### CPU & GPU

- install `requirements`
  ```
  pip install -r requirements.txt
  ```

## Usage

After placing `API Token` and `model_path` and installing dependencies with 
either GPU or CPU support, simply run:
  ```
  python app.py
  ```
and start a chat with your bot on Telegram.


### Roadmap

- **ToDo**s
  - multi-memory / persistent memory
  - logging
  - error handling
  - skip `/start` message
  - exit / abort function
