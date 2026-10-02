from pypdf import PdfReader, PdfWriter


def extract_pages(input_pdf_path, output_pdf_path, pages_to_extract):
    """Extracts specific 1-based page numbers from a PDF and saves them to a new file.

    :param input_pdf_path: Path to the original PDF file.
    :param output_pdf_path: Path where the extracted PDF should be saved.
    :param pages_to_extract: List of page numbers (1-indexed) to extract.
    """
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for page_num in pages_to_extract:
        # Convert 1-based user input to 0-based Python indexing
        zero_index = page_num - 1

        if 0 <= zero_index < len(reader.pages):
            writer.add_page(reader.pages[zero_index])
        else:
            print(
                f"Warning: Page {page_num} is out of range (PDF has {len(reader.pages)} pages)."
            )

    with open(output_pdf_path, "wb") as output_file:
        writer.write(output_file)

    print(f"Saved: {output_pdf_path}")


# --- Example Usage ---
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Flute_Part_A.pdf", [11])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Flute_Part_B.pdf", [12])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Flute_Part_C.pdf", [13])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Flute_Part_D.pdf", [14])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Bells_Part_A.pdf", [17])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Bells_Part_B.pdf", [18])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Bells_Part_C.pdf", [19])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Bells_Part_D.pdf", [20])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Trumpet_Part_A.pdf", [23])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Tenor_Sax_Part_A.pdf", [23])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Trumpet_Part_B.pdf", [24])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Tenor_Sax_Part_B.pdf", [24])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Trumpet_Part_C.pdf", [25])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Tenor_Sax_Part_C.pdf", [25])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Trumpet_Part_D.pdf", [26])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Tenor_Sax_Part_D.pdf", [26])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Alto_Saxophone_Part_A.pdf", [29])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Bari_Sax_Part_A.pdf", [29])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Alto_Saxophone_Part_B.pdf", [30])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Bari_Sax_Part_B.pdf", [30])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Alto_Saxophone_Part_C.pdf", [31])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Bari_Sax_Part_C.pdf", [31])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Alto_Saxophone_Part_D.pdf", [32])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Bari_Sax_Part_D.pdf", [32])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/French_Horn_Part_A.pdf", [35])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/French_Horn_Part_B.pdf", [36])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/French_Horn_Part_C.pdf", [37])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/French_Horn_Part_D.pdf", [38])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Trombone_Part_A.pdf", [41])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Baritone_Part_A.pdf", [41])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Trombone_Part_B.pdf", [42])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Baritone_Part_B.pdf", [42])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Trombone_Part_C.pdf", [43])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Baritone_Part_C.pdf", [43])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Trombone_Part_D.pdf", [44])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Baritone_Part_D.pdf", [44])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Tuba_Part_A.pdf", [47])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Tuba_Part_B.pdf", [48])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Tuba_Part_C.pdf", [49])
extract_pages("/Users/ben/Downloads/Split to part/Sunset.pdf", "/Users/ben/Downloads/Split to part/Sunset/Tuba_Part_D.pdf", [50])