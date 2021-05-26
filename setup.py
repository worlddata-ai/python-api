# -*-coding:utf-8-*-

from setuptools import setup

setup(
    name="worlddata",
    version="0.0.1",
    packages=[
        "worlddata",
        "worlddata.APIExceptions",
        "worlddata.APISections",
    ],
    url="https://github.com/worlddata-ai/python-api",
    license="MIT",
    author="Vikas Patel",
    author_email="vikas.patel@zdaly.com",
    description="Python API wrapper for WorldData.AI",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    install_requires=("requests",),
)
