import setuptools #导入setuptools打包工具
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    #install_requires = ["rich>=12.0.1"],
    name="txvx", 
    version="1.0", 
    author="FZZkill",
    author_email="qa000m@126.com", 
    description="更简单的配置",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Mozilla Public License 2.0"
    url="https://github.com/FZZkill/TxvxConfig",
    packages= setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8', 
)
setuptools.setup()

