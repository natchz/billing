from fetch_invoices import psql_invoices
from webservice import ws_send_invoice
from datetime import datetime
from os import listdir
from utils import qr_generator,pdf_generator

#Define paths and global variables
TODAY = datetime.today().date()
INVOICE_FILES = format('invoices/{}/'.format(TODAY))
DEBIT_FILES = format('debit_notes/{}/'.format(TODAY))
CREDIT_FILES = format('credit_notes/{}/'.format(TODAY))

#--for invoices
#get_invoices()
psql_invoices()
for zip_file in listdir(INVOICE_FILES):
    if zip_file.endswith(".zip"):
        ws_send_invoice(INVOICE_FILES+zip_file)

"""
#--for debit notes
#get_debit_notes()
for zip_file in listdir(DEBIT_FILES):
    if zip_file.endswith(".zip"):
        ws_send_invoice(DEBIT_FILES+zip_file)
#--for credit notes
#get_credit_notes()
for zip_file in listdir(CREDIT_FILES):
    if zip_file.endswith(".zip"):
        ws_send_invoice(CREDIT_FILES+zip_file)
"""
