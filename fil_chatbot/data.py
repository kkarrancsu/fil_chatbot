#!/usr/bin/env python3

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
# from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import MarkdownTextSplitter
from langchain.text_splitter import MarkdownHeaderTextSplitter

import hashlib
import os

class VectorStoreManager:
    def __init__(self, persist_directory: str = "vector_store", embedding_fn=None):
        os.makedirs(persist_directory, exist_ok=True)
        if embedding_fn is None:
            embedding_fn=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        self.vector_store = Chroma(embedding_function=embedding_fn, persist_directory=persist_directory)
        self.injested_docs_hash_fp = os.path.join(persist_directory, "files.txt")

    def compute_file_hash(self, file_path: str) -> str:
        """
        Computes the hash (checksum) of a file's content.

        Args:
            file_path (str): Path to the file.

        Returns:
            str: Hexadecimal representation of the file's hash.
        """
        hasher = hashlib.sha256()
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()

    def update_vector_store(self, file_paths: list[str]):
        """
        Saves a vector store to disk and updates it with new documents if provided.
        If no new documents are given, loads the existing vector store from disk.

        Args:
            file_paths (list[str]): List of file paths corresponding to the new documents to add to the vector store.

        TODO: update this from Markdown Specific text
        """
        headers_to_split_on = [
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
        ]
        markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=headers_to_split_on, strip_headers=False
        )
        markdown_splitter = MarkdownTextSplitter(chunk_size=1024, chunk_overlap=128)

        existing_file_hashes = []
        if os.path.exists(self.injested_docs_hash_fp):
            with open(self.injested_docs_hash_fp, "r") as file:
                for line in file:
                    existing_file_hashes.append(line.strip())

        # Filter out any existing file paths from the new list
        new_file_paths = [fp for fp in file_paths if self.compute_file_hash(fp) not in existing_file_hashes]

        # Check if new documents are provided
        if new_file_paths:
            # Example: Load new documents based on the new file paths
            new_docs = []
            for fp in file_paths:
                assert os.path.exists(fp), f"File not found: {fp}"
                assert os.path.splitext(fp)[1] == ".md", f"Invalid file type: {fp}"
                markdown_text = open(fp, "r").read()
                md_header_splits = markdown_splitter.split_text(markdown_text)
                docs = markdown_splitter.create_documents(md_header_splits)
                new_docs.extend(docs)

            # Add new documents to the vector store
            self.vector_store.add_documents(new_docs)
            # Update the file paths associated with the vector store
            with open(self.injested_docs_hash_fp, "a") as file:
                for fp in new_file_paths:
                    file.write(self.compute_file_hash(fp) + "\n")

            print(f"Vector store updated with {len(new_docs)} new documents.")
            self.vector_store.persist()
        else:
            print("No new documents found. Vector store remains unchanged.")
