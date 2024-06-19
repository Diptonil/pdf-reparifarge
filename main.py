import os
from time import ctime
from typing import Dict

from PyPDF2 import PdfReader, PdfWriter


class PDF:
    def __init__(self, path: str) -> None:
        self.path = path

    def get_metadata(self) -> Dict[str, str]:
        try:
            with open(self.path, 'rb') as f:
                pdf = PdfReader(f)
                metadata = {key: value for key, value in pdf.metadata.items()}
                return metadata
        except Exception as e:
            print("An error seems to have occured: " + str(e))

    def get_creation_time(self) -> str:
        try:
            return ctime(os.path.getctime(self.path))
        except Exception as e:
            print("An error seems to have occured: " + str(e))

    def change_metadata(self, new_metadata: Dict[str, str], inplace: bool=False) -> None:
        try:
            reader = PdfReader(self.path)
            writer = PdfWriter()
            writer.append_pages_from_reader(reader)
            for key, value in new_metadata.items():
                writer.add_metadata({key: value})
            with open(self.path + "_changed" if not inplace else self.path, "ab") as file:
                writer.write(file)
            writer.close()
        except Exception as e:
            print("An error seems to have occured: " + str(e))


if __name__ == '__main__':
    pdf = PDF('VTUDOC_VLWKDS_1RF20EC001_PUG.pdf')
    # metadata = {'/Producer': 'PFU PDF Library 1.2.1', '/Creator': 'PaperStream Capture 1.5', '/CreationDate': "D:20240604124646+05'30'", '/ModDate': "D:20240604124646+05'30'", '/MetadataDate': "D:20240604124646+05'30'"}
    print(pdf.get_creation_time())
    # change_pdf_metadata(pdf_path, metadata)
