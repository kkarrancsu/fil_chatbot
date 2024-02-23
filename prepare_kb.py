#!/usr/bin/env python3

import os, glob
from fil_chatbot.kb import KBManager

cwd = os.getcwd()
full_path = os.path.join(cwd, "kb/cel/data/*.md")
gas_documents = glob.glob(full_path)
kb = KBManager(persist_directory="./fil_chatbot/filecoin_kb")
kb.add_documents(gas_documents)