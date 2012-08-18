#! /usr/bin/env python

import email
import logging

from google.appengine.api import mail
from google.appengine.ext import webapp 
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from google.appengine.ext.webapp.util import run_wsgi_app
from lib.directory import Directory
from models.drive import Drive

class ReceiveMail(InboundMailHandler):
    """
    """

    def receive(self, message):
        """Event that is fired upon receiving an email

        """
        names = self._parse_for_names(message)
        directory = self._load_directory()

    def _load_directory(self):
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
        

    def _parse_for_names(self, message):
        """Parse an email's body for the names of people

        """
        htmltext = message.bodies('text/html')
        result = []

        for content_type, body in htmltext:
            decoded = body.decode()
            # Obtain index of tag with this label
            start = decoded.find("Obituary-Deceased Name")

            while start > 0:
                # index of closing-tag
                index = decoded.find('>', start) + 1
                # index of next opening-tag
                end = decoded.find('<', start)
                
                # Grab the person's name
                item = decoded[index:end]
                result.append(item)
                
                # Reset start pointer to look through rest of email
                start = decoded.find("Obituary-Deceased Name", end)

        return result


    def _ping(self, message):
        """Sends an email
        """
        message_ping = mail.EmailMessage(
                sender="Arbiter <arbiter@mitsuo62matsumoto.appspotmail.com>",
                subject="Notification")

        message_ping.to = "Reclaimer <matsumoto.fambam@gmail.com>"
        message_ping.body = """
Reclaimer,

This is a notification of receiving a message.

-- Arbiter
"""

        message_ping.send()

application = webapp.WSGIApplication([
    ReceiveMail.mapping()
], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()