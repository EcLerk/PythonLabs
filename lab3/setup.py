# Always prefer setuptools over distutils
from setuptools import setup

# This call to setup() does all the work
setup(
    name="serializer_Kachanovskaya",
    version="0.1.8",
    description="JSON / XML serializer",
    author="EcLer",
    author_email="lerakachanovskaya@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.11',
    packages=["serializer_Kachanovskaya", "serializer_Kachanovskaya.packer", "serializer_Kachanovskaya.serializer"],
    include_package_data=True,
    install_requires=["regex"]
)
