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

2. All the properties have doc strings explaining what they do.

3. I would love for your feedback and any ideas that you have for NeuKivy!

## PERFORMANCE PROBLEMS

NeuKivy needs to compute two shadows for every widget that is displayed. A shadow's computation is slow due to the dependency of Pillow. Thus the library has been structured in a way so as to minimize the amount of needed shadow recomputes. As of now when a widget changes size or elevation the shadow is recomputed.

On a PC the impact is negligible but on Android, animations regarding widget sizes is very slow. It might be okay with a couple of small widgets. But anything more will cause frame drops.

Elevation changes do not affect performance as much, but also should not be animated as much as possible.

Currently work is being done to draw the shadows using glsl shaders. This would make redrawing the shadows very fast.

**If you know anything about glsl shaders and creating super fast drop shadow shaders, your contributions are greatly welcome.(As I am not that experienced in glsl and it will take a long time to learn the language and the techniques.)**

To sum everything up. NeuKivy can run on android as long as you don't animate a lot of widget sizes ;)  

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

    (Can choose which side icon appears)
    - Rectangular
    - Rounded Rectangle

4. Card

5. Banner
