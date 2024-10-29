from setuptools import setup, find_packages

setup(
    name="py_singl_slider",
    version="{{VERSION_PLACEHOLDER}}",
    author="kerodekroma",
    author_email="kerodekroma@gmail.com",
    description="A single virtual slider control",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/kerodekroma/py-singl-slider",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pygame>=2.0.0',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'py_singl_slider=py_singl_slider.main:main',
        ],
    },
)