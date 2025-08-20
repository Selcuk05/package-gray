import setuptools

setuptools.setup(
    name="package-gray",
    version="0.0.1",
    author="Selcuk Oz",
    author_email='selcuk_45@protonmail.com',
    description="PackageGray",
    url='https://github.com/Selcuk05/package-gray',
    license='MIT',
    install_requires=['sdk', 'opencv-python-headless'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    packages=[
        'novavision.package',
        'novavision.package.classes',
        'novavision.package.configs',
        'novavision.package.dataloaders',
        'novavision.package.executors',
        'novavision.package.models',
        'novavision.package.utils',
        'novavision.package.weights'
    ],
    package_dir={'novavision.package': 'src'},
    python_requires=">=3.6"
)