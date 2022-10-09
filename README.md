<div align="center">

# Gradio Demo on Lightning-Hydra-Template (with CIFAR10 and TIMM)

[![python](https://img.shields.io/badge/-Python_3.7_%7C_3.8_%7C_3.9_%7C_3.10-blue?logo=python&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pytorch](https://img.shields.io/badge/PyTorch_1.8+-ee4c2c?logo=pytorch&logoColor=white)](https://pytorch.org/get-started/locally/)
[![lightning](https://img.shields.io/badge/-Lightning_1.6+-792ee5?logo=pytorchlightning&logoColor=white)](https://pytorchlightning.ai/)
[![hydra](https://img.shields.io/badge/Config-Hydra_1.2-89b8cd)](https://hydra.cc/)
[![black](https://img.shields.io/badge/Code%20Style-Black-black.svg?labelColor=gray)](https://black.readthedocs.io/en/stable/)
[![pre-commit](https://img.shields.io/badge/Pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![tests](https://github.com/ashleve/lightning-hydra-template/actions/workflows/test.yml/badge.svg)](https://github.com/ashleve/lightning-hydra-template/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/ashleve/lightning-hydra-template/branch/main/graph/badge.svg)](https://codecov.io/gh/ashleve/lightning-hydra-template)
[![code-quality](https://github.com/ashleve/lightning-hydra-template/actions/workflows/code-quality-main.yaml/badge.svg)](https://github.com/ashleve/lightning-hydra-template/actions/workflows/code-quality-main.yaml)
[![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)](https://github.com/ashleve/lightning-hydra-template#license)
[![contributors](https://img.shields.io/github/contributors/ashleve/lightning-hydra-template.svg)](https://github.com/ashleve/lightning-hydra-template/graphs/contributors)

<!-- <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/-Python 3.7+-blue?style=for-the-badge&logo=python&logoColor=white"></a> -->

<!-- <a href="https://pytorch.org/get-started/locally/"><img alt="PyTorch" src="https://img.shields.io/badge/-PyTorch 1.8+-ee4c2c?style=for-the-badge&logo=pytorch&logoColor=white"></a>
<a href="https://pytorchlightning.ai/"><img alt="Lightning" src="https://img.shields.io/badge/-Lightning 1.6+-792ee5?style=for-the-badge&logo=pytorchlightning&logoColor=white"></a>
<a href="https://hydra.cc/"><img alt="Config: hydra" src="https://img.shields.io/badge/config-hydra 1.2-89b8cd?style=for-the-badge&labelColor=gray"></a>
<a href="https://black.readthedocs.io/en/stable/"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-black.svg?style=for-the-badge&labelColor=gray"></a> -->

A clean and scalable template to kickstart your deep learning project 🚀⚡🔥<br>
Click on [<kbd>Use this template</kbd>](https://github.com/ashleve/lightning-hydra-template/generate) to initialize new repository.

_Suggestions are always welcome!_

</div>

<br>

## 📌  TSAI Assignment-4 by Sparsh Kedia

This is built on top of Assignment-3

**Objectives**

- To train the model using the best hyperparameters found in assignment - 3
- To script the model using torch.jit.script for inference purposes
- Use gradio to host a demo to perform inference on the scripted model

**Steps to pull docker image from dockerhub and host inference demo on the scripted model directly:**

- Pull image from dockerhub -
        ``` docker pull sparshkedia/emlov2-assignment-04:gradio_app ```
- Run the docker image pulled - 
        ``` docker run -t -p 8080:8080 sparshkedia/emlov2-assignment-04:gradio_app ```
- Open your browser and run the demo by visiting - 
        ``` 0.0.0.0:8080 ```

Uncompressed size of the container is 1.14 GB.

**Steps to train the model yourself, create the container and host the inference demo:**

- Git clone the repository - 
        ``` git clone https://github.com/sparshk/emlov2-session-04.git ```
- Change working directory to the cloned repo - 
        ``` cd emlov2-session-04 ```
- Create conda environment - 
        ``` conda create --name <env_name> ```
- Activate conda environment - 
        ``` conda activate <env_name> ```
- Install requirements - 
        ``` pip install -r requirements.txt ```       
- Run the hypermater sweep - 
        ``` python src/train_script.py experiment=cifar ```
- This will save your scripted model inside - ``` logs/train/runs/<run_time>/model.script.pt ```
- Copy this scripted model to the demo folder - 
        ``` cp -r logs/train/runs/<run_time>/model.script.pt demo/ ```
- Create the docker container using - 
        ``` make build ```
- Run the container using - 
        ``` make run ```

This will give you run the gradio service on your local machine's port 8080. You can access the demo page by opening your browser and visiting - ``` 0.0.0.0:8080 ```
