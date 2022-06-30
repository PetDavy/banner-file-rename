import click
import os
from . filters import FILTERS, filter_files_by_type
from . banner_names import set_banner_names

@click.command()
@click.option('--filter', '-f', multiple=True, type=click.Choice(FILTERS.keys()), default=['image'], help='Filter files by type')
@click.option('--banners', '-b', is_flag=True, help='Rename files for banners patterns')
@click.argument('dist', type=click.Path(exists=True))
def run(dist, banners, filter):
    '''Welcome to renamefiles'''
    files = os.listdir(dist)
    filtered_files = filter_files_by_type(files, filters=filter)

    if banners:
        set_banner_names(files=filtered_files, dist=dist)
