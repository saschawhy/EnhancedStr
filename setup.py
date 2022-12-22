from setuptools import setup, find_packages  # type: ignore
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.0.2"
DESCRIPTION = "A Python library for prettier, fully customizable console outputs."
LONG_DESCRIPTION = "A Python library for prettier, fully customizable console outputs."

setup(
    name="enhanced_str",
    version=VERSION,
    author="saschawhy",
    # author_email="<mail@neuralnine.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    # install_requires=["opencv-python", "pyautogui", "pyaudio"],
    keywords=["python", "console", "output", "pretty", "print"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)


# 1) python setup.py sdist bdist_wheel
# 2) twine upload dist/*
