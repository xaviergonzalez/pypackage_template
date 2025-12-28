import hydra
import wandb
from omegaconf import DictConfig, OmegaConf
from lightning.pytorch.loggers import WandbLogger

@hydra.main(config_path="configs", config_name="harness")
def main(cfg: DictConfig):
    pass