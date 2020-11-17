import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MathSets", # Replace with your own username
    version="0.0.1",
    author="Yuval Rosen",
    author_email="yuv.rosen@gmail.com",
    description="A package to use mathematical sets in pytohn.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yuvix25/MathSets",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)