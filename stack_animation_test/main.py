########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
from PySide2.QtCore import *

########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################


########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()
        ########################################################################
        ## 
        ########################################################################

        ########################################################################
        ## QSTACKWIDGETS NAVIGATION
        ########################################################################
        # self.ui.prev.clicked.connect(lambda: self.ui.stackedWidget.slideToPreviousWidget())
        # self.ui.nxt.clicked.connect(lambda: self.ui.stackedWidget.slideToNextWidget())

        # self.ui.page1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        # self.ui.page2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        ########################################################################
        ## 
        ########################################################################

        ########################################################################
        ## QSTACKWIDGETS ANIMATION
        # ########################################################################        
        # self.ui.stackedWidget.setTransitionDirection(QtCore.Qt.Vertical)
        # self.ui.stackedWidget.setTransitionSpeed(500)
        # self.ui.stackedWidget.setTransitionEasingCurve(QtCore.QEasingCurve.Linear)
        # # ACTIVATE Animation
        # self.ui.stackedWidget.setSlideTransition(True)

        # # Fade animation
        # self.ui.stackedWidget.setFadeSpeed(500)
        # self.ui.stackedWidget.setFadeCurve(QtCore.QEasingCurve.Linear)
        # self.ui.stackedWidget.setFadeTransition(True)
        ########################################################################
        ## 
        ########################################################################

        ########################################################################
        ## LOAD QSTACKWIDGETS ANIMATION AND NAVIGATIONS FROM JSON FILE
        ########################################################################
        loadJsonStyle(self.ui)
        ########################################################################
        ## 
        ########################################################################




########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
