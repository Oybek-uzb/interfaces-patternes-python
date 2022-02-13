from abc import ABC, abstractmethod


class Editor:
    clipboard = None

    def __init__(self, text: str):
        self.text = text


class EditorCommand(ABC):

    def __init__(self, editor):
        self.editor = editor

    @abstractmethod
    def execute(self) -> None:
        pass


class CopyCommand(EditorCommand):
    __backup = None

    def __int__(self, editor: Editor) -> None:
        super().__init__(editor)

    def execute(self) -> None:
        self._backup()
        self.editor.clipboard = self.editor.text

    def rollback(self):
        self.editor.clipboard = self.__backup

    def _backup(self):
        self.__backup = self.editor.clipboard


class PasteCommand(EditorCommand):
    __backup = None

    def __init__(self, edit: Editor) -> None:
        super().__init__(edit)

    def execute(self) -> None:
        self._backup()
        self.editor.text = self.editor.clipboard

    def rollback(self):
        self.editor.text = self.__backup

    def _backup(self):
        self.__backup = self.editor.text


if __name__ == '__main__':
    e = Editor(text="hello")
    copy_command = CopyCommand(editor=e)
    copy_command.execute()
    print(e.clipboard)
    print(e.text)
    copy_command.rollback()
    print(e.clipboard)
    print(e.text)
