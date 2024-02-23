#!/usr/bin/env python3

import os, glob
from fil_chatbot.data import VectorStoreManager as VectorStore

cwd = os.getcwd()
full_path = os.path.join(cwd, "kb/cel/data/*.md")
gas_documents = glob.glob(full_path)
vector_store = VectorStore(persist_directory="./fil_chatbot/vector_store")
vector_store.update_vector_store(gas_documents)