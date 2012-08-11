#! /usr/bin/env python

import logging

import gdata.spreadsheet.service
from lib.my_user import User


class Drive:

    def __init__(self):
        self.__user = User()
        self.__client = gdata.spreadsheet.service.SpreadsheetsService()

        self.__client.ClientLogin(self.__user.email, self.__user.ticket)

    def spreadsheets(self):
        result = []
        feed = self.__client.GetSpreadsheetsFeed()
        
        for item in feed.entry:
            result.append(item.content.text)
        
        return result

    def worksheets(self, spreadsheet):
        spreadsheets_feed = self.spreadsheets()
        index = -1

        spreadsheets_feed = self.__equalize_array(spreadsheets_feed)
        for element in spreadsheets_feed:
            ++index
            element = self.__equalize_string(element)

            if self.__equalize_string(spreadsheet) == element:
                worksheets_feed = 

    def __equalize_array(self, string_array):
        result = []

        for element in string_array:
            result.append(self.__equalize_string(element))

        return result

    def __equalize_string(self, string):
        return string.lower().replace(' ', '')