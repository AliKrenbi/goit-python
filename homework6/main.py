from pathlib import Path
import shutil
import sys
import sort as parser
from normalize import normalize


def handle_audio(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_documents(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_images(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))

def handle_video(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_archive(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))

    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'Це не архів {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Помилка видалення папки {folder}')


def main(folder: Path):
    parser.scan(folder)
    for file in parser.PPTX:
        handle_media(file, folder / 'documents' )
    for file in parser.XLSX:
        handle_media(file, folder / 'documents' )
    for file in parser.PDF:
        handle_media(file, folder / 'documents' )
    for file in parser.TXT:
        handle_media(file, folder / 'documents' )
    for file in parser.DOCX:
        handle_media(file, folder / 'documents' )
    for file in parser.DOC:
        handle_media(file, folder / 'documents' )
    for file in parser.MKV:
        handle_media(file, folder / 'video' )
    for file in parser.MOV:
        handle_media(file, folder / 'video' )
    for file in parser.MP4:
        handle_media(file, folder / 'video' )
    for file in parser.AVI:
        handle_media(file, folder / 'video' )
    for file in parser.JPEG:
        handle_media(file, folder / 'images' )
    for file in parser.JPG:
        handle_media(file, folder / 'images' )
    for file in parser.PNG:
        handle_media(file, folder / 'images' )
    for file in parser.SVG:
        handle_media(file, folder / 'images' )
    for file in parser.MP3:
        handle_media(file, folder / 'audio' )
    for file in parser.OGG:
        handle_media(file, folder / 'audio' )
    for file in parser.WAV:
        handle_media(file, folder / 'audio' )
    for file in parser.AMR:
        handle_media(file, folder / 'audio' )

    for file in parser.MY_OTHER:
        handle_other(file, folder / 'MY_OTHER')
    for file in parser.ZIP:
        handle_archive(file, folder / 'archives')
    for file in parser.GZ:
        handle_archive(file, folder / 'archives')
    for file in parser.TAR:
        handle_archive(file, folder / 'archives')

    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)


if __name__ == '__main__':
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        print(f'Start in folder {folder_for_scan.resolve()}')
        main(folder_for_scan.resolve())
