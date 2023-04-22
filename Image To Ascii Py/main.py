from PIL import Image

# ASCII characters and their intensities
ASCII_CHARS = [" ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]

def resize_image(image, new_width=100):
    """ Resizes and rotates the given image according to the specified width """
    width, height = image.size
    new_height = new_width * height // width
    return image.resize((new_width, new_height))

def grayify(image):
    """ Returns the given image in grayscale """
    return image.convert('L')

def pixels_to_ascii(image):
    """ Converts the pixels of the given image to ASCII characters """
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        # Select ASCII character based on pixel density
        ascii_str += ASCII_CHARS[pixel//10]
    return ascii_str

def image_to_ascii(image_path, new_width=100, output_path="ascii.txt"):
    """ Converts the given image with ASCII characters and writes it to the specified file """
    image = Image.open(image_path)
    image = resize_image(image, new_width=new_width)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)

    # Print ASCII characters to file
    with open(output_path, "w") as file:
        for i in range(0, len(ascii_str), new_width):
            file.write(ascii_str[i:i+new_width])
            file.write("\n")

# Usage example
image_to_ascii('test.jpeg', new_width=200, output_path="ascii.txt")
