import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fp:
    install_requires = fp.read()

with open('egybest-dl/egybest-dl') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.replace("'", '').split()[-1]
            break


setuptools.setup(
    name="egybest-dl",
    version=version,
    author="Yassine Addi",
    author_email="yassineaddi98@gmail.com",
    license="MIT",
    keywords="egybest movies series",
    description="Downloads any Movie or TV Series from EgyBest.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yassineaddi/egybest-dl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
    install_requires=install_requires,
    scripts=["egybest-dl/egybest-dl", "egybest-dl/egybest-dl.bat"]
)