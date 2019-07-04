# -*- coding: utf-8 -*-
import datetime
import json
import re
import util
import os

"""Main module."""
# Replace follwoing dirs with real paths
# These are for testing and will remove them in future
IMGFPATH = "../applebackup/test"
STOREPATH = "../applebackup/test/convert/"


def getfiles(FileName="tetsFile"):
    """ Test Apple Importer method"""
    return FileName


def check_dir(date):
    # Check whether the dir is exits with given date
    # Date is given in yyyy:mm:dd hh:mm:ss format
    hdate = date.replace(':', '-')
    destdname = hdate.split(' ')[0]
    # File name is [created date yyyy-mm-dd-hh-mm-ss]- OrigianlFilename
    dpath = STOREPATH + destdname
    if not os.path.isdir(dpath):
        cmd = ['mkdir', '-p']
        cmd.append(dpath)
        util.call_process(cmd)
    return dpath


def excute():
    cmd = ['exiftool', '-j', '-CreateDate', '-DateCreated', '-FileType']
    cmd.append(IMGFPATH)
    flist_json = util.call_process(cmd)
    flist = json.loads(flist_json)
    # Do convert each file in the list
    for f in flist:
        # HEIC file has CreateDate tag and PNG and some other image
        # files has DateCreated tag.
        ftype = f.get('FileType')
        fpath = f.get('SourceFile')
        # Some files does not have Created datestamp
        # Move them to directory name 'unknown' with
        # current datetime stamp as the file name
        if not f.get('CreateDate') or f.get('DateCreated'):
            created = "{0:%Y:%m:%d %H:%M:%S}".format(datetime.datetime.now())
            dpath = STOREPATH + 'unknown'
            cmd = ['mkdir', '-p']
            cmd.append(dpath)
            util.call_process(cmd)
            cmd = ['cp']
            cmd.append(fpath)
            cmd.append(dpath)
            
        if ftype == 'HEIC':
            # HEIC files need to convert to jpg
            # and save in to the  directory with created date
            created = f.get('CreateDate')
            # Destination directory name is the date of file created
            # Use the time stamp of the file to get the directory name
            # Directory name format is yyyy-mm-dd
            dpath = check_dir(created)
            # Covert HEIC to jpg
            # Output file name is yyyy-mm-dd-hh-mm-ss-original_filename.jpg
            output_f_name = re.sub(r' |:', '-', created) + fpath.split(
                '/')[-1].split('.')[0] + '.jpg'
            print(output_f_name)
            # Call Convert here
        if ftype == 'JPEG' or ftype == 'MOV':
            created = f.get('CreateDate')
            dpath = check_dir(created)
            cmd = ['cp']
            cmd.append(fpath)
            cmd.append(dpath)
            util.call_process(cmd)


if __name__ == "__main__":
    excute()
