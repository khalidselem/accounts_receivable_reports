from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in accounts_receivable_reports/__init__.py
from accounts_receivable_reports import __version__ as version

setup(
	name="accounts_receivable_reports",
	version=version,
	description="Accounts Receivable Reports",
	author="Smart Solutions",
	author_email="ahmed.younis_6@hotmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
