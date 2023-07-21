from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'This is the compressible version of various libraries of python '
LONG_DESCRIPTION = 'This is the compressible version of various libraries of python '

# Setting up
setup(
    name="JaiShriRam",
    version=VERSION,
    author="Krishna",
    author_email="Krishnavijaywargiya12@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['turtle','mediapipe','autopy','torch', 'tkinter', 'pyautogui', 'time', 'speech_recognition', 'pyttsx3'],
    keywords=['sum', 'minus', 'multiply', 'divide', 'factorial'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)