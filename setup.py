import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plotter",
    version="1.3",
    author="Thomas Trouchkine",
    author_email="thomas.trouchkine@gmail.com",
    description="Plotting library with descriptive approach",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://thomas.trouchkine.com/projects/plotter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
