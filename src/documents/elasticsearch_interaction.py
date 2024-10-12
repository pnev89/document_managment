from elasticsearch import Elasticsearch


class ElasticsarchInteraction:
    
    def __init__(self, host: str ="localhost", port: int = 9200):
        # Connect to the Elasticsearch instance

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
        return self.connection

    def index_document(self, content: str, index: str = "default"):
        try:
            # Attempt to index the document
            response = self.connection.index(index=index, document=content)
            print("Document indexed successfully:", response)
            return response
        except Exception as e:
            print(e)
            # Handle any other exceptions