# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/datawork/repo/mgear4/release/scripts/mgear/shifter_epic_components/EPIC_spine_01/settingsUI.ui',
# licensing of 'C:/datawork/repo/mgear4/release/scripts/mgear/shifter_epic_components/EPIC_spine_01/settingsUI.ui' applies.
#
# Created: Thu Jan 19 11:29:12 2023
#      by: pyside2-uic  running on PySide2 5.12.5
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(279, 308)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.softness_label = QtWidgets.QLabel(self.groupBox)
        self.softness_label.setObjectName("softness_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.softness_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.softness_slider = QtWidgets.QSlider(self.groupBox)
        self.softness_slider.setMinimumSize(QtCore.QSize(0, 15))
        self.softness_slider.setMaximum(100)
        self.softness_slider.setOrientation(QtCore.Qt.Horizontal)
        self.softness_slider.setObjectName("softness_slider")
        self.horizontalLayout_3.addWidget(self.softness_slider)
        self.softness_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.softness_spinBox.setMaximum(100)
        self.softness_spinBox.setObjectName("softness_spinBox")
        self.horizontalLayout_3.addWidget(self.softness_spinBox)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.softness_label_2 = QtWidgets.QLabel(self.groupBox)
        self.softness_label_2.setObjectName("softness_label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.softness_label_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.position_slider = QtWidgets.QSlider(self.groupBox)
        self.position_slider.setMinimumSize(QtCore.QSize(0, 15))
        self.position_slider.setMaximum(100)
        self.position_slider.setOrientation(QtCore.Qt.Horizontal)
        self.position_slider.setObjectName("position_slider")
        self.horizontalLayout_4.addWidget(self.position_slider)
        self.position_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.position_spinBox.setMaximum(100)
        self.position_spinBox.setObjectName("position_spinBox")
        self.horizontalLayout_4.addWidget(self.position_spinBox)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.softness_label_3 = QtWidgets.QLabel(self.groupBox)
        self.softness_label_3.setObjectName("softness_label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.softness_label_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lockOri_pelvis_slider = QtWidgets.QSlider(self.groupBox)
        self.lockOri_pelvis_slider.setMinimumSize(QtCore.QSize(0, 15))
        self.lockOri_pelvis_slider.setMaximum(100)
        self.lockOri_pelvis_slider.setOrientation(QtCore.Qt.Horizontal)
        self.lockOri_pelvis_slider.setObjectName("lockOri_pelvis_slider")
        self.horizontalLayout_5.addWidget(self.lockOri_pelvis_slider)
        self.lockOri_pelvis_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.lockOri_pelvis_spinBox.setMaximum(100)
        self.lockOri_pelvis_spinBox.setObjectName("lockOri_pelvis_spinBox")
        self.horizontalLayout_5.addWidget(self.lockOri_pelvis_spinBox)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.softness_label_4 = QtWidgets.QLabel(self.groupBox)
        self.softness_label_4.setObjectName("softness_label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.softness_label_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lockOri_chest_slider = QtWidgets.QSlider(self.groupBox)
        self.lockOri_chest_slider.setMinimumSize(QtCore.QSize(0, 15))
        self.lockOri_chest_slider.setMaximum(100)
        self.lockOri_chest_slider.setOrientation(QtCore.Qt.Horizontal)
        self.lockOri_chest_slider.setObjectName("lockOri_chest_slider")
        self.horizontalLayout_6.addWidget(self.lockOri_chest_slider)
        self.lockOri_chest_spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.lockOri_chest_spinBox.setMaximum(100)
        self.lockOri_chest_spinBox.setObjectName("lockOri_chest_spinBox")
        self.horizontalLayout_6.addWidget(self.lockOri_chest_spinBox)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)
        self.maxStretch_label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxStretch_label.sizePolicy().hasHeightForWidth())
        self.maxStretch_label.setSizePolicy(sizePolicy)
        self.maxStretch_label.setObjectName("maxStretch_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.maxStretch_label)
        self.maxStretch_spinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxStretch_spinBox.sizePolicy().hasHeightForWidth())
        self.maxStretch_spinBox.setSizePolicy(sizePolicy)
        self.maxStretch_spinBox.setMinimum(1.0)
        self.maxStretch_spinBox.setSingleStep(0.1)
        self.maxStretch_spinBox.setProperty("value", 1.5)
        self.maxStretch_spinBox.setObjectName("maxStretch_spinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.maxStretch_spinBox)
        self.maxSquash_label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxSquash_label.sizePolicy().hasHeightForWidth())
        self.maxSquash_label.setSizePolicy(sizePolicy)
        self.maxSquash_label.setObjectName("maxSquash_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.maxSquash_label)
        self.maxSquash_spinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxSquash_spinBox.sizePolicy().hasHeightForWidth())
        self.maxSquash_spinBox.setSizePolicy(sizePolicy)
        self.maxSquash_spinBox.setMinimum(0.1)
        self.maxSquash_spinBox.setMaximum(1.0)
        self.maxSquash_spinBox.setSingleStep(0.1)
        self.maxSquash_spinBox.setProperty("value", 0.5)
        self.maxSquash_spinBox.setObjectName("maxSquash_spinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.maxSquash_spinBox)
        self.divisions_label = QtWidgets.QLabel(self.groupBox)
        self.divisions_label.setObjectName("divisions_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.divisions_label)
        self.division_spinBox = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.division_spinBox.sizePolicy().hasHeightForWidth())
        self.division_spinBox.setSizePolicy(sizePolicy)
        self.division_spinBox.setMinimum(2)
        self.division_spinBox.setMaximum(99)
        self.division_spinBox.setProperty("value", 4)
        self.division_spinBox.setObjectName("division_spinBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.division_spinBox)
        self.autoBend_label = QtWidgets.QLabel(self.groupBox)
        self.autoBend_label.setObjectName("autoBend_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.autoBend_label)
        self.autoBend_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.autoBend_checkBox.setText("")
        self.autoBend_checkBox.setObjectName("autoBend_checkBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.autoBend_checkBox)
        self.autoBend_label_2 = QtWidgets.QLabel(self.groupBox)
        self.autoBend_label_2.setObjectName("autoBend_label_2")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.autoBend_label_2)
        self.IKWorldOri_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.IKWorldOri_checkBox.setText("")
        self.IKWorldOri_checkBox.setObjectName("IKWorldOri_checkBox")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.IKWorldOri_checkBox)
        self.centralTangent_label = QtWidgets.QLabel(self.groupBox)
        self.centralTangent_label.setObjectName("centralTangent_label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.centralTangent_label)
        self.centralTangent_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.centralTangent_checkBox.setText("")
        self.centralTangent_checkBox.setObjectName("centralTangent_checkBox")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.centralTangent_checkBox)
        self.squashStretchProfile_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.squashStretchProfile_pushButton.setObjectName("squashStretchProfile_pushButton")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.SpanningRole, self.squashStretchProfile_pushButton)
        self.leafJoints_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.leafJoints_checkBox.setText("")
        self.leafJoints_checkBox.setObjectName("leafJoints_checkBox")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.leafJoints_checkBox)
        self.leafJoints_label = QtWidgets.QLabel(self.groupBox)
        self.leafJoints_label.setObjectName("leafJoints_label")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.leafJoints_label)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.softness_slider, QtCore.SIGNAL("sliderMoved(int)"), self.softness_spinBox.setValue)
        QtCore.QObject.connect(self.softness_spinBox, QtCore.SIGNAL("valueChanged(int)"), self.softness_slider.setValue)
        QtCore.QObject.connect(self.position_slider, QtCore.SIGNAL("valueChanged(int)"), self.position_spinBox.setValue)
        QtCore.QObject.connect(self.position_spinBox, QtCore.SIGNAL("valueChanged(int)"), self.position_slider.setValue)
        QtCore.QObject.connect(self.lockOri_pelvis_spinBox, QtCore.SIGNAL("valueChanged(int)"), self.lockOri_pelvis_slider.setValue)
        QtCore.QObject.connect(self.lockOri_pelvis_slider, QtCore.SIGNAL("valueChanged(int)"), self.lockOri_pelvis_spinBox.setValue)
        QtCore.QObject.connect(self.softness_slider, QtCore.SIGNAL("valueChanged(int)"), self.softness_spinBox.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.softness_label.setText(QtWidgets.QApplication.translate("Form", "Softness", None, -1))
        self.softness_label_2.setText(QtWidgets.QApplication.translate("Form", "Position", None, -1))
        self.softness_label_3.setText(QtWidgets.QApplication.translate("Form", "Lock Orient Pelvis", None, -1))
        self.softness_label_4.setText(QtWidgets.QApplication.translate("Form", "Lock Orient Chest", None, -1))
        self.maxStretch_label.setText(QtWidgets.QApplication.translate("Form", "Max Stretch", None, -1))
        self.maxSquash_label.setText(QtWidgets.QApplication.translate("Form", "Max Squash", None, -1))
        self.divisions_label.setText(QtWidgets.QApplication.translate("Form", "Divisions", None, -1))
        self.autoBend_label.setText(QtWidgets.QApplication.translate("Form", "Auto Bend Control", None, -1))
        self.autoBend_label_2.setText(QtWidgets.QApplication.translate("Form", "IK CTL World Ori", None, -1))
        self.IKWorldOri_checkBox.setToolTip(QtWidgets.QApplication.translate("Form", "<html><head/><body><p>If checked the IK controls will be oriented to world space in XYZ</p></body></html>", None, -1))
        self.centralTangent_label.setText(QtWidgets.QApplication.translate("Form", "Central Tangent", None, -1))
        self.squashStretchProfile_pushButton.setText(QtWidgets.QApplication.translate("Form", "Squash and Stretch Profile", None, -1))
        self.leafJoints_label.setText(QtWidgets.QApplication.translate("Form", "Leaf Joints", None, -1))

