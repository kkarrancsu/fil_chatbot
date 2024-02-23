#!/usr/bin/env python3

import os, glob
from fil_chatbot.kb import KBManager

os.environ['GRPC_DNS_RESOLVER'] = 'native' # seems to be needed for mac ... 

cwd = os.getcwd()
full_path = os.path.join(cwd, "kb/data/*.md")
gas_documents = glob.glob(full_path)
kb = KBManager(persist_directory="filecoin_kb")
kb.add_documents(gas_documents)