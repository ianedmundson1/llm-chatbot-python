import unittest
from dotenv import load_dotenv
from langchain.schema import AIMessage
load_dotenv()

class TestStringMethods(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        from langchain_openai import AzureChatOpenAI
        cls.llm = AzureChatOpenAI()
    
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
        
    # def test_openai_embeddings():
    #     from langchain_openai import AzureOpenAIEmbeddings
    #     embeddings = AzureOpenAIEmbeddings()
    #     assert embeddings is not None
    
if __name__ == '__main__':
    unittest.main()