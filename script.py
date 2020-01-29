from PIL import Image
import os


HEIGHT = 17
WIDTH = 106
BINARY_SIZE = 1802


def get_mode() -> int:
    print('Enter the mode:\n0 - from image to number\n1 - from number to image')

    try:
        mode = int(input())
    except ValueError:
        print('Error! Enter correct number!')
        mode = get_mode()

    if mode not in (0, 1):
        print('Error! Enter correct number!')
        mode = get_mode()

    return mode


def from_image_to_num() -> int:

    def find_num() -> int:
        byte_string: str = ''

        for x in range(105, -1, -1):
            for y in range(0, HEIGHT):
                pixel: str = str(pic.getpixel((x, y)))
                if pixel == "255":
                    byte_string += '1'
                else:
                    byte_string += '0'

        k_number = int(byte_string, 2) * 17
        return k_number

    print('Enter the name of image (106x17 pixels)')

    pic_name = input()

    if pic_name in os.listdir('./'):
        pic: Image = Image.open(pic_name)
        pic_width, pic_height = pic.size
        if pic_width == WIDTH and pic_height == HEIGHT:
            pic = pic.convert('1')
            k: int = find_num()
        else:
            print('Error! Incorrect size of pic!')
            k: int = from_image_to_num()
    else:
        print('Error! Incorrect name of pic!')
        k: int = from_image_to_num()

    return k


def from_num_to_image():

    def get_k() -> int:
        print('Enter k')

        try:
            k_number = int(input())
        except ValueError:
            print('Error! Enter correct k!')
            k_number = get_k()

        return k_number

    def draw_pic() -> Image:
        pic = Image.new('1', (WIDTH, HEIGHT), 0)
        for y in range(HEIGHT):
            for x in range(WIDTH):
                pic.putpixel(xy=(WIDTH - x - 1, HEIGHT - y - 1), value=(int(pixels_data[y][x]), ))
        return pic

    def save_pic(pic):
        print('Print name for pic')

        try:
            pic_name = input()
            pic.save(pic_name)
        except ValueError:
            print('Error! Incorrect filename!')
            save_pic(pic)

    k = get_k()
    k //= 17

    binary_k = bin(k)[2:]

    if len(binary_k) < BINARY_SIZE:
        fixed_binary_k = '0' * (BINARY_SIZE - len(binary_k))
        binary_k += fixed_binary_k

    pixels_data = [[] for _ in range(HEIGHT)]
    for pixel in range(BINARY_SIZE):
        pixels_data[pixel % HEIGHT].append(binary_k[pixel])
    pixels_data.reverse()

    picture = draw_pic()
    save_pic(picture)


def main():
    mode: int = get_mode()

    if mode == 0:
        k: int = from_image_to_num()
        print(k)
    elif mode == 1:
        from_num_to_image()


if __name__ == "__main__":
    main()
