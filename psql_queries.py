import psycopg2
import psycopg2.extras

try:
    conn = psycopg2.connect("dbname='health321' user='postgres' host='localhost' password='postgres'")
except:
    print "I am unable to connect to the database"


def get_invoices(TODAY):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
         cur.execute("""select * from account_invoice where  invoice_date = %(today)s""",{"today":TODAY})
    except:
        print "I can't SELECT from health321"
    dict_result = []
    for row in cur:
        dict_result.append(dict(row))
    return dict_result
#invoice = RawQuery(AccountInvoice,'select * from account_invoice where  invoice_date = {}'.format(TODAY))
#account_invoice : key:id : party, number,
#account_invoice_line : link-account_invoice-: id and get number


def get_invoice_lines(invoice_num):
    lines = RawQuery(AccountInvoiceLine,"select * from account_invoice_line as il where il.invoice = '32'")
    return lines

def get_invoice_tax(invoice_num):
    taxes = RawQuery(AccountInvoiceTax,"select * from account_invoice_tax as il where il.invoice = '32'")
    return taxes

if __name__ == '__main__':
    a=get_invoices('2018-04-16')
    print(a)
