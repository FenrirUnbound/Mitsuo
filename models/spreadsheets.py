#! /usr/bin/env python

import logging

import gdata.spreadsheet.service

from lib.directory import Directory
from lib.my_user import User
from models.drive import Drive

def main():
    drive = Drive()
    
    spreadsheets = drive.spreadsheets()
    worksheets = drive.worksheets('Matsumoto Family Directory')

def normal():
    names = []
    user = User()

    client = gdata.spreadsheet.service.SpreadsheetsService()
    client.ClientLogin(user.email, user.ticket)

    # Spreadsheets
    feed = client.GetSpreadsheetsFeed()
    
    logging.info(feed)
    
    id_parts = feed.entry[0].id.text.split('/')
    spreadsheet = id_parts[len(id_parts) - 1]

    # Worksheets within the Spreadsheet
    wsFeed = client.GetWorksheetsFeed(spreadsheet)
    id_parts = wsFeed.entry[0].id.text.split('/')
    worksheet = id_parts[len(id_parts) - 1]

    # Get cell data
    feed = client.GetCellsFeed(spreadsheet, worksheet)

    directory = Directory()
    for entry in feed.entry:
        # Only pull data from the 'Name' column ('A' column)
        if entry.title.text[0] == 'A':
            person = entry.content.text.strip()
            directory.add(person)


if __name__ == "__main__":
    main()