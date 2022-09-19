'''
copymp3: Copy MP3 files to another directory
Copyright (C) 2022  Rafael Delgado Martins

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import click
from copymp3 import core


@click.command()
@click.argument('source', type=click.Path())
@click.argument('dest', type=click.Path())
@click.option(
    '-s',
    '--synchronize',
    is_flag=True,
    help='''
    Delete from DEST files that don\' exist in SOURCE and copy only new
    files.
    '''
)
@click.option(
    '-f',
    '--flatten',
    is_flag=True,
    help='Put all files on the root of DEST'
)
def main(source, dest, synchronize, flatten):
    ''' Copy MP3 files from SOURCE to DEST. '''
    click.echo('''
    copymp3 Copyright (C) 2022  Rafael Delgado Martins
    This program comes with ABSOLUTELY NO WARRANTY;
    This is free software, and you are welcome to redistribute it
    under certain conditions.
    ''')

    mp3_files = core.find_mp3_files(source)
    click.echo(mp3_files)


if __name__ == '__main__':
    main()
