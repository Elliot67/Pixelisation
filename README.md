# Pixelisation

## What is it ?

Pixelisation is a free python program that will divide your image into bigger pixels.

Before | After
------ | -----
![dog](img/dog.jpg) | ![dog_pixelate](img/modif_dog.jpg)


# How to use it ?

To run pixelisation, you just need to go in the same folder where is located main.py and run:
```bash
python main.py dog.jpg -s 50 -o new_dog.jpg
```
The scale [-s] and output [-o] parameter are not required, which means you can also do:
```bash
python main.py dog.jpg
```
It will automatically set the scale to 1/30 of the image (width or height) and the output to *filename*\_pixelate.*extension* .



# Requirements

- Python 3
- Python module :
	- [numpy](www.pypi.org/project/numpy)
	- [openCV](www.pypi.org/project/opencv-python)
