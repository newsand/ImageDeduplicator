from PIL import Image
import shutil, os

def compare_images(im1: str, im2: str) -> bool:
    im1 = Image.open(im1)
    im2 = Image.open(im2)

    if list(im1.getdata()) == list(im2.getdata()):
        print("Identical")
        return True
    else:
        print("Different")
        return False


def is_image(file: str) -> bool:
    try:
        with Image.open(current_file) as im:
            return True
    except OSError:
        return False


def contain_image(files: list, current_image: str) -> bool:
    for file in files:
        if compare_images(file, current_image):
            return True
        else:
            return False


if __name__ == '__main__':
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        print(f)
    print(type(files))

    unique_images = []
    for current_file in files:
        if not (is_image(current_file)):
            print(current_file)
            continue
        if not unique_images:
            unique_images.append(current_file)

        if not contain_image(unique_images, current_file):
            unique_images.append(current_file)

    for f in unique_images:
        shutil.copy(f, 'unique_images')

