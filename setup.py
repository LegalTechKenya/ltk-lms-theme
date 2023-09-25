import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "tutorindigo", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="ltk-lms-theme",
    version=ABOUT["__package_version__"],
    url="https://github.com/LegalTechKenya/ltk-lms-theme",
    project_urls={
        "Documentation": "https://docs.tutor.overhang.io/",
        "Code": "https://github.com/LegalTechKenya/ltk-lms-theme",
        "Issue tracker": "https://github.com/LegalTechKenya/ltk-lms-theme/issues",
        "Community": "https://legaltechkenya.com/",
    },
    license="AGPLv3",
    author="William Otieno - LTK",
    author_email="william.otieno@legaltechkenya.com",
    maintainer="LegalTechKE",
    maintainer_email="support@legaltechkenya.com",
    description="Indigo theme plugin for LTK LMS",
    long_description=load_readme(),
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["tutor>=16.0.0,<17.0.0"],
    entry_points={"tutor.plugin.v1": ["indigo = tutorindigo.plugin"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
