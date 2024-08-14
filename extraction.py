# # # bring in our LLAMA_CLOUD_API_KEY
# from dotenv import load_dotenv
# load_dotenv()

# # bring in deps
# from llama_parse import LlamaParse
# from llama_index.core import SimpleDirectoryReader

# # set up parser
# parser = LlamaParse(
#     result_type="text"  # "markdown" and "text" are available
# )

# # use SimpleDirectoryReader to parse our file
# file_extractor = {".pdf": parser}
# documents = SimpleDirectoryReader(input_files=[r"C:\Users\AMALVIYA\Downloads\Acrobat Document arabic_removed.pdf"], file_extractor=file_extractor).load_data()
# print(documents)

from dotenv import load_dotenv
load_dotenv()

# bring in deps
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader

# set up parser
parser = LlamaParse(
    result_type="markdown"  # "markdown" and "text" are available
)

# use SimpleDirectoryReader to parse our file
file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader(input_files=[r"C:\Users\AMALVIYA\Downloads\senegal 1.pdf"], file_extractor=file_extractor).load_data()
print(documents)
# Assuming you have already loaded the `documents` variable as shown in your provided code

# Define the path for the output text file
output_file_path = "output_documents.md"

# Write the contents of `documents` to the text file
with open(output_file_path, "w", encoding="utf-8") as file:
    file.write(str(documents))


print(f"Documents have been written to {output_file_path}")

