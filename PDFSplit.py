import copy
from pypdf import PdfReader, PdfWriter

def split_pdf_pages_in_half(input_filename, output_filename="split_output.pdf"):
    reader = PdfReader(input_filename)
    writer = PdfWriter()

    for page in reader.pages:
        # Create separate page objects for the left and right halves
        left_half = copy.copy(page)
        right_half = copy.copy(page)

        # Get original boundaries
        media_box = page.mediabox
        min_x = media_box.lower_left[0]
        max_x = media_box.upper_right[0]
        mid_x = (min_x + max_x) / 2

        min_y = media_box.lower_left[1]
        max_y = media_box.upper_right[1]

        # Crop Left Half
        left_half.mediabox.lower_left = (min_x, min_y)
        left_half.mediabox.upper_right = (mid_x, max_y)

        # Crop Right Half
        right_half.mediabox.lower_left = (mid_x, min_y)
        right_half.mediabox.upper_right = (max_x, max_y)

        # Add both halves sequentially to the output
        writer.add_page(left_half)
        writer.add_page(right_half)

    with open(output_filename, "wb") as f:
        writer.write(f)

    print(f"Successfully split each page of '{input_filename}' in half!")
    print(f"Output saved to '{output_filename}' ({len(writer.pages)} total pages).")

# Run the script on your file
split_pdf_pages_in_half("input.pdf")