def is_file_image(file: str) -> bool:
  '''define if file has extention of (jpg, jpeg, png, gif)'''
  return file.endswith(('.jpg', '.jpeg', '.png', '.gif'))

def is_file_doc(file: str) -> bool:
  '''define if file has extention of (doc, docx, xls, xlsx, pdf)'''
  return file.endswith(('.doc', '.docx', '.xls', '.xlsx', '.pdf'))

def is_file_text(file: str) -> bool:
  '''define if file has extention of (txt, rtf)'''
  return file.endswith(('.txt', '.rtf'))

FILTERS = {
  'image': is_file_image,
  'doc': is_file_doc,
  'text': is_file_text,
}


def filter_files_by_type(files: list, filters: tuple) -> list:
  '''filter files by type'''
  return [file for file in files if any(FILTERS[filter](file) for filter in filters)]

