SELECT  
ail.type, 
ail.quantity,
ail.unit,
ail.invoice,
pt.name,
ail.description, 
ail.create_date, 
ail.note, 
ail.product, 
ail.company, 
ail.origin,
ail.unit_price,
ail.write_date,
ail.invoice_type
FROM public.account_invoice_line ail
JOIN product_template pt on pt.id = ail.product
