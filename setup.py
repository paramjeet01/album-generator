from setuptools import setup

requirements = [
    'click==7.1.2',
    'Jinja2==2.11.3',
    'Pillow==8.1.2',
]

setup(
    name="album-generator",
    version='1.0',
    packages=[
        'album',
    ],
    install_requires=requirements,
    include_package_data=True,
    entry_points='''
    [console_scripts]
    album-generator=album.album_generator:main
    ''',
)
