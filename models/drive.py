#! /usr/bin/env python

import logging

import gdata.spreadsheet.service
from lib.my_user import User


class Drive:
    """
    """

    def __init__(self):
        """
        """
        
        self._user = User()
        self._client = gdata.spreadsheet.service.SpreadsheetsService()

        self._client.ClientLogin(self._user.email, self._user.ticket)

    def list_spreadsheets(self):
        """
        """
        result = []
        feed = self._client.GetSpreadsheetsFeed()
        
        return self._feed_content(feed)

    def list_worksheets(self, spreadsheet):
        """
        """
        index = -1

        spreadsheets_feed = self._client.GetSpreadsheetsFeed()
        equalized_string = self._equalize_string(spreadsheet)
        for element in self._feed_content(spreadsheets_feed):
            ++index

            # Found the requested spreadsheet
            if equalized_string == self._equalize_string(element):
                # Grab the ID
                id_parts = spreadsheets_feed.entry[index].id.text.split('/')
                id_ = id_parts[len(id_parts) - 1]

                worksheets_feed = self._client.GetWorksheetsFeed(id_)
                
                return self._feed_content(worksheets_feed)

        return []

    def _equalize_array(self, string_array):
        """
        """
        result = []

        for element in string_array:
            result.append(self._equalize_string(element))

        return result

    def _equalize_string(self, string):
        """
        """
        return string.lower().replace(' ', '')

    def _feed_content(self, feed):
        """
        """
        result = []
        
        for item in feed.entry:
            result.append(item.content.text)
        
        return result