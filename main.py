from PIL import Image
import shutil, os


def read_all_files_recursive(path: str) -> list:
    files = []
    for current_file in os.listdir(path):
        if os.path.isfile(os.path.join(path, current_file)):
            if is_image(os.path.join(path, current_file)):
                files.append(os.path.join(path, current_file))
        elif os.path.isdir(os.path.join(path, current_file)):
            files += read_all_files_recursive(os.path.join(path, current_file))
    return files


def get_unique_images(files: list) -> list:
    unique_images = []
    for file in files:
        if not contain_image(unique_images, file):
            unique_images.append(file)
    return unique_images

def get_unique_images_from_folder(files: list,unique_images: list) -> list:
    for file in files:
        if not contain_image(unique_images, file):
            unique_images.append(file)
    return unique_images


def get_unique_images_in_folder(path: str) -> list:
    files = read_all_files_recursive(path)
    return get_unique_images(files)


def scan_unique_images_in_folder(path: str,unique_images: list) -> list:
    files = read_all_files_recursive(path)
    return get_unique_images_from_folder(files,unique_images)






def get_unique_list():
    unique_images = read_all_files_recursive("./unique_images")
    return unique_images


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
        with Image.open(file) as im:
            return True
    except OSError:
        return False


def contain_image(files: list, current_image: str) -> bool:
    for file in files:
        if compare_images(file, current_image):
            return True
    return False


def move_images(files: list, path: str):
    for file in files:
        try:
            shutil.move(file, path)
        except shutil.Error:
            print("File already exists")


if __name__ == '__main__':
    unique_images = get_unique_list()

    print(len(unique_images))
    images = read_all_files_recursive("./Images")
    #unique = get_unique_images_in_folder(".")

    unique=scan_unique_images_in_folder("./Images",unique_images)
    print(len(unique))
    move_images(unique, "./unique_images")
