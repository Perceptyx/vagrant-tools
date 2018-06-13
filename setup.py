from setuptools import setup, find_packages
setup(
    name="VagrantTools",
    version="0.1",
    packages=find_packages(),
    scripts=['vagrant-download.py', 'vagrant-upload.py'],

    install_requires=['decorator>=3.4.2', 'ecdsa>=0.13', 
        'Fabric>=1.10.2', 'paramiko>=1.15.2', 'pycrypto>=2.6.1',
        'six>=1.9.0', 'validators>=0.8'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.md'],
    },

    # metadata for upload to PyPI
    author="Andres Montalban",
    author_email="amontalban@perceptyx.com",
    description="A collection of Python scripts to manage Vagrant boxes in a private repository",
    license="LICENSE",
    keywords="vagrant tools",
    url="https://github.com/Perceptyx/vagrant-tools/",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://github.com/Perceptyx/vagrant-tools/issues/",
        "Documentation": "https://github.com/Perceptyx/vagrant-tools/",
        "Source Code": "https://github.com/Perceptyx/vagrant-tools/",
    }

    # could also include long_description, download_url, classifiers, etc.
)
