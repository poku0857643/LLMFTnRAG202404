from transformers import RagTokenizer, RagRetriever, RagTokenForGeneration

class Llama3RAGModel:
    def __init__(self):
        # Load the RAG model (Llama3 + retriever)
        self.tokenizer = RagTokenizer.from_pretrained('facebook/rag-token-base')
        self.retriever = RagRetriever.from_pretrained('facebook/rag-token-base', index_name = 'custom')
        self.model = RagTokenForGeneration.from_pretrained('medFTLlama3')

    def generate_answer(self, question):
        # Tokenize the input question
        inputs = self.tokenizer(question, return_tensors='pt')

        # Retrieve context documents
        retriever_outputs = self.retriever(question, return_tensors='pt')

        # Generate an answer using the retrieved documents
        generated_ids = self.model.generate(input_ids=inputs['input_ids'], context_input_ids=retriever_outputs['context_input_ids'])

        return self.tokenizer.decode(generated_ids[0], skip_special_tokens=True)