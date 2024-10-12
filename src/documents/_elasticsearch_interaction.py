from elasticsearch import Elasticsearch
from typing import List

class ElasticsearchInteraction:
    """Interact with ElasticSearch.
    """    
    def __init__(self, host: str ="localhost", port: int = 9200):
        """Constructs the object.

        Parameters
        ----------
        host : str, optional
            ElasticSearch host, by default "localhost"
        port : int, optional
            ElasticSearch port, by default 9200

        Raises
        ------
        ConnectionError
            Elasticsearch is not reachable
        RuntimeError
            Cannot connect to ElasticSearch
        RuntimeError
            No Object was created
        """
        try: 
            self.connection = Elasticsearch([f'http://{host}:{port}'])
            
            # Check if the connection is established
            if not self.connection.ping():
                raise ConnectionError("Elasticsearch is not reachable.")
                
            print("Connected to Elasticsearch successfully.")
        
        except Exception as e:
            # Raise an exception if the connection fails
            raise RuntimeError(f"Failed to connect to Elasticsearch: {e}")
        
        # Raise an exception if no exception was raised but connection is still None
        if self.connection is None:
            raise RuntimeError("No connection object was created.")

    def get_connection(self):
        """Returns ElasticSearch connection.

        Returns
        -------
        connenction
            ElasticSearch connection
        """        
        return self.connection

    def index_document(self, content: str, index: str = "default")->None:
        """Indexes document to ElasticSearch.

        Parameters
        ----------
        content : str
            Content of the document
        index : str, optional
            Index where the document will be indexed, by default "default"
        """        
        try:
            # Attempt to index the document
            response = self.connection.index(index=index, document=content)
            print(f'Document indexed successfully: {response}')
            return response
        except Exception as e:
            print(e)
            # Handle any other exceptions

    def delete_document(self, index: str, doc_ids: List[str])->bool:
        """Removes document from index.

                Parameters
                ----------
                index : str
                    Index from where the document is to be removed
                doc_ids : List[str]
                    List of documents to be removed 

                Returns
                -------
                bool
                    True if deletes everything
                """     
        # Loop through the list and delete each document
        for doc_id in doc_ids:
            try:
                response = self.connection.delete(index=index, id=doc_id)
                print(f"Document ID {doc_id} deleted successfully: {response}")
                return response
            except Exception as e:
                print(f"Error deleting document ID {doc_id}: {e}")
                return None

    
    def delete_index(self, index: str) -> None:
        """Deletes an index.

        Parameters
        ----------
        index : str
            Index to be deleted
        """
        try:
            if self.connection.indices.exists(index=index):
                response = self.connection.indices.delete(index=index)
                print(f"Index '{index}' deleted successfully: {response}")
                return response
            else:
                print(f"Index '{index}' does not exist.")
                return None
        except Exception as e:
            print(f"Error deleting index '{index}': {e}")
            return None