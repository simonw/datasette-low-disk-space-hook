from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-low-disk-space-hook",
    description="Datasette plugin providing the low_disk_space hook for other plugins to check for low disk space",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-low-disk-space-hook",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-low-disk-space-hook/issues",
        "CI": "https://github.com/simonw/datasette-low-disk-space-hook/actions",
        "Changelog": "https://github.com/simonw/datasette-low-disk-space-hook/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License",
    ],
    version=VERSION,
    packages=["datasette_low_disk_space_hook"],
    entry_points={"datasette": ["low_disk_space_hook = datasette_low_disk_space_hook"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio"]},
    python_requires=">=3.7",
)
