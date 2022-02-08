from setuptools import setup, find_packages

name = "anybadge-frontend"
version = "0.0.1"

cmdclass={} 

setup(
    name=name,
    version=version,
    author="Christian Klarhorst",
    author_email="cklarhor@techfak.uni-bielefeld.de",
    description="",
    long_description="",
    long_description_content_type="text/markdown",
    url="todo",
    project_urls={
        "Main framework": "todo",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': ['gen-badge = anybadge_frontend.gen_badge:main',],
    },
    cmdclass=cmdclass,
    python_requires=">=3.6", # todo
    install_requires= [
        "anybadge", "xmltodict",
    ],
)
