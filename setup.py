from setuptools import setup, find_packages

setup(
    name="physlib",
    version="0.1",
    description="A simple modular physics library for mechanics, thermodynamics, optics, and more.",
    author="Mocha",
    author_email="ohplot@gmail.com",
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    keywords="physics kinematics dynamics waves electricity optics",
    license="MIT",
)