from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension
from torch.utils import cpp_extension
import os
include_path=cpp_extension.include_paths()
#include_path.append("/home/singhanu/anaconda3/include")
setup(
    name='test',
    ext_modules=[
        CppExtension('test', [
            'test.cpp',
        ],
        libraries = ['fli'],
        library_dirs = [os.getcwd()],
        #runtime_library_dirs=[os.getcwd()],
        #extra_objects=[
        #    'libfli.so',],
        include_dirs=include_path)],
    cmdclass={
        'build_ext': BuildExtension
    })
