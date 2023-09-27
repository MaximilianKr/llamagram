from langchain.llms import LlamaCpp
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
from langchain.prompts import PromptTemplate
from botdata.settings import model_path, n_ctx, n_gpu_layers, n_batch


class LangChainMemoryBot:
    def __init__(self):
        llm = LlamaCpp(
            model_path=model_path,
            n_ctx=n_ctx,
            last_n_tokens_size=1024,
            n_gpu_layers=n_gpu_layers,
            n_batch=n_batch,
            verbose=False,

            stop=["USER:", "ASSISTANT:", "HUMAN", "RESPONSE", "###", "AI:",
                  "Human:", "\n"],
            repeat_penalty=1.1,
            max_tokens=1024,
            temperature=0.3,
            )

        # Let LLM summarise current conversation and use this as context
        # ToDo: use Langchain multi-memory
        memory = ConversationSummaryBufferMemory(
            llm=llm,
            max_token_limit=500  # 3000
        )

        self.conversation = ConversationChain(
            llm=llm,
            memory=memory,
            verbose=True,
        )

    def predict(self, prompt):
        return self.conversation.predict(input=prompt)
