
import sys
import numpy
from PyQt5 import QtCore, QtGui
import PyQt5.Qwt5 as Qwt


numPoints=1000
xs=numpy.arange(numPoints)
ys=numpy.sin(3.14159*xs*10/numPoints) #this is our data

def plotSomething():
    global ys
    ys=numpy.roll(ys,-1)
    c.setData(xs, ys)
    uiplot.qwtPlot.replot()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    win_plot = ui_plot.QtGui.QMainWindow()
    uiplot = ui_plot.Ui_win_plot()
    uiplot.setupUi(win_plot)

    # tell buttons what to do when clicked
    uiplot.btnA.clicked.connect(plotSomething)
    uiplot.btnB.clicked.connect(lambda: uiplot.timer.setInterval(100.0))
    uiplot.btnC.clicked.connect(lambda: uiplot.timer.setInterval(10.0))
    uiplot.btnD.clicked.connect(lambda: uiplot.timer.setInterval(1.0))

    # set up the QwtPlot (pay attention!)
    c=Qwt.QwtPlotCurve()  #make a curve
    c.attach(uiplot.qwtPlot) #attach it to the qwtPlot object
    uiplot.timer = QtCore.QTimer() #start a timer (to call replot events)
    uiplot.timer.start(100.0) #set the interval (in ms)
    win_plot.connect(uiplot.timer, QtCore.SIGNAL('timeout()'), plotSomething)

    # show the main window
    win_plot.show()
    sys.exit(app.exec_())