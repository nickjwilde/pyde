import re
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat
from PyQt5.QtCore import Qt

class PyHighlighter(QSyntaxHighlighter):
    """ Class to handle syntax highlighting on TextEdit """

    format = QTextCharFormat()
    format.setForeground(Qt.blue)
    keywords = [
        r'\bFalse\b',
        r'\bNone\b',
        r'\bTrue\b',
        r'\band\b',
        r'\bas\b'
        r'\bassert\b',
        r'\bbreak\b',
        r'\bclass\b',
        r'\bcontinue\b',
        r'\bdef\b',
        r'\bdel\b',
        r'\belif\b',
        r'\belse\b',
        r'\bexcept\b',
        r'\bfinally\b',
        r'\bfor\b',
        r'\bfrom\b',
        r'\bglobal\b',
        r'\bif\b',
        r'\bimport\b',
        r'\bin\b',
        r'\bis\b',
        r'\blambda\b',
        r'\bnonlocal\b',
        r'\bnot\b',
        r'\bor\b',
        r'\bpass\b',
        r'\braise\b',
        r'\breturn\b',
        r'\btry\b',
        r'\bwhile\b',
        r'\bwith\b',
        r'\byield\b']

    def __init__(self, parent=None):
        super().__init__(parent)

    def highlightBlock(self, text):
        for kwd in self.keywords:
            match = re.search(kwd, text)
            if match is None:
                continue
            index = match.start()
            length = match.end() - match.start()
            self.setFormat(index, length, self.format)