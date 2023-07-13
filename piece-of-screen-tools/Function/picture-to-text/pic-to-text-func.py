import cv2
import pytesseract


def resize_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dimensions = (width, height)
    resized_image = cv2.resize(
        image, dimensions, interpolation=cv2.INTER_LINEAR)

    # Convert to grayscale
    gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    # Apply a binary threshold
    _, binary = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary


def pic_to_text(pic_path, scale_percent=200):
    # Read the picture
    image = cv2.imread(pic_path)

    # Resize the image
    resized_image = resize_image(image, scale_percent)

    # Extract text from the resized image
    string = pytesseract.image_to_string(resized_image)

    # Write the text to a file
    with open("text.txt", "w") as file:
        file.write(string)


pic_to_text("./test.png")
