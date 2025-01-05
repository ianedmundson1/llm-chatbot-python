import unittest
from dotenv import load_dotenv
from langchain.schema import AIMessage
import os
load_dotenv()

class TestStringMethods(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        from langchain_openai import AzureChatOpenAI
        cls.llm = AzureChatOpenAI()
        
        from langchain_openai import AzureOpenAIEmbeddings
        cls.embeddings = AzureOpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY_EMBEDDING"),
                                               azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT_EMBEDDING"))
    
    def test_importing_openai(self):
        assert self.llm is not None
        print(self.llm)
        print("Test passed")
    
    def test_invoking_openai(self):
        
        messages = [
            (
                "system",
                "You are a helpful assistant that translates English to French. Translate the user sentence.",
            ),
            ("human", "I love programming."),
        ]
        response = self.llm.invoke(messages)
        self.assertIsInstance(response, AIMessage)
        print(response)
        print("Test passed")
        
    def test_importing_embedding(self):
        assert self.embeddings is not None
        print(self.embeddings)
        print("Test passed")
    
    def test_embedding(self):
        
        example_text = "foo"
        embedding_result = self.embeddings.embed_query(example_text)
        print(f"Embedding result for '{example_text}': {embedding_result}")
        assert self.llm is not None
        print(self.llm)
        print("Test passed")
        
        
if __name__ == '__main__':
    unittest.main()