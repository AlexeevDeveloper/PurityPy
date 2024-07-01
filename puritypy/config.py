#!/usr/bin/python3
"""
 @ Author: Alexeev Bronislav
 @ Title: PurityPy Configuration File
 @ Filepath: puritipy.py
 @ Description: File for reading config from .puritypy.toml

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
import tomllib


class Configuration:
	def __init__(self, filepath: str) -> None:
		self.filepath = filepath
		self.config = self.load_config()
	
	def load_config(self) -> dict:
		with open(self.filepath, "rb") as f:
			toml_dict = tomllib.load(f)

		return toml_dict
