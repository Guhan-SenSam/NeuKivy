# NeuKivy

![demo](https://github.com/Guhan-SenSam/NeuKivy/blob/main/images/demo.png)

Neukivy is a collection of neumorphic widgets built with Kivy. The library is currently in its initial development so there isn't much yet. But hopefully it will grow into a library you can use to easily create neumorphic UI in python.

## How to Install
1. Neukivy requires the latest version of pillow to run. This dependency will eventually be removed.
```
python3 -m pip install --upgrade Pillow
```
Make sure you are running the latest version (8.2.0)

2. Now install NeuKivy
```
pip install --upgrade git+git://github.com/Guhan-SenSam/NeuKivy.git
```

## Usage

There is a temporary examples directory that contains some code to help you understand the basic properties of NeuKivy better.

## Things to Know

1. I am just starting! NeuKivy is very young and still needs to grow by a lot to become of any practical use. Right now its more of a proof of concept and a demo rather than an actual usable library.

2. Neukivy is very slow. The current method for calculating shadows(needed for the neumorphism effect) is very slow and requires Pillow to work. The end goal is to imitate the current method by using glsl shaders which are faster when done right. But until then I wouldn't suggest running this on your android device as even a couple of moving widgets can make your app a slideshow. However if you use NeuKivy on a pc you most likely wont feel the performance impact. Just don't do too crazy for now :).

3. All the properties have doc strings explaining what they do.

3. I would love for your feedback and any ideas that you have for NeuKivy!

# Widgets Available
1. Button
    - Rectangular
    - Rounded Rectangle
    - Circular
2. Icon Button
    - Rectangular
    - Rounded Rectangle
    - Circular
3. Icon With Text Button
    - Rectangular
    - Rounded Rectangle
    (Can choose which side icon appears)
    
4. Card
