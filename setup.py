'''
Created on Aug 19, 2013

@author: Mike
'''
from distutils.core import setup
import py2exe
import matplotlib
 
setup(windows=['DotaGrapher.py'],
	options={
               'py2exe': {
                          'packages' :  ['matplotlib'],
                          'dll_excludes': ['libgdk-win32-2.0-0.dll',
                                         'libgobject-2.0-0.dll',
                                         'libgdk_pixbuf-2.0-0.dll',
                                         'libgtk-win32-2.0-0.dll',
                                         'libglib-2.0-0.dll',
                                         'libcairo-2.dll',
                                         'libpango-1.0-0.dll',
                                         'libpangowin32-1.0-0.dll',
                                         'libpangocairo-1.0-0.dll',
                                         'libglade-2.0-0.dll',
                                         'libgmodule-2.0-0.dll',
                                         'libgthread-2.0-0.dll',
                                         'QtGui4.dll', 'QtCore.dll',
                                         'QtCore4.dll'
                                        ],
                          }
                },
	 			  data_files=matplotlib.get_py2exe_datafiles(),
)