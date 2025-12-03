from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fungraphics",
    version="1.0.0",
    author="HES-SO Valais//Wallis",
    author_email="",
    description="A simple 2D graphics library for Python, perfect for learning programming",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/isc-hei/FunGraphics",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Topic :: Multimedia :: Graphics",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # tkinter is included with Python, no external dependencies required
    ],
    extras_require={
        "imaging": ["Pillow>=9.0.0"],  # Optional for PNG export and image transformations
    },
)
