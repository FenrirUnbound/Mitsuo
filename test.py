#! /usr/bin/env python

import logging

from lib.directory import Directory
from models.drive import Drive

def main():
    _spreadsheet = "Matsumoto Family Directory"
    _worksheet = "Current"
        
    directory = _load_directory()
    
    logging.info(directory.get_directory())

def _load_directory():
    """
    """
    _spreadsheet = "Matsumoto Family Directory"
    _worksheet = "Current"
        
    directory = Directory()
    drive = Drive()
        
    data = drive.get_data(_spreadsheet, _worksheet)
    name_list = data[1][1:]
        
    directory.adds(name_list)
        
    return directory

def _parse_for_names():
    """Parse an email's body for the names of people
    """
    result = ['George Washington', 'The League', 'Rodney Ruxin', 'The Sacco']

    return result


if __name__ == "__main__":
    main()