from setuptools import find_packages, setup


print(find_packages())

setup(
    name='compapi',
    version='1.0.0',
    packages=['.'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask_sqlalchemy'
    ],
)
