import click
import os

BANNER_POSTFIXES = [
  '1600', '1600-2x',
  '1310', '1310-2x',
  '1024', '1024-2x',
  'tablet', 'tablet-2x',
  'mobile', 'mobile-2x'
]

def set_banner_names(files: list, dist: str):
  base_name = click.prompt('Base name', default='banner')
  files_paths = [os.path.join(dist, file) for file in files]

  sorted_files = sorted(files_paths, key=os.path.getmtime)

  if len(sorted_files) != len(BANNER_POSTFIXES):
    click.echo('Number of files does not match number of banner postfixes')
    return

  for file_path, postfix in zip(sorted_files, BANNER_POSTFIXES):
    file_extension = os.path.splitext(file_path)[1]

    new_file_path = os.path.join(dist, f'{base_name}_{postfix}{file_extension}')
    os.rename(file_path, new_file_path)