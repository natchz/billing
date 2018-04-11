# -*- coding: utf-8 -*-
This project starts on main.py, the business flow is:
1. Get all invoices for current day
2. Convert these invoices to xml and then sign them.
3. Create a zip files with these xml and send it using ws

WS specification:
1. First ws for get the number of invoices
2. Second ws for send the zip file on base64 format
3. Additional steps are:
    3.1 Generate QR for invoice
    3.2 Generate PDF with inv and QR inside
    3.3 Send this to customer using job over mail server

TODO:
1. I need to revert all the queries using sql, so I can changes front invoice for other engine or backnend.
    1.1 Create a sql module where you put all sql que
