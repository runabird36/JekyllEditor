from __future__ import annotations
import sys
from PyQt5.QtWidgets import (
                                QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                                QPushButton, QApplication, QMessageBox, QSpacerItem,
                                QFrame, QSizePolicy
                            )
from PyQt5.QtCore import QUrl, Qt, QEasingCurve
from PyQt5.QtWebEngineWidgets import QWebEngineView
from functools import partial
from git import Repo, repo
from custom_qstacked_widgets import QStackedWidget
from functools import partial
from qt_material import apply_stylesheet


PAGE_INFO = {
                "markdown_test_page"    : "https://dillinger.io/",
                "admin_page"            : "http://127.0.0.1:4000/admin",
                "local_host_page"       : "http://127.0.0.1:4000"
             }


class CommandToolkit():
    @staticmethod
    def get_repo() -> repo.base.Repo:
        return Repo("/home/taiyeong.song/Desktop/pipeTemp/taiyeong.github.io")
    
    @staticmethod
    def git_add_all(tar_repo :repo.base.Repo) -> None:
        tar_repo.git.add(all=True)
        
    @staticmethod
    def git_commit(_repo :repo.base.Repo, _msg :str) -> None:
        _repo.git.commit('-m', _msg)
        
    @staticmethod
    def git_push(_repo :repo.base.Repo) -> None:
        _remote = _repo.remotes.origin
        _remote.push()
        
    @staticmethod
    def show_msg_box(_msg :str) -> None:
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(_msg)
        msgBox.setWindowTitle("Jekyll Page")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)

        # Executing the QMessageBox and handling the result
        result = msgBox.exec_()
        if result == QMessageBox.Ok:
            print("OK button clicked")
        elif result == QMessageBox.Cancel:
            print("Cancel button clicked")


class PageCalculator():
    
    
    def __init__(self) -> None:
        self.cur_index:int=0
        self.page_info:dict={}
        self.btn_info:dict={}
        self.set_idx(0)
    
    def set_idx(self, _idx :int) -> None:
        self.cur_index = _idx
    
    def get_idx(self) -> int:
        return self.cur_index
    
    def setup_page_info(self, _idx :int, _page_name :str) -> None:
        self.page_info[_page_name] = _idx
        
    def setup_btn_info(self, _idx :int, _btn_name :str) -> None:
        self.btn_info[_btn_name] = _idx
        
    def calc_count(self, to_btn_name :str) -> int:
        # print(self.btn_info[to_btn_name] , self.cur_index)
        to_count =  self.btn_info[to_btn_name] - self.cur_index
        self.set_idx(self.btn_info[to_btn_name])
        return to_count
        
        
class SignalSetter():
    def set_main_win(self, _win:MainView) -> None:
        self.main_view = MainView
        
    def set_btns_win(self, _win:BtnToolkit) -> None:
        self.btn_view = _win

    def set_viewport_win(self, _win:ViewPort) -> None:
        self.viewport_view = _win
        
    def set_calculator(self, _toolkit:PageCalculator) -> None:
        self.page_calculator = _toolkit
        
    def get_mian_win(self) -> MainView:
        return self.main_view
    
    def get_btns_win(self) -> BtnToolkit:
        return self.btn_view
    
    def get_viewport_win(self) -> ViewPort:
        return self.viewport_view
    
    def get_page_calculator(self) -> PageCalculator:
        return self.page_calculator
    
    def set_links(self) -> None:
        
        self.get_btns_win().get_md_checker_btn().clicked.connect(   partial(self.to_md_checker_view,    self.get_btns_win().get_md_checker_btn().text()))
        self.get_btns_win().get_admin_btn().clicked.connect(        partial(self.to_admin_view,         self.get_btns_win().get_admin_btn().text()))
        self.get_btns_win().get_local_btn().clicked.connect(        partial(self.to_local_view,         self.get_btns_win().get_local_btn().text()))
        
        self.get_btns_win().get_publish_btn().clicked.connect(self.do_publish)
        
    def to_md_checker_view(self, _btn_name :str) -> None:
        to_count = self.get_page_calculator().calc_count(_btn_name)
        self.activate_switcher(to_count)
        
    def to_admin_view(self, _btn_name :str) -> None:
        to_count = self.get_page_calculator().calc_count(_btn_name)
        self.activate_switcher(to_count)
    
    def to_local_view(self, _btn_name :str) -> None:
        to_count = self.get_page_calculator().calc_count(_btn_name)
        self.activate_switcher(to_count)
        
    def activate_switcher(self, _to_count :int) -> None:
        if _to_count == -2:
            self.get_viewport_win().get_switcher().doubleSlideToPreviousWidget()
        
        elif _to_count == -1:
            self.get_viewport_win().get_switcher().slideToPreviousWidget()
            
        elif _to_count == 0:
            pass
    
        elif _to_count == 1:
            self.get_viewport_win().get_switcher().slideToNextWidget()
            
        elif _to_count == 2:
            self.get_viewport_win().get_switcher().doubleSlideToNextWidget()
            
    def do_publish(self) -> None:
        _is_clear = True
        try:
            _repo = CommandToolkit.get_repo()
            try:
                CommandToolkit.git_add_all(_repo)
                CommandToolkit.git_commit(_repo, "Publish by Python")
            except:
                pass
            CommandToolkit.git_push(_repo)
        except:
            _is_clear = False
        
        if _is_clear == True:
            CommandToolkit.show_msg_box("Complete publish !\nURL : https://taiyeong.github.io/")
        else:
            CommandToolkit.show_msg_box("Error : Fail publish")
            
class BtnToolkit(QWidget):
    def __init__(self, _parent:QWidget=None) -> None:
        super(BtnToolkit, self).__init__(_parent)
        
        self.to_md_checker_btn  = QPushButton("Check Markdown")
        self.to_admin_btn       = QPushButton("Admin Page")
        self.to_local_btn       = QPushButton("Check in Local")
        self.publish_btn        = QPushButton("Publish")
        
        self.main_vl = QVBoxLayout()
        self.main_vl.addWidget(self.to_local_btn)
        self.main_vl.addWidget(self.to_admin_btn)
        self.main_vl.addWidget(self.to_md_checker_btn)
        self.main_vl.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.main_vl.addWidget(self.publish_btn)
        self.setLayout(self.main_vl)
        
    def get_md_checker_btn(self) -> QPushButton:
        return self.to_md_checker_btn
    
    def get_admin_btn(self) -> QPushButton:
        return self.to_admin_btn
    
    def get_local_btn(self) -> QPushButton:
        return self.to_local_btn
    
    def get_publish_btn(self) -> QPushButton:
        return self.publish_btn

class WebPage(QWebEngineView):
    def __init__(self, parent: QWidget = None, _page_name:str="", _url:str="") -> None:
        super(WebPage, self).__init__(parent)
        self.page_name = _page_name
        self.load(QUrl(_url))
        
    def set_url(self, _url:str="") -> None:
        self.load(QUrl(_url))
        
    def get_url(self) -> str:
        self.url().url()
        
    def get_page_name(self) -> str:
        return self.page_name
        
        

class ViewPort(QWidget):
    def __init__(self, parent: QWidget =None) -> None:
        super(ViewPort, self).__init__(parent)

        

        self.page01 = WebPage(_page_name="local_host_page",_url=PAGE_INFO.get("local_host_page"))
        self.page02 = WebPage(_page_name="admin_page",_url=PAGE_INFO.get("admin_page"))
        self.page03 = WebPage(_page_name="markdown_test_page",_url=PAGE_INFO.get("markdown_test_page"))
        
        self.view_switcher_sw = QStackedWidget()
        self.view_switcher_sw.setTransitionDirection(Qt.Vertical)
        self.view_switcher_sw.setTransitionEasingCurve(QEasingCurve.OutCubic)
        self.view_switcher_sw.setSlideTransition(True)
        self.view_switcher_sw.addWidget(self.page01)
        self.view_switcher_sw.addWidget(self.page02)
        self.view_switcher_sw.addWidget(self.page03)
        
        self.main_vl = QVBoxLayout()
        self.main_vl.addWidget(self.view_switcher_sw)
        _m = 3
        self.main_vl.setContentsMargins(_m, _m, _m, _m)
        self.setLayout(self.main_vl)
        
        
        
    def get_switcher(self) -> QStackedWidget:
        return self.view_switcher_sw
    
    


    
class MainView(QMainWindow):
    def __init__(self, _parent:QWidget=None) -> None:
        super(MainView, self).__init__(_parent)
        
        
        
        self.signal_setter      = SignalSetter()
        self.page_calculator    = PageCalculator()
        
        self.setupUi()
        
    def setupUi(self) -> None:
        
        self.btn_toolkit_wg = BtnToolkit()
        
        self.btn_layout_vl = QVBoxLayout()
        self.btn_layout_vl.addWidget(self.btn_toolkit_wg)
        
        self.btn_containier_frame = QFrame()
        self.btn_containier_frame.setLayout(self.btn_layout_vl)
        
        
        self.main_viewport = ViewPort()
        

        
        self.main_hl = QHBoxLayout()
        self.main_hl.addWidget(self.btn_containier_frame)
        self.main_hl.addWidget(self.main_viewport)
        self.main_hl.setStretch(0, 1)
        self.main_hl.setStretch(1, 8)
        
        self.main_wg = QWidget()
        self.main_wg.setLayout(self.main_hl)
        self.setCentralWidget(self.main_wg)
        
        self.resize(1600, 1000)
        
        apply_stylesheet(self, "dark_blue.xml")
        
        
        
        self.page_calculator.setup_btn_info(0, self.btn_toolkit_wg.to_local_btn.text())
        self.page_calculator.setup_btn_info(1, self.btn_toolkit_wg.to_admin_btn.text())
        self.page_calculator.setup_btn_info(2, self.btn_toolkit_wg.to_md_checker_btn.text())
        

        self.page_calculator.setup_page_info(0, self.main_viewport.page01.get_page_name())
        self.page_calculator.setup_page_info(1, self.main_viewport.page02.get_page_name())
        self.page_calculator.setup_page_info(2, self.main_viewport.page03.get_page_name())
        
        
        
        self.signal_setter.set_main_win(self)
        self.signal_setter.set_btns_win(self.btn_toolkit_wg)
        self.signal_setter.set_viewport_win(self.main_viewport)
        self.signal_setter.set_calculator(self.page_calculator)
        self.signal_setter.set_links()
        

        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    _view = MainView()
    _view.show()
    
    app.exec_()