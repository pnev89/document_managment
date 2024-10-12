from parsing_documents import ParsingDocuments



parser = ParsingDocuments(
        directory="resources/input_docs",
        elasticSearch_host="localhost",
        elasticSearch_port=9200,
        index="text_index")

parser.parse_docs()
