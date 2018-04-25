# -*- coding: utf-8 -*-


This project starts on main.py, the business flow is:
1. Get all invoices for current day
2. Convert these invoices to xml and then sign them.
3. Create a zip files with these xml and send it using ws
4. Create the pdf with QR code, data , and send to customer using sendmail server
5. Finishing the process for ebilling.


Sign with certificate:
1. Using java seems to be working fine, just keep the CA value and you can
use it on many customer if they approved, like any other Proveedor Tecnologico.


FTP: specification:
1. Seems that there's a way to simple use ftp to deliver,
maybe you can consider this option.Additional

WS specification:
1. First ws for get the number of invoices
2. Second ws for send the zip file on base64 format
3. Additional steps are:
    3.1 Generate QR for invoice
    3.2 Generate PDF with inv and QR inside
    3.3 Send this to customer using job over mail server

TODO:
1. I need to revert all the queries using sql, so I can change Backend invoiceplane
for other engine or backnend. Like Tryton by instance.
    1.1 Create a sql module where you put all sql que
    1.2 Keep using ORM, it's easy to read
