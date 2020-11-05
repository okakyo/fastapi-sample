import torch
from transformers import AutoModel,AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-japanese-whole-word-masking")
model = AutoModel.from_pretrained("../bin")





