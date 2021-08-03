from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as f:
    readme = f.read()

with open("VERSION.txt", "r") as f:
    version_num = f.read()

setup (
    name="cleanlogs",
    version = version_num.strip(),
    author="Arpit",
    author_email="arpitfalcon1@gmail.com",
    description = "Clean thousand of lines of log file",
    long_description = readme,
    long_description_content_type = "text/markdown",

    # Homepage
    url="https://github.com/arpitfalcon/clean-my-logs",

    install_requires=[],
    keywords="pypi logmine cleanlogs clean logs cli bash",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points = {
    'console_scripts': [
        'cleanlogs = src.run:run'
    ],}
    )