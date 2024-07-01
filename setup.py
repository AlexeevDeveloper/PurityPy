#!/usr/bin/python3
"""
 @ Author: Alexeev Bronislav
 @ Title: PurityPy setup file
 @ Filepath: setup.py
 @ Description: Special setup file to uploading library

 @ LICENSE GNU LGPL 3
  Powerful Linter and Formatter for Clean Python Code
  Copyright (C) 2024  Alexeev Bronislav

  This library is free software; you can redistribute it and/or
  modify it under the terms of the GNU Lesser General Public
  License as published by the Free Software Foundation; either
  version 2.1 of the License, or (at your option) any later version.

  This library is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
  Lesser General Public License for more details.
  
  You should have received a copy of the GNU Lesser General Public
  License along with this library; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
  USA
"""
from setuptools import setup, find_packages

setup(
	name='puritypy',
	version='1.0.0',
	description='Powerful Linter and Formatter for Clean Python Code',
	author='Alexeev Bronislav',
	author_email='alexeev.dev@mail.ru',
	url='https://github.com/AlexeevDeveloper/PurityPy',
	packages=find_packages(),
	install_requires=[
		'astroid>=3.2.2',
		'autopep8>=2.2.0',
		'black>=24.4.2',
		'click>=8.1.7',
		'dill>=0.3.8',
		'flake8>=7.0.0',
		'isort>=5.13.2',
		'markdown-it-py>=3.0.0',
		'mccabe>=0.7.0',
		'mdurl>=0.1.2',
		'mypy-extensions>=1.0.0',
		'packaging>=24.1',
		'pathspec>=0.12.1',
		'platformdirs>=4.2.2',
		'pycodestyle>=2.11.1',
		'pyflakes>=3.2.0',
		'Pygments>=2.18.0',
		'pylint>=3.2.3',
		'rich>=13.7.1',
		'ruff>=0.4.9',
		'tomlkit>=0.12.5',
	],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU LGPL 3",
		"Operatin System :: OS Indepedent"
	]
)
