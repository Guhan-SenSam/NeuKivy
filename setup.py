from setuptools import find_packages, setup
setup(
    name='NeuKivy',
    url='https://github.com/Guhan-SenSam/NeuKivy',
    author='Guhan SenSam',
    author_email='infinium.software.2021@gmail.com',
    packages=find_packages(include=["neukivy", "neukivy.*", "neukivy.uix.behaviors"]),
    package_dir={"neukivy": "neukivy"},
    package_data={
            "neukivy": ["fonts/*.ttf"]
        },
    install_requires=["kivy>=2.0.0", "pillow"],
    version='0.1',
    license='MIT',
    description='A collection of neumorphic widgets built with kivy'
)
