#!/usr/bin/env python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(sender="john@doe.com",recipients="jane@doe.com",subject="default"
                                                                      "subject"):

    sender = sender
    #recipients = ['ana.forero@carvajal.com']
    recipients = recipients
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
    html = """\

    <!DOCTYPE html>
    <html>
    <head>
    <style>
    table {
        border-collapse: collapse;
        width: 100%;
    }

    th, td {
        text-align: left;
        padding: 8px;
    }

    tr:nth-child(even){background-color: #f2f2f2}

    th {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    </head>
    <body>

    <h2>Un archivo ha sido cargado en el SFTP</h2>

    <table>
      <tr>
        <th>El archivo de corresponsal ha sido cargado</th>
       <th>SUCCESS!!!</th>

      </tr>


    </table>

    </body>
    </html>


    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(html, 'html')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('localhost')
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(me, recipients, msg.as_string())
    s.quit()
