from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in money_management_backend/__init__.py
from money_management_backend import __version__ as version

setup(
	name="money_management_backend",
	version=version,
	description="to manage our income ,expenses ,etc...",
	author="saheeth",
	author_email="saheeth@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
