from PIL import Image
import shutil, os


# funcao de  leitura de arquivos
def find_all_images_recursive(path: str) -> list:
    files = []
    for current_file in os.listdir(path):
        if os.path.isfile(os.path.join(path, current_file)):
            if is_image(os.path.join(path, current_file)):
                files.append(os.path.join(path, current_file))
        elif os.path.isdir(os.path.join(path, current_file)):
            files += find_all_images_recursive(os.path.join(path, current_file))
    return files


def clean_up_duplicates(files: list, unique_images: list) -> list:
    for file in files:
        if not contain_image(unique_images, file):
            unique_images.append(file)
    return unique_images


def scan_unique_images_in_folder(path: str, unique_images: list) -> list:
    files = find_all_images_recursive(path)
    return clean_up_duplicates(files, unique_images)


def get_unique_folder_files():
    unique_images = find_all_images_recursive("./unique_images")
    return unique_images


# closed list stuff
def get_unique_images_in_folder(path: str) -> list:
    files = find_all_images_recursive(path)
    return get_unique_images_in_list(files)


def get_unique_images_in_list(files: list) -> list:
    unique_images = []
    for file in files:
        if not contain_image(unique_images, file):
            unique_images.append(file)
    return unique_images


# image testing

def is_image(file: str) -> bool:
    try:
        with Image.open(file) as im:
            return True
    except OSError:
        return False


def compare_images(im1: str, im2: str) -> bool:
    im1 = Image.open(im1)
    im2 = Image.open(im2)

    if list(im1.getdata()) == list(im2.getdata()):
        print("Identical")
        return True
    else:
        print("Different")
        return False


def contain_image(files: list, current_image: str) -> bool:
    for file in files:
        if compare_images(file, current_image):
            return True
    return False


# File manipulation
def move_images(files: list, path: str):
    for file in files:
        try:
            shutil.move(file, path)
        except shutil.Error:
            print("File already exists")


def copy_images(files: list, path: str):
    for file in files:
        try:
            shutil.copy(file, path)
        except shutil.Error:
            print("File already exists")


def rename_files_with_directory_name_ordinal(files: list):
    for i, file in enumerate(files):
        path, ext = os.path.splitext(file)
        os.path.basename(os.path.dirname(file))
        os.rename(file, os.path.join(os.path.dirname(file),
                                     os.path.basename(os.path.dirname(file)) + str(i) + ext))


# routines

def run():
    unique_images = get_unique_folder_files()
    print("Current unique count: ",len(unique_images))
    images = find_all_images_recursive("./Images")
    rename_files_with_directory_name_ordinal(images)
    # unique = get_unique_images_in_folder(".")
    unique = scan_unique_images_in_folder("./Images", unique_images)
    print("Final count: ",len(unique))
    copy_images(unique, "./unique_images")


def run2():
    unique_images = get_unique_folder_files()

    images=find_all_images_recursive("./Images")
    for i, file in enumerate(images):
        path, ext = os.path.splitext(file)
        os.path.basename(os.path.dirname(file))
        os.rename(file, os.path.join(os.path.dirname(file),
                                     os.path.basename(os.path.dirname(file)) + str(i) + ext))
        #os.rename(file, os.path.join(dir, path2[-2] + str(i) + ext))




if __name__ == '__main__':
    run()
""" o codigo pega uma pasta e copia todos os arquivos que nao se repitam para uma pasta chamada unique_images
    perimeiro busca todas as imagens da pasta de aquivo unicos para usar de base
    segundo busca todas as imagens das pastasa serem analisadas de forma recursivar criando uma lista de arquivos
    compara todas as imagens uma a uma de forma a identificar todas as duplicatas
    todas as imagens unicas sao movidas para a pastas unique_images
    das imagens duplicadas escolhe-se uma ao acaso e envia para a pasta unique_images
"""

# rename_files_as_directory_name_ordinal(get_unique_folder_files())


# def split_file_path(path):
