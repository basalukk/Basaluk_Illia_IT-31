from pathlib import Path
import qrcode

text = "Illia Basalukk, IT-31, i.basalukk@student.edu.ua"

image = qrcode.make(text)
output = Path(__file__).parent / "contact.png"
image.save(output)

print(f"QR-код збережено: {output.name}")
print(f"Дані: {text}")
