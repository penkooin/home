import fitz  # PyMuPDF
import os

pdf_path = "포트폴리오.pdf"
output_dir = "images"
os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
image_count = 0

for page_num in range(len(doc)):
    page = doc[page_num]
    images = page.get_images(full=True)
    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image_path = os.path.join(output_dir, f"page{page_num+1}_img{img_index+1}.{image_ext}")
        with open(image_path, "wb") as f:
            f.write(image_bytes)
        image_count += 1
        print(f"Saved: {image_path}")

print(f"\n✅ Done. {image_count} images extracted.")
