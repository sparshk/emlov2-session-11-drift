import timm
import urllib
import requests
import torch
import json
import hydra
from omegaconf import DictConfig, OmegaConf
from PIL import Image
from timm.data import resolve_data_config
from timm.data.transforms_factory import create_transform
import logging
logging.disable()

import pyrootutils

root = pyrootutils.setup_root(
    search_from=__file__,
    indicator=[".git", "pyproject.toml"],
    pythonpath=True,
    dotenv=True,
)

@hydra.main(version_base="1.2", config_path=root / "configs", config_name="predict.yaml")
def inference(cfg: DictConfig):

    model_name = cfg.model
    image_url = cfg.image
    # load model
    model = timm.create_model(model_name, pretrained=True)
    model.eval()

    # load image
    config = resolve_data_config({}, model=model)
    transform = create_transform(**config)
    img = Image.open(requests.get(image_url, stream=True).raw).convert("RGB")
    tensor = transform(img).unsqueeze(0)

    # get model_predictions
    with torch.no_grad():
        out = model(tensor)
    probabilities = torch.nn.functional.softmax(out[0], dim=0)

    # Get imagenet class mappings
    url, filename = (
        "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt",
        "imagenet_classes.txt",
    )
    urllib.request.urlretrieve(url, filename)
    with open("imagenet_classes.txt", "r") as f:
        categories = [s.strip() for s in f.readlines()]

    # return the required json with the top label and confidence score
    top_prob, top_catid = torch.topk(probabilities, 1)
    res_json = dict()
    for i in range(top_prob.size(0)):
        res_json["predicted"] = categories[top_catid[i]]
        res_json["confidence"] = top_prob[i].item()

    print(json.dumps(res_json))


if __name__ == "__main__":
    inference()