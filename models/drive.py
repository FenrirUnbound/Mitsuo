#! /usr/bin/env python

import logging

import gdata.spreadsheet.service
from lib.my_user import User


class Drive:

    def __init__(self):
        self._user = User()
        self._client = gdata.spreadsheet.service.SpreadsheetsService()

        self._client.ClientLogin(self._user.email, self._user.ticket)
    
    @property
    def spreadsheets(self):
        result = []
        feed = self._client.GetSpreadsheetsFeed()
        
        for item in feed.entry:
            result.append(item.content.text)
        
        return result