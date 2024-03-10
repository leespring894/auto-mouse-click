# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainDlg.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(233, 173)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelUsage = QLabel(self.groupBox)
        self.labelUsage.setObjectName(u"labelUsage")

        self.verticalLayout.addWidget(self.labelUsage)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelStatus = QLabel(self.groupBox_2)
        self.labelStatus.setObjectName(u"labelStatus")

        self.verticalLayout_2.addWidget(self.labelStatus)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Auto Mouse Click", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Usage", None))
        self.labelUsage.setText(QCoreApplication.translate("Dialog", u"F2 : Toggle auto click mouse.\n"
"F3 : Toggle auto move mouse.\n"
"F12 : Terminate this program.", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Status", None))
        self.labelStatus.setText(QCoreApplication.translate("Dialog", u"<B>Disabled</B>", None))
    # retranslateUi

