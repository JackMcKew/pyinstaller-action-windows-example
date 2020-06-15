# import argparse
from gooey import Gooey, GooeyParser
import os

@Gooey(optional_cols=2,program_name="Gooey Executable with Pyinstaller")
def parse_args():
    prog_descrip = 'Pyinstaller example with Gooey'
    parser = GooeyParser(description=prog_descrip)

    sub_parsers = parser.add_subparsers(help='commands', dest='command')

    first_parser = sub_parsers.add_parser('file',help='This function prints the chosen file name')

    first_parser.add_argument('file_path',help='Select a random file',type=str,widget='FileChooser')

    first_parser.add_argument('--file-size',help='Do you want to print the file size?',action='store_true')

    second_parser = sub_parsers.add_parser('folder',help='This funtion prints all files in a folder')

    second_parser.add_argument('folder_path',help='Select a folder',type=str,widget='DirChooser')

    second_parser.add_argument('--file-type',help='Specify file type with .jpg',type=str)

    args = parser.parse_args()

    return args

def print_file_name(path,filesize):
    """
    Inputs:
        path (str): filepath to file selected
        filezize (bool): whether to print the file size or not
    Prints file name of file from path given and if filesize is true then will print the total size of the file in bytes
    """
    print(os.path.basename(path))
    if filesize:
        print(f"File size: {os.path.getsize(path)} bytes")

def get_files_in_folder(path,extension):
    """
    Inputs:
        path (str): path to folder selected
        extension (str): extension to filter by
    Prints all files in folder, if an extension is given, will only print the files with the given extension
    """
    f = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        if extension:
            for filename in filenames:
                if filename.endswith(extension):
                    f.append(filename)
        else:
            f.extend(filenames)
    return f


if __name__ == '__main__':
    conf = parse_args()
    if conf.command == 'file':
        print_file_name(conf.file_path,conf.file_size)
    elif conf.command == 'folder':
        print(get_files_in_folder(conf.folder_path,conf.file_type))


