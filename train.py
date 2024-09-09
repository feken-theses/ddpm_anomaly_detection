from dataclasses import dataclass


@dataclass
class TrainingConfig:
    image_size =256
    image_channels = 1
    train_batch_size = 14
    eval_batch_size = 14
    num_epochs = 100
    start_epoch = 0
    learning_rate = 2e-5
    diffusion_timesteps = 800
    beta_start=1e-6
    beta_end=1e-4
    save_image_epochs = 6
    save_model_epochs = 6
    dataset = 'image/filter'
    output_dir = f'image/{dataset.split("/")[-1]}'
    device = "cuda"
    seed = 0
    resume = None
    batch_num=1000

training_config = TrainingConfig()