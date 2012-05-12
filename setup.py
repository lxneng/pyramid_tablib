from setuptools import setup
from setuptools import find_packages

version = '0.1'

requires = [
    'tablib',
    ]

tests_require = []

setup(name='pyramid_tablib',
      version=version,
      description='tablib renderer (xlsx, xls, csv) for pyramid',
      author='Eric Lo',
      author_email='lxneng@gmail.com',
      url='https://github.com/lxneng/pyramid_tablib',
      license='BSD',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=tests_require,
      extras_require={
          'docs': ['sphinx'],
          'tests': tests_require,
          },
      test_suite='pyramid_tablib')
