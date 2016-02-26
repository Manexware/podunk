from setuptools import setup, find_packages  # Always prefer setuptools over distutils

long_description = """Reporte personalizado para Odoo.
Mas informacion en : http://www.github.com/manexware
"""

setup(name="podunk",
      version="1.0.0",
      description="",
      long_description=long_description,
      author="Jim Storch - Manuel Vega Ulloa",
      author_email="manuel.vega@manexware.com",
      license="GPLv3",
      url="http://www.github.com/manexware",
      download_url="http://www.github.com/manexware",
      classifiers=['Development Status :: 1.0.0',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Information Technology',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: System Administrators',
                   'Intended Audience :: Telecommunications Industry',
                   'Intended Audience :: Other Audience',
                   'Topic :: System :: Networking',
                   'Topic :: Security',
                   'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 2.7'],
      keywords="odoo reportlab report",
      install_requires=[],
      zip_safe=False,
      # TODO: This exclude is not working, tests package is still included in
      # packages. It's a bug in pip:
      #     https://bitbucket.org/pypa/wheel/issue/99/cannot-exclude-directory
      # Until it is fixed, the workaround is to create a MANIFEST.in file where
      # you prune your undesired files and compile package in two steps:
      #     python setup.py sdist
      #     pip wheel --no-index --no-deps --wheel-dir dist dist/*.tar.gz
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*",
                                      "tests", "*tests*"]),
      entry_points={'console_scripts': [],
                    },
      package_data={"podunk": [], }
      )