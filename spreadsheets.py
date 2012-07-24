#! /usr/bin/env python

import gdata.spreadsheet.service
import logging
import myUser

user = myUser.User()

client = gdata.spreadsheet.service.SpreadsheetsService()
client.ClientLogin(user.email, user.ticket)

# Spreadsheets
feed = client.GetSpreadsheetsFeed()
id_parts = feed.entry[0].id.text.split('/')
spreadsheet = id_parts[len(id_parts) - 1]

# Worksheets within the Spreadsheet
feed = client.GetWorksheetsFeed(spreadsheet)
id_parts = feed.entry[0].id.text.split('/')
worksheet = id_parts[len(id_parts) - 1]

# Get cell data

# This works, but has a lot of pieces to parse through
#feed = client.GetCellsFeed(spreadsheet, worksheet)
#logging.info(feed)

# This breaks when coming across an empty row
feed = client.GetListFeed(spreadsheet, worksheet)
logging.info(feed)