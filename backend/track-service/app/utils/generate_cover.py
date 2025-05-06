from PIL import Image, ImageDraw, ImageFont
import io


def generate_cover(title: str) -> tuple[bytes, str]:
    image_size = (200, 200)
    background_color = (156, 163, 175)
    text_color = (255, 255, 255)

    img = Image.new("RGB", image_size, background_color)
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 70)
    except IOError:
        font = ImageFont.load_default()

    text = title[:2].upper()
    text_size = draw.textbbox((0, 0), text, font=font)
    text_x = (image_size[0] - text_size[2]) / 2
    text_y = (image_size[1] - text_size[3]) / 2
    draw.text((text_x, text_y), text, font=font, fill=text_color)

    image_io = io.BytesIO()
    img.save(image_io, format="PNG")
    image_io.seek(0)
    filename = f"{title}_profile.png"

    return image_io.read(), filename
