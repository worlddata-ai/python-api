# -*-coding:utf-8-*-

from setuptools import setup

setup(
    name="worlddata",
    version="0.0.3",
    packages=[
        "worlddata",
        "worlddata.APIExceptions",
        "worlddata.APISections",
    ],
    url="https://github.com/worlddata-ai/python-api",
    license="WorldData",
    author="Akash Doifode",
    author_email="akash.doifode@worlddata.ai",
    description="Python API wrapper for WorldData.AI",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    install_requires=("requests",),
)
