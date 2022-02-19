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


def get_unique_images_in_folder(path: str) -> list:
    files = read_all_files_recursive(path)
    return get_unique_images(files)


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
    unique_images = get_unique_images_in_folder("./unique_images")

    print(len(unique_images))
    images = read_all_files_recursive("./Images")
    unique = get_unique_images_in_folder(".")
    print(len(unique))
    move_images(unique, "./unique_images")

    # files = [f for f in os.listdir('.') if os.path.isfile(f)]
    # for f in files:
    #     print(f)
    # print(type(files))
    #
    # unique_images = []
    # for current_file in files:
    #     if not (is_image(current_file)):
    #         print(current_file)
    #         continue
    #     if not unique_images:
    #         unique_images.append(current_file)
    #
    #     if not contain_image(unique_images, current_file):
    #         unique_images.append(current_file)
    #
    # for f in unique_images:
    #     shutil.move(f, 'unique_images')
    #
