#! /usr/bin/env python

import logging

from models.drive import Drive

def main():
    drive = Drive()
    
    spreadsheets = drive.list_spreadsheets()
    
    worksheets = drive.list_worksheets('Matsumoto Family Directory')
    
    cells = drive.list_cells('Matsumoto Family Directory', 'Current')
    logging.info(cells)

if __name__ == "__main__":
    main()