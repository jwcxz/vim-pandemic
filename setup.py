from distutils.core import setup

setup(
    name="Pandemic",
    version="2.0.0",
    author="http://jwcxz.com/",
    url="https://github.com/jalanb/vim-pandemic",
    requires=["argparse"],
    packages=["Pandemic"],
    scripts=["bin/pandemic"],
)
