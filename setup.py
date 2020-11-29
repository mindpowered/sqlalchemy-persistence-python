import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='mindpowered-sqlalchemy-persistence',
    version='0.0.3',
    author="Mind Powered Corporation",
    author_email="support@mindpowered.dev",
    license="CPAL-1.0",
    url="https://mindpowered.dev/",
    description="SQLAlchemy Persistence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['persistence'],
    packages=['mindpowered_sqlalchemy_persistence'],
    package_dir={'mindpowered_sqlalchemy_persistence': 'wrappers'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'mindpowered-maglev',
        'SQLAlchemy'
    ],
)
