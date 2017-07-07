def save_file(main_window=None):
    pass

def new_file(main_window=None):
    tab_widget = main_window.centralWidget()
    tab_widget.addTab(TextEdit("", tab_widget), "new %s" % tab_widget.next_tab_number)

__all__ = ['save_file']
