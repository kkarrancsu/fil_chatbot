#!/usr/bin/env python

from kb import KBManager
from langchain_community.llms import GPT4All
from langchain import hub
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage

class GPT4AllConfig:
    def __init__(self, model_fp: str, device: str, max_tokens: int, n_predict: int, n_batch: int, temp: float, top_k: int, streaming: bool, n_threads: int, f16_kv: bool, verbose: bool, callbacks: list[BaseCallbackHandler] = []):
        self.model_fp = model_fp
        self.device = device
        self.max_tokens = max_tokens
        self.n_predict = n_predict
        self.n_batch = n_batch
        self.temp = temp
        self.top_k = top_k
        self.streaming = streaming
        self.n_threads = n_threads
        self.f16_kv = f16_kv
        self.verbose = verbose
        self.callbacks = callbacks

class GPT4AllModel:
    def __init__(self, model_config: GPT4AllConfig):
        self.model_config = model_config
        
        self.llm = GPT4All(
            model=model_config.model_fp,
            device=model_config.device,
            max_tokens=model_config.max_tokens,
            n_predict=model_config.n_predict,
            n_batch=model_config.n_batch,
            temp=model_config.temp,
            top_k=model_config.top_k,
            streaming=model_config.streaming,
            n_threads=model_config.n_threads,
            f16_kv=model_config.f16_kv,
            verbose=model_config.verbose,
            callbacks=model_config.callbacks,
        )

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

"""
Focus on reducing hallucinations!

Next Steps:
1 - include more static context.  I observe that initial queries usually fail, but subsequent queries don't when 
the user provides more details/context.  This should be automated so that it is easier to use.

2 - improve the information retrieval from the KB, as that will be the main source of context.
     - try hybrid search (keyword + semantic)
     - rank documents based on a trust score
     - https://blog.vespa.ai/improving-text-ranking-with-few-shot-prompting/
     - remove stop words from the query going into the IR

3 - numbers are big source of halluciations.

Evaluation Framework
 - Evaluate each step of process separately.  Separate IR evaluation, etc ...
 - Invest time in creating a great evaluation data-set
 - OpenAI Evals and Langchain Auto Evaluator
 - Adversarial Testing - I don't know is better than incorrect answer for RAG applications.

 Paper - ReQA: An evaluation for End-to-End answer retrieval models

 Good IR Evaluation Models/Practices
  - Care more about precision than recall, b/c you don't want to feed in too much context
  - 
"""

class ChatBot:
    def __init__(self, llm: GPT4AllModel, kb: KBManager):
        # TODO: expand the model type to include other types ... I think 
        # langchain already has an abstraction for this

        # Retrieve and generate using the relevant snippets of the blog.
        self.retriever = kb.retriever
        self.chat_history = []

        self.model = llm

        qa_system_prompt = """
        You are an expert in cryptocurrencies, economics, cryptoeconomics and Filecoin. \
        Use the following context and your knowledge of Filecoin, describe the question in detail first, and then attempt to answer the question. \ 
        If you don't know the answer, do not making anything up, just say that you don't know. \
        Keep the answer concise.\

        {context}"""
        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", qa_system_prompt),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{question}"),
            ]
        )
        contextualize_q_system_prompt = """Given a chat history and the latest user question \
            which might reference context in the chat history, formulate a standalone question \
            which can be understood without the chat history. Do NOT answer the question, \
            just reformulate it if needed and otherwise return it as is."""
        contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", contextualize_q_system_prompt),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{question}"),
            ]
        )
        self.contextualize_q_chain = contextualize_q_prompt | llm | StrOutputParser()

        # the general pipeline
        self.rag_chain = (
            RunnablePassthrough.assign(
                context=self.contextualized_question | self.retriever | format_docs
            )
            | qa_prompt
            | llm
            | StrOutputParser()
        )
    
    def clear_history(self):
        self.chat_history = []

    def contextualized_question(self, input: dict):
        if input.get("chat_history"):
            return self.contextualize_q_chain
        else:
            return input["question"]

    def format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    def __call__(self, question: str):
        ai_msg = self.rag_chain.invoke({"question": question, 'chat_history': self.chat_history})
        self.chat_history.extend([HumanMessage(content=question), AIMessage(content=ai_msg)])

        return ai_msg