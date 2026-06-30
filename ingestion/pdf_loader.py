"""
===========================================
PDF Loader
===========================================
"""

from pypdf import PdfReader
from utils.helper import debug, success, error


class PDFLoader:

    def __init__(self, pdf_path):

        self.pdf_path = pdf_path

    def load(self):

        try:

            debug(f"Loading PDF : {self.pdf_path}")

            reader = PdfReader(self.pdf_path)

            text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:

                    text += page_text + "\n"

            success("PDF Loaded Successfully")

            return text

        except Exception as e:

            error(e)

            return ""

# ==============================
# TEST RUN
# ==============================

if __name__ == "__main__":

    print("Testing PDF Loader...")


    loader = PDFLoader(
        "uploads/uploaded_resume.pdf"
    )


    text = loader.load()


    print("\n========== RESULT ==========\n")

    print("Characters:", len(text))


    print("\nPreview:\n")

    print(text[:500])