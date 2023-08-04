import setuptools

with open("README.md","r",encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text_summarizer"
AUTHOR_USERNAME = "asharma-02"
SRC_REPO="TextSummarizer"
AUTHOR_EMAIL="sharma.adhista@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email=AUTHOR_EMAIL,
    description="Text summarizer using NLP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}",
    project_urls = {"Bug Tracker": f"https://github.com/{AUTHOR_USERNAME}/{REPO_NAME}/issues",},
    package_dir= {"": "src"},
    packages=setuptools.find_packages(where="src"),
)