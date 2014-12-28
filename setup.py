#!/usr/bin/python

from cx_Freeze import setup, Executable

includefiles = []
includes = []
excludes = []
packages = ["Pmw"]

setup(
    name = 'Youtube Python Downloader',
    version = '0.1',
    author = 'jasongi',
    author_email = 'jasongiancono@gmail.com',
    options = {'build_exe': {'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
    executables = [Executable('pysonggui.py')]
)
