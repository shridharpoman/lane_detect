from distutils.core import setup 
from distutils.extension import Extension 
from Cython.Build import cythonize 
 
ext_modules = [Extension("cylane", 
                            sources=["cylane.pyx"])] 
 
ext_options = {"compiler_directives": {"profile": True}, "annotate": True} 
 
setup(name="cylane",
      ext_modules=cythonize(ext_modules, **ext_options))
