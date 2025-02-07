from metadata import metadataManager
from table import table
from utils.validators import validate_columns,validate_values

class database:
    def __init__(self):
        self.metadata = metadataManager.loadMetadata()
        self.tables = {}
        self.tables = table.load_tables()
    def load_tables(self):
        for table_name,columns in self.metadata.items():
            self.tables[table_name] = table(table_name,columns)
    def save_metadata(self):
        metadataManager.saveMetadata(self.metadata)
