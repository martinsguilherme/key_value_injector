import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='src',
    version='1.0',
    author='Guilherme Martins',
    author_email='martins_guilherme@live.com',
    description='Injects a pair of key and value to a header of an HTTP request',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/martinsguilherme/key_value_injector',
    license='MIT',
    packages=['src', 'src.controller', 'src.model', 'src.test'],
    install_requires=['requests', 'fastapi', 'pydantic'],
)