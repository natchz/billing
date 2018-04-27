SELECT
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