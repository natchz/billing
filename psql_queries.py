import psycopg2
import psycopg2.extras


"""
Important keys

account_invoice:id --> account_invoice_line:number
account_invoice:party --> party_party:id

"""
# Create the connection to db
try:
    conn = psycopg2.connect("dbname='health321' user='postgres' host='localhost' password='postgres'")
except:
    print("I am unable to connect to the database")


def get_invoices(TODAY):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
         cur.execute("""SELECT
ac.id,
ac.type,
cc.code as currency,
ac.description,
ac.create_date,
ac.number,
ac.invoice_address,
ac.reference,
ac.tax_identifier,
ac.company,
ac.state,
ac.payment_term,
ac.comment,
ac.party,
ac.accounting_date
FROM account_invoice ac
JOIN currency_currency cc on cc.id = ac.currency
where  invoice_date = %(date)s""",{"date":TODAY})
    except:
        print("I can't SELECT get_invoices from health321")
    dict_result = []
    for row in cur:
        dict_result.append(dict(row))
    return dict_result

def get_invoice_lines(number):

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
         cur.execute("""SELECT
ail.type,
ail.quantity,
ail.unit,
ail.invoice,
pt.name,
ail.description,
ail.note,
ail.unit_price,
ail.invoice_type,
ait.description,
ait.amount,
ait.base,
ait.tax,
ait.tax_code
FROM public.account_invoice_line ail
JOIN product_template pt on pt.id = ail.product
JOIN account_invoice_line_account_tax aiat on aiat.line = ail.id
JOIN account_invoice_tax ait on ait.tax = aiat.tax
where  ail.invoice = %(invoice_id)s""",{"invoice_id":number})
    except:
        print("I can't SELECT invoices taxes from health321 for invoice id {}".format(number))
    dict_result = []
    for row in cur:
        dict_result.append(dict(row))
    return dict_result

def get_party(party_id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
         cur.execute("""SELECT
pp.name,
pp.lastname,
pp.ssn,
pp.ssn_number,
cs.name as subdivision,
cc.name as country,
du.desc as address -- use left join in case no du available
FROM party_party as pp
left join country_country cc on cc.id = pp.citizenship
left join country_subdivision cs on cs.id = pp.residence
left join gnuhealth_du du on du.id = pp.du
where pp.id = %(invoice_id)s""",{"invoice_id":party_id})
    except:
        print("I can't SELECT invoices lines from health321 for invoice id {}".format(party_id))
    dict_result = []
    for row in cur:
        dict_result.append(dict(row))
    return dict_result


'''
def get_invoice_taxes(invoice_id):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
         cur.execute("""SELECT
         id,
         base_sign,
         sequence,
         write_uid,
         write_date,
         amount,
         manual,
         description,
         invoice,
         create_date,
         base,
         tax,
         account,
         tax_sign,
         base_code,
         create_uid,
         tax_code
         FROM public.account_invoice_tax
         where invoice = %(invoice_id)s""",{"invoice_id":invoice_id})
    except:
        print("I can't SELECT invoices lines from health321 for invoice id {}".format(invoice_id))
    dict_result = []
    for row in cur:
        dict_result.append(dict(row))
    return dict_result
'''

def get_issuer(data):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
         cur.execute("""SELECT
         id,
         write_uid,
         header,
         parent,
         write_date,
         currency,
         create_date,
         timezone,
         party,
         create_uid,
         footer
         FROM public.company_company;
         """)
    except:
        print("I can't SELECT invoices lines from health321 for invoice id {}".format(invoice_id))
    dict_result = []
    for row in cur:
        dict_result.append(dict(row))
    return dict_result


if __name__ == '__main__':
    invoice = get_invoices('2018-04-27')
    invoice_lines = get_invoice_lines(invoice[0]["id"])
    invoice_party = get_party(invoice[0]["party"])