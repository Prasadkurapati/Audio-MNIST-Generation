codebook_slots = 256
vocab_size = codebook_slots
n_head = 8
n_layer = 8
n_embd = 32
dropout = 0.1
epochs = 500
TRANSFORMER_MODEL_PATH = f'saved_models/Transformer_epochs_{epochs}.pt'
MONAI_TRANSFORMER_MODEL_PATH = f'saved_models/MONAI_Transformer_epochs_{epochs}.pt'
device = 'cuda:0'
VQVAE_PATH = 'saved_models/vqvae_monai.pth'
classes = range(10)
batch_size = 32
num_workers = 4
data_dir = '../Data'
block_size = 352
eval_folder = 'Evaluation_results'