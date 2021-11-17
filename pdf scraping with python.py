import tabula as tb
import pandas as pd
import re

# source file can be any pdf which has structured data
file = '/Users/Rana/Downloads/New Compressed (zipped) Folder/1247716.pdf'
data = tb.read_pdf(file, stream=True)
print(data)
