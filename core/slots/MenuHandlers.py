from ui.editor import TextEdit

def file_new(main_window):
    tab_widget = main_window.centralWidget()
    tab_widget.addTab(TextEdit("", tab_widget), "new1")
