from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="markupquill",
    version="0.0.10",
    description="Create a LaTeX matrix from console input",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    entry_points={'console_scripts': ['markupquill=markupquill.run:run']},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asgervelling/markupquill",
    author="Asger Skov Velling",
    author_email="asger.skov.velling@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
