from utils.constants import FILE_SEPARATOR,ROW_SEPARATOR
from utils.file_headler import File_headler

class table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.File_headler = File_headler(f"{name}.txt")
    def get_Headers(self):
        return list(self.columns.keys())
    def row_to_dict(self, row):
        values = row.split("FILE_SEPARATOR")
        return dict(zip(self.get_Headers(),values))
    def dict_to_row(self, row_dict):
        return FILE_SEPARATOR.join(str(row_dict.get(col,'')) for col in self.get_Headers())
    