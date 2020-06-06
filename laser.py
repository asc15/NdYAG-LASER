# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laser.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_laser(object):
    def setupUi(self, laser):
        laser.setObjectName("laser")
        laser.setWindowModality(QtCore.Qt.ApplicationModal)
        laser.resize(552, 466)
        laser.setStyleSheet("background-color:rgb(203, 203, 203);\n"
"")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(laser)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(130, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(laser)
        self.label.setStyleSheet("BACKGROUND-COLOR:grey;\n"
"font:bold;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(128, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(laser)
        self.label_2.setStyleSheet("BACKGROUND-COLOR:grey;\n"
"font:bold;\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(165, 13, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_6 = QtWidgets.QLabel(laser)
        self.label_6.setStyleSheet("BACKGROUND-COLOR:grey;\n"
"font:bold;")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(209, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_14 = QtWidgets.QLabel(laser)
        self.label_14.setStyleSheet("BACKGROUND-COLOR:white;\n"
"font:bold;")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        spacerItem4 = QtWidgets.QSpacerItem(171, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.line_5 = QtWidgets.QFrame(laser)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_7.addWidget(self.line_5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(laser)
        self.label_3.setStyleSheet("BACKGROUND-COLOR:grey;\n"
"font:bold;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.l = QtWidgets.QLineEdit(laser)
        self.l.setStyleSheet("BACKGROUND-COLOR:white;\n"
"")
        self.l.setText("")
        self.l.setObjectName("l")
        self.horizontalLayout_4.addWidget(self.l)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(50, 97, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 1, 4, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_9 = QtWidgets.QLabel(laser)
        self.label_9.setStyleSheet("BACKGROUND-COLOR:grey;\n"
"font:bold;")
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.l1 = QtWidgets.QLineEdit(laser)
        self.l1.setStyleSheet("BACKGROUND-COLOR:white;\n"
"")
        self.l1.setObjectName("l1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.l1)
        self.label_10 = QtWidgets.QLabel(laser)
        self.label_10.setStyleSheet("BACKGROUND-COLOR:grey;\n"
"font:bold;\n"
"")
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.w2 = QtWidgets.QLineEdit(laser)
        self.w2.setStyleSheet("BACKGROUND-COLOR:white;\n"
"")
        self.w2.setObjectName("w2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.w2)
        self.label_11 = QtWidgets.QLabel(laser)
        self.label_11.setStyleSheet("BACKGROUND-COLOR:grey;\n"
"font:bold;\n"
"")
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.tdoubledash = QtWidgets.QLineEdit(laser)
        self.tdoubledash.setStyleSheet("BACKGROUND-COLOR:white;\n"
"")
        self.tdoubledash.setObjectName("tdoubledash")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.tdoubledash)
        self.gridLayout.addLayout(self.formLayout, 0, 2, 3, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(laser)
        self.label_4.setStyleSheet("BACKGROUND-COLOR:grey;\n"
"font:bold;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.w = QtWidgets.QLineEdit(laser)
        self.w.setStyleSheet("BACKGROUND-COLOR:white;\n"
"")
        self.w.setObjectName("w")
        self.horizontalLayout_5.addWidget(self.w)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(laser)
        self.label_7.setStyleSheet("BACKGROUND-COLOR:grey;\n"
"font:bold;\n"
"")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.t = QtWidgets.QLineEdit(laser)
        self.t.setStyleSheet("BACKGROUND-COLOR:white;\n"
"")
        self.t.setObjectName("t")
        self.horizontalLayout_6.addWidget(self.t)
        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(laser)
        self.label_8.setStyleSheet("BACKGROUND-COLOR:grey;\n"
"font:bold;")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.tdash = QtWidgets.QLineEdit(laser)
        self.tdash.setStyleSheet("BACKGROUND-COLOR:white;\n"
"")
        self.tdash.setObjectName("tdash")
        self.horizontalLayout_7.addWidget(self.tdash)
        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_7)
        self.line_6 = QtWidgets.QFrame(laser)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_5.addWidget(self.line_6)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_12 = QtWidgets.QLabel(laser)
        self.label_12.setStyleSheet("BACKGROUND-COLOR:grey;\n"
"font:bold;")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.line = QtWidgets.QFrame(laser)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_9.addWidget(self.line)
        spacerItem9 = QtWidgets.QSpacerItem(13, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.tc = QtWidgets.QLineEdit(laser)
        self.tc.setStyleSheet("BACKGROUND-COLOR:white;\n"
"")
        self.tc.setObjectName("tc")
        self.horizontalLayout_9.addWidget(self.tc)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_13 = QtWidgets.QLabel(laser)
        self.label_13.setStyleSheet("BACKGROUND-COLOR:grey;\n"
"font:bold;")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_10.addWidget(self.label_13)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        self.pa = QtWidgets.QLineEdit(laser)
        self.pa.setStyleSheet("BACKGROUND-COLOR:white;\n"
"")
        self.pa.setText("")
        self.pa.setObjectName("pa")
        self.horizontalLayout_10.addWidget(self.pa)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(13, 49, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_17 = QtWidgets.QLabel(laser)
        self.label_17.setStyleSheet("BACKGROUND-COLOR:grey;\n"
"font:bold;")
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem12 = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.cfc = QtWidgets.QLineEdit(laser)
        self.cfc.setStyleSheet("BACKGROUND-COLOR:white;\n"
"")
        self.cfc.setObjectName("cfc")
        self.horizontalLayout_8.addWidget(self.cfc)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.line_2 = QtWidgets.QFrame(laser)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem13 = QtWidgets.QSpacerItem(318, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem13)
        self.calculate = QtWidgets.QPushButton(laser)
        self.calculate.setStyleSheet("\n"
"background-color:rgb(118, 118, 118) ;\n"
"font:bold;")
        self.calculate.setObjectName("calculate")
        self.horizontalLayout_17.addWidget(self.calculate)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem14)
        self.graph = QtWidgets.QPushButton(laser)
        self.graph.setStyleSheet("\n"
"background-color:rgb(118, 118, 118) ;\n"
"font:bold;")
        self.graph.setObjectName("graph")
        self.horizontalLayout_17.addWidget(self.graph)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.line_9 = QtWidgets.QFrame(laser)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_5.addWidget(self.line_9)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_5 = QtWidgets.QLabel(laser)
        self.label_5.setStyleSheet("BACKGROUND-COLOR:grey;\n"
"font:bold;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_12.addWidget(self.label_5)
        self.tnot = QtWidgets.QLineEdit(laser)
        self.tnot.setStyleSheet("BACKGROUND-COLOR:white;\n"
"")
        self.tnot.setObjectName("tnot")
        self.horizontalLayout_12.addWidget(self.tnot)
        spacerItem15 = QtWidgets.QSpacerItem(238, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem15)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_15 = QtWidgets.QLabel(laser)
        self.label_15.setStyleSheet("BACKGROUND-COLOR:grey;\n"
"font:bold;")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_13.addWidget(self.label_15)
        self.t1 = QtWidgets.QLineEdit(laser)
        self.t1.setStyleSheet("BACKGROUND-COLOR:white;\n"
"")
        self.t1.setMaxLength(32767)
        self.t1.setObjectName("t1")
        self.horizontalLayout_13.addWidget(self.t1)
        spacerItem16 = QtWidgets.QSpacerItem(118, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem16)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_16 = QtWidgets.QLabel(laser)
        self.label_16.setStyleSheet("BACKGROUND-COLOR:grey;\n"
"font:bold;")
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_14.addWidget(self.label_16)
        self.t2 = QtWidgets.QLineEdit(laser)
        self.t2.setStyleSheet("\n"
"background-color:white ;\n"
"")
        self.t2.setObjectName("t2")
        self.horizontalLayout_14.addWidget(self.t2)
        spacerItem17 = QtWidgets.QSpacerItem(88, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem17)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.line_3 = QtWidgets.QFrame(laser)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_6.addWidget(self.line_3)
        self.line_8 = QtWidgets.QFrame(laser)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_6.addWidget(self.line_8)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem18 = QtWidgets.QSpacerItem(488, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem18)
        self.reset = QtWidgets.QPushButton(laser)
        self.reset.setStyleSheet("\n"
"background-color:rgb(118, 118, 118) ;\n"
"font:bold;\n"
"")
        self.reset.setObjectName("reset")
        self.horizontalLayout_15.addWidget(self.reset)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem19)
        self.verticalLayout_6.addLayout(self.horizontalLayout_15)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.graph.raise_()
        self.line_6.raise_()
        self.line_9.raise_()

        self.retranslateUi(laser)
        self.reset.clicked.connect(self.pa.clear)
        self.reset.clicked.connect(self.tc.clear)
        self.reset.clicked.connect(self.tdash.clear)
        self.reset.clicked.connect(self.t.clear)
        self.reset.clicked.connect(self.tdoubledash.clear)
        self.reset.clicked.connect(self.w.clear)
        self.reset.clicked.connect(self.w2.clear)
        self.reset.clicked.connect(self.l1.clear)
        self.reset.clicked.connect(self.l.clear)
        self.reset.clicked.connect(self.cfc.clear)
        self.reset.clicked.connect(self.tnot.clear)
        self.reset.clicked.connect(self.t1.clear)
        self.reset.clicked.connect(self.t2.clear)
        QtCore.QMetaObject.connectSlotsByName(laser)

        self.calculate.setCheckable(True)
        self.calculate.clicked.connect(self.cal)
        self.graph.setCheckable(True)


        
       
        



    

    def cal(self):

        length=(self.l.text())
        power=(self.pa.text())
        width=(self.w.text())
        thick=(self.t.text())
        thickd=(self.tdash.text())
        length1=(self.l1.text())
        width2=(self.w2.text())
        thickdd=(self.tdoubledash.text())
        tempc=(self.tc.text())
        cf=(self.cfc.text())
        length=float(length)
        power=float(power)
        width=float(width)
        thick=float(thick)
        thickd=float(thickd)
        length1=float(length1)
        width2=float(width2)
        thickdd=float(thickdd)
        tempc=float(tempc)
        cf=float(cf)
    
        
        
        f=length1*width2*2
        ar=3.14*((width2/2)*(width2/2))
        v=(cf*1000)/(60*ar)
        h=0.00299*v+0.1917
        totalpower=0.30*(power*1000)*0.576

        try:
            t11=tempc+(totalpower*((thick/(4*0.14*f))+(1/(f*h))))
            self.tnot.setText(str(t11))
        except:
            print("invalid input")
       
    
        try:
            t12=(totalpower*thick)/(4*0.14*f)
            self.t1.setText(str(t12))
        except:
            print("invalid input")

        try:
            t13=totalpower/(f*h)
            self.t2.setText(str(t13))
        except:
            print("invalid input")

        self.graph.clicked.connect(lambda:self.gg(t11,t12,t13,width,width2,thick,thickd))


      
    def gg(self,t11,t12,t13,width,width2,thick,thickd):
        import pyqtgraph as pg
        import pyqtgraph.exporters
        import numpy as np
     
        a=t11
        b=t12
        c=t13
        ts=a-b
        tc=ts-c
        d=width+width2+thick+thickd
        e=((thick+thick)/2)+width/2
        f=((thick+thick)/2)+(width/2)+width2/2
        x1,y1=[0,a]
        x2,y2=[e,ts]
        x3,y3=[f,tc]


        
        x=[0,e,f]
        y=[a,ts,tc]
        plt = pg.plot()
        plt.setYRange(0,a+1)
        plt.setXRange(0,d)
        plt.setWindowTitle('Temperature vs distance graph')
        plt.showGrid(x=True,y=True)
        plt.setLabel('left', 'Temperature', units='deg celcius')
        plt.setLabel('bottom', 'Distance', units='cm')
        plt.plot(x, y, pen='b', symbol='x', symbolPen='b', symbolBrush=0.2, name='red')
        plt.show()        
        

    def retranslateUi(self, laser):
        _translate = QtCore.QCoreApplication.translate
        laser.setWindowTitle(_translate("laser", "laser"))
        laser.setWhatsThis(_translate("laser", "<html><head/><body><p>background color: grey;</p><p><br/></p></body></html>"))
        self.label.setText(_translate("laser", "TEMPERATURE DISTRIBUTION IN Nd:YAG DISK"))
        self.label_2.setText(_translate("laser", "Physical Dimension of 2% doped Nd:Yag  "))
        self.label_6.setText(_translate("laser", "Physical Dimension of cooling jacket:"))
        self.label_14.setText(_translate("laser", "units must be entered in cm,celsius & kW"))
        self.label_3.setText(_translate("laser", "Length"))
        self.label_9.setText(_translate("laser", "Length"))
        self.label_10.setText(_translate("laser", "Width"))
        self.label_11.setText(_translate("laser", "Thickness"))
        self.label_4.setText(_translate("laser", "Width"))
        self.label_7.setText(_translate("laser", "YAG:Nd and YAG:YAG thickness"))
        self.label_8.setText(_translate("laser", "Nd: YAG thickness"))
        self.label_12.setText(_translate("laser", "Temperature of coolant"))
        self.label_13.setText(_translate("laser", "Total Pump Power"))
        self.label_17.setText(_translate("laser", "Chiller pumping capacity(litre/min)"))
        self.calculate.setText(_translate("laser", "Calculate"))
        self.graph.setText(_translate("laser", "Graph"))
        self.label_5.setText(_translate("laser", "Temperature at centre"))
        self.label_15.setText(_translate("laser", "Temperature difference between centre and surface"))
        self.label_16.setText(_translate("laser", "Temperature difference between surface and coolant"))
        self.reset.setText(_translate("laser", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    laser = QtWidgets.QDialog()
    ui = Ui_laser()
    ui.setupUi(laser)
    laser.show()
    sys.exit(app.exec_())
