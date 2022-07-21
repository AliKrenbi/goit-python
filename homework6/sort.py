import sys
from pathlib import Path

DOCUMENTS = []
IMAGES = []
MUSIC = []
VIDEO = []
AUDIO = []
MY_OTHER = []
ARCHIVES = []

REGISTER_EXTENSIONS = {
    'DOC': DOCUMENTS, 'DOCX': DOCUMENTS, 'TXT': DOCUMENTS, 'PDF': DOCUMENTS, 'XLSX': DOCUMENTS, 'PPTX': DOCUMENTS,
    'JPEG': IMAGES, 'PNG': IMAGES, 'JPG': IMAGES, 'SVG': IMAGES,
    'AVI': VIDEO, 'MP4': VIDEO, 'MOV': VIDEO, 'MKV': VIDEO,
    'MP3': AUDIO, 'OGG': AUDIO, 'WAV': AUDIO, 'AMR': AUDIO,
    'ZIP': ARCHIVES, 'GZ': ARCHIVES, 'TAR': ARCHIVES
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()

def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].upper()

def scan(folder: Path) -> None:
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        ext = get_extension(item.name)  
        fullname = folder / item.name 
        if not ext:  
            MY_OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHER.append(fullname)

if __name__ == '__main__':

    folder_for_scan = sys.argv[1]
    print(f'Start in folder {folder_for_scan}')

    scan(Path(folder_for_scan))
    print(FOLDERS[::-1])                        