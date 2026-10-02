import copy
from pypdf import PdfReader, PdfWriter

def split_pdf_pages_horizontally(input_filename, output_filename="split_horizontal_output.pdf"):
    reader = PdfReader(input_filename)
    writer = PdfWriter()

    for page in reader.pages:
        # Create separate page objects for the top and bottom halves
        top_half = copy.copy(page)
        bottom_half = copy.copy(page)

        # Get original boundaries
        media_box = page.mediabox
        min_x = media_box.lower_left[0]
        max_x = media_box.upper_right[0]

        min_y = media_box.lower_left[1]
        max_y = media_box.upper_right[1]
        
        # Calculate horizontal midpoint (vertical division line)
        mid_y = (min_y + max_y) / 2

        # Crop Top Half
        top_half.mediabox.lower_left = (min_x, mid_y)
        top_half.mediabox.upper_right = (max_x, max_y)

        # Crop Bottom Half
        bottom_half.mediabox.lower_left = (min_x, min_y)
        bottom_half.mediabox.upper_right = (max_x, mid_y)

        # Add top and bottom halves sequentially to the output
        writer.add_page(top_half)
        writer.add_page(bottom_half)

    with open(output_filename, "wb") as f:
        writer.write(f)

    print(f"Successfully split each page of '{input_filename}' horizontally!")
    print(f"Output saved to '{output_filename}' ({len(writer.pages)} total pages).")

# Run the script on your file
split_pdf_pages_horizontally("/Users/ben/Downloads/PDFSplitting/Joy to the WorldJ.pdf")