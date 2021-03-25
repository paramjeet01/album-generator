import os
from jinja2 import Template

"""
        Creates new html file for the given files !!
"""


def create_html(root, files):
    file_paths = path_generator(root, files)
    jinja2_template_string = open("sample.html", 'r', encoding="utf8").read()  # Reads the sample html file
    template = Template(jinja2_template_string)
    html_template_string = template.render(image_paths=file_paths[0], thumbnail_paths=file_paths[1], file_names=files)  # Renders a new html code using " JINJA "
    htmlfilepath = os.path.join(root, "Mygallery.html")
    htmlfile = open(htmlfilepath, 'w', encoding="utf8")
    htmlfile.write(html_template_string)  # New HTML file is created


"""
        Generates path for the given filenames !!
"""


def path_generator(root, files):
    images_path = []
    thumbnails_path = []
    for file in files:
        image_path = os.path.join(root, file)
        images_path.append(image_path)
        thumbnail_path = os.path.join(root, "thumbnails", file)
        thumbnails_path.append(thumbnail_path)
    return [images_path, thumbnails_path]
