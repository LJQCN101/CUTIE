# written by Xiaohui Zhao
# 2018-02
# xh.zhao@outlook.com
import tensorflow.compat.v1 as tf
import argparse

import tokenization
from data_loader_json import DataLoader

parser = argparse.ArgumentParser(description='Data Tokenizer parameters')
parser.add_argument('--dict_path', type=str, default='dict/vocab.txt') 
parser.add_argument('--doc_path', type=str, default='./invoice_data')
parser.add_argument('--batch_size', type=int, default=16)
params = parser.parse_args()

#class DataTokenizer(DataLoader):
    
if __name__ == '__main__':
    ## convert data into tokenized data with updated bbox
    #data_loader = DataLoader(params, update_dict=True, load_dictionary=False)
    tokenizer = tokenization.FullTokenizer(vocab_file=params.dict_path, do_lower_case=True)

