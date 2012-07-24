#! /usr/bin/env python

import gdata.spreadsheet.service
import logging
import myUser

def main():
	user = myUser.User()

	client = gdata.spreadsheet.service.SpreadsheetsService()
	client.ClientLogin(user.email, user.ticket)

	# Spreadsheets
	feed = client.GetSpreadsheetsFeed()
	id_parts = feed.entry[0].id.text.split('/')
	spreadsheet = id_parts[len(id_parts) - 1]

	# Worksheets within the Spreadsheet
	wsFeed = client.GetWorksheetsFeed(spreadsheet)
	id_parts = wsFeed.entry[0].id.text.split('/')
	worksheet = id_parts[len(id_parts) - 1]

	# Get cell data
	maxRows = wsFeed.entry[0].row_count.text
	feed = client.GetCellsFeed(spreadsheet, worksheet)

	for entry in feed.entry:
		# Only pull data from the 'Name' column ('A' column)
		if entry.title.text[0] == 'A':
			logging.info(entry.content.text.strip()

if __name__ == "__main__":
	main()