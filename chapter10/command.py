"""
The Command Pattern (命令模式：用来给应用添加Undo操作)

命令模式帮助我们把一个操作(undo,redo,copy,paste等)封装成一个对象，通常是创建一个包含Operation所有逻辑和方法的类。 
通过命令模式可以控制命令的执行时间和过程，还可以用来组织事务。 
用一些文件操作类来说明命令模式的使用
"""
import os

verbose = True


class FileCommand:
    def execute(self):
        pass

    def redo(self):
        if verbose:
            print(f'redo: {self.__class__.__name__}')
        self.execute()


class RenameFile(FileCommand):
    def __init__(self, src, dest):
        """ 在init里保存一些必要信息，比如undo需要的老的和新的文件名 """
        self.src = src
        self.dest = dest

    def execute(self):
        if verbose:
            print(f"[renaming '{self.src}' to '{self.dest}']")
        os.rename(self.src, self.dest)

    def undo(self):
        if verbose:
            print(f"[renaming '{self.dest}' back to '{self.src}']")
        os.rename(self.dest, self.src)


class CreateFile(FileCommand):
    def __init__(self, path, txt='hello world\n'):
        self.path = path
        self.txt = txt

    def execute(self):
        if verbose:
            print(f"[creating file '{self.path}']")
        with open(self.path, 'w', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        delete_file(self.path)


class ReadFile(FileCommand):
    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print(f"[reading file '{self.path}']")
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')


def delete_file(path):
    if verbose:
        print(f"deleting file {path}")
    os.remove(path)


def main():

    orig_name, new_name = 'file1', 'file2'

    commands = (CreateFile(orig_name), ReadFile(orig_name),
                RenameFile(orig_name, new_name))

    [c.execute() for c in commands]

    answer = input('reverse the executed commands? [y/n] ')

    if answer not in 'yY':
        print(f"the result is {new_name}")
        exit()

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            print("Error", str(e))
    
    [c.redo() for c in commands[:2]]


if __name__ == "__main__":
    main()
