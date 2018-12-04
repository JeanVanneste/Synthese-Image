# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 13:30:15 2018

@author: 17242
"""

import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import sys

class CustomizedShader(object):
    def __init__(self):
        
        # Setup the view window
        self.app = QtGui.QApplication(sys.argv)
        self.w = gl.GLViewWidget()
        self.w.setGeometry(0, 110, 1920, 1080)
        self.w.view()
        self.w.setWindowTitle('Collision')
        self.w.setCameraPosition(distance=30, elevation = 8)
        
        
        
    def start(self):
        """
        get the graphic window open & setup
        """
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()


if __name__ == '__main__':
    pass
