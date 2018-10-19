from oslo_utils import fileutils
import os
import shutil

path = 'path/to/here'
fileutils.ensure_tree(path)

file = fileutils.write_to_tempfile('hello fileutils', path)
print("template file " + file)

for n in ['sha1', 'md5', 'sha256']:
    print(fileutils.compute_file_checksum(file, read_chunksize=65536, algorithm=n))

print(fileutils.last_bytes(file, 1))
print(fileutils.last_bytes(file, 10000))

fileutils.delete_if_exists(file)

# any exception will cause the path to be deleted.
#fileutils.remove_path_on_error(path)

# fileutils have no routine for directory :(
shutil.rmtree('path')
