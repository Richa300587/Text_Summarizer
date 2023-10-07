import setuptools

with open("README.md",'r',encoding='UTF-8') as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME='Text_Summarizer'
AUTHOR_NAME='Richa300587'
SRC_REPO='textsummarizer'
AUTHOR_EMAIL='richa.chaudhary30@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description='NLP app',
    long_description=long_description,
    long_description_content='text/markdown',
    url=f"http://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)