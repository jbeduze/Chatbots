def load_dataset(dataset_name:str="dataset.csv") -> pd.DataFrame:
    """
    Helper function to load the dataset

    Args:
         dataset_name (str, optional): Name of the file saved from the extraction phase. Defaults to "dataset.csv".

    Returns:
         pd.DataFrame: Pandas DataFrame of data collected by LangChain
    """
    pass

def create_chunks(dataset:pd.DataFrame, chunk_size:int, chunk_overlap:int) -> list:
    """
    Creates informational chunks from the dataset 

    Args:
        dataset (pd.DataFrame): Dataset Pandas
        chunk_size (int): How many chunks do we want?
        chunk_overlap (int): How much information should overlap among chunks?

    Returns:
        list: list of chunks
    """
    pass

def create_or_get_vector_store(chunks: list) -> FAISS:
    """
    Creates or loads the vector database locally

    Args:
        chunks: List of chunks

    Returns:
        FAISS: Vector store
    """
    pass

def get_conversational_chain(vector_store: FAISS, human_message: str, system_message: str) -> None:
    """
    Retrieves the conversational chain from LangChain
    
    Args:
        vector_store (FAISS): Vector store
        system_message (str): System message
        human_message (str): Human message
    
    Returns:
        ConversationalRetrievalChain: Chatbot conversation chain
    """    
    pass

def main():
    pass


if __name__ == "__main__":
    main()
