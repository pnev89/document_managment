from tika import parser
from pathlib import Path
from elasticsearch_interaction import ElasticsarchInteraction


class ParsingDocuments:

    def __init__(self, elasticSearch_host: str, elasticSearch_port: int, index: str, directory: str = "resources/input_docs"):

        self.docs_directory = directory
        self.elasticSearch_host = elasticSearch_host
        self.elasticSearch_port = elasticSearch_port
        self.index = index

    def parse_docs(self):

        docs_directory = Path(self.docs_directory)

        es = ElasticsarchInteraction(
            host=self.elasticSearch_host,
            port=self.elasticSearch_port
            )

        # Loop through the files in the directory
        for file_path in docs_directory.iterdir():
            # Check if it's a file (not a directory)
            if file_path.is_file():
                print(f"Processing file: {file_path}")
                # Add your file processing logic here

                # Parse the PDF file
                parsed_pdf = parser.from_file(file_path.as_posix())

                # Extract the text
                pdf_text = parsed_pdf.get('content')

                # Create a document to be indexed
                doc = {
                    "title": "PDF Document Title",
                    "content": pdf_text,
                    "timestamp": "2024-10-11T12:00:00"
                }

                es.index_document(content=doc, index=self.index)



        # Print the response
        #print(response)
