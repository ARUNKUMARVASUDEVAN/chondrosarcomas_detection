import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()


__version__="0.0.0"

REPO_NAME="chondrosarcomas_detection"
AUTHOR_USER_NAME="ARUNKUMARVASUDEVAN"
SRC_REPO="chondrosarcomas_detection"
AUTHOR_EMAIL="oyeahitsarun@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="CNN",
    Long_description=long_description,
    Long_description_content="text/markdown",
    url=f"https://github/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug_Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
