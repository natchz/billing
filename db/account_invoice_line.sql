SELECT  
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

