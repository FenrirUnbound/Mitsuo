#! /usr/bin/env python

import logging, email
from google.appengine.api import mail
from google.appengine.ext import webapp 
from google.appengine.ext.webapp.mail_handlers import InboundMailHandler 
from google.appengine.ext.webapp.util import run_wsgi_app

class ReceiveMail(InboundMailHandler):
	def receive(self, message):
		htmltext = message.bodies('text/html')
		names = []	# list of names accumulated

		for content_type, body in htmltext:
			decoded = body.decode()	#url-decoded email message
			start = decoded.find("Obituary-Deceased Name")	# index of tag with this label
			
			while start > 0:
				# index of closing tag
				index = decoded.find(">", start) + 1
				# index of next opening tag
				end = decoded.find("<", start)
				
				# Grab the person's name
				item = decoded[index:end]
				names.append(item)

				# Reset start pointer to look through rest of email
				start = decoded.find("Obituary-Deceased Name", end)

		for item in names:
			logging.info("Name: %s" % item)


	def ping(self, message):
		message_ping = mail.EmailMessage(sender="Arbiter <arbiter@mitsuo62matsumoto.appspotmail.com>",
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