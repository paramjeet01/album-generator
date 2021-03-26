import click
import os
from PIL import Image
from album import generatehtml
import shutil

bool_types = [".jpg", ".png", ".jpeg"]  # Image file formats for choosing files


@click.command()
@click.argument('filepath', type=click.Path(exists=True))
def main(filepath):
    files = getfiles(filepath)  # List all files in given directory
    image_files = check_extension(files)  # List with all image files in given directory
    new_directory = "thumbnails"
    thumbnails_path = create_directory(filepath, new_directory, "Created")  # Creates new directory
    if thumbnails_path is not None:
        thumbnail_generator(image_files, filepath, new_directory)  # Generates thumbnail for each image
    else:
        path = os.path.join(filepath, new_directory)
        shutil.rmtree(path)
        create_directory(filepath, new_directory, "Updated")
        thumbnail_generator(image_files, filepath, new_directory)
    generatehtml.create_html(filepath, image_files, "index.html", "index.html") # Creates new html file


"""
        Returns all files in given directory !!
"""


def getfiles(filepath):
    image_directory = os.listdir(filepath)
    return image_directory


"""
        Creates thumbnail for images !!
"""


def thumbnail_generator(files, filepath, directory):
    for filename in files:
        temp_path = os.path.join(filepath, filename)
        image = Image.open(temp_path)
        max_size = (250, 250)
        image.thumbnail(max_size)
        newfile_path = os.path.join(filepath, directory, filename)
        save_files(newfile_path, image)  # saves the generated thumbnail image


"""
        Saves the file !!
        
"""


def save_files(path, image_file):
    image_file.save(path)


"""
        Creates new directory !!
"""


def create_directory(parent_dir, directory, txt):
    path = os.path.join(parent_dir, directory)
    try:
        os.mkdir(path)
        print("Directory:", directory, txt)
        return path
    except FileExistsError:
        print("Directory:", directory, "already exists")
        return None


"""
    Checks the image files in given directory !!
"""


def check_extension(filenames):
    files = []
    for filename in filenames:
        for type in bool_types:
            if filename.endswith(type):
                files.append(filename)
                break
    return files


if __name__ == '__main__':
    main()
