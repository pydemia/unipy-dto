#-*- coding: utf-8 -*-

"""
"""
import os
import datetime as dt
import tarfile
import distutils
import subprocess

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages
from distutils.cmd import Command

from pip._internal.req import parse_requirements


__all__ = ['__version__']

__version__ = '0.1.0'

package_name = 'unipy_dto'
package_version = __version__
python_requires = '>= 3.8'
short_desc = "A Data Transfer Object based on 'pydantic'"

git_url = 'https://github.com/pydemia/unipy_dto'
doc_url = ''
download_url = git_url
license_family_str = ''
license_str = ''


__desc__ = """

"""

long_desc = ""
with open('README.rst', 'r', encoding='utf-8') as readme_file:
    long_desc = readme_file.read()


required_packages = [
    str(r.requirement) for r in
    parse_requirements("requirements.txt", session='hack')
]


class SphinxCommand(Command):
    """Documentation Command"""

    def initialize_options(self):
        """Set default values for options."""
        pass

    def finalize_options(self):
        """Post-process options."""
        pass

    def run(self):
        """Run command."""
        command = ['cd docs;make html;cd ..']
        # command.append(os.getcwd())
        self.announce(
            'Running command: %s' % str(command),
            level=distutils.log.INFO)
        subprocess.check_call(command)


setup(name=package_name,
      version=package_version,
      description=short_desc,
      long_description=long_desc,
      python_requires=python_requires,
      url=doc_url,
      download_url=download_url,
      author='Youngju Jaden Kim',
      author_email='pydemia@gmail.com',
      license=license_str,
      packages=find_packages(include='app', exclude=['contrib', 'docs', 'tests']),
      cmdclass={'documentation': SphinxCommand},
      install_requires=required_packages,
      zip_safe=False,
      package_data={package_name: ['*.gz', 'dataset/resources.tar.gz']}
      )
