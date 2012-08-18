import logging

import gdata.docs.service

import my_user

user = my_user.User()

client = gdata.docs.service.DocsService()
client.ClientLogin(user.email, user.ticket)

documents_feed = client.GetDocumentListFeed()

for document_entry in documents_feed.entry:
    logging.info("Document: %s" % document_entry.title.text)