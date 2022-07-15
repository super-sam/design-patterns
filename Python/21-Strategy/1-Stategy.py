from abc import ABC
from enum import Enum, auto

class ListStrategy(ABC):
    def start(self, buffer): pass
    def end(self, buffer): pass
    def add_list_item(self, buffer, item): pass


class MarkDownListStrategy(ListStrategy):
    def add_list_item(self, buffer, item):
        buffer.append(f" * {item}\n")


class HTMLListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append("<ul>\n")

    def add_list_item(self, buffer, item):
        buffer.append(f"    <li>{item}</li>\n")

    def end(self, buffer):
        buffer.append("</ul>\n")


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


class TextProcessor:
    def __init__(self, list_stategy=HTMLListStrategy):
        self.buffer = []
        self.list_strategy = list_stategy

    def append_list(self, items):
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(self.buffer, item)
        self.list_strategy.end(self.buffer)

    def set_output_fromat(self, format):
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkDownListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HTMLListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return "".join(self.buffer)


if __name__ == "__main__":
    items = ['foo', 'bar', 'baz']
    tp = TextProcessor()
    tp.set_output_fromat(OutputFormat.MARKDOWN)
    tp.append_list(items)
    print(tp)
    tp.set_output_fromat(OutputFormat.HTML)
    tp.clear()
    tp.append_list(items)
    print(tp)