from peewee import *

#python -m pwiz -e mysql -u root invoice > model.py

database = MySQLDatabase('invoice', **{'user': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class IpClientCustom(BaseModel):
    client_custom_fieldid = IntegerField()
    client_custom_fieldvalue = TextField(null=True)
    client_custom = PrimaryKeyField(db_column='client_custom_id')
    client = IntegerField(db_column='client_id')

    class Meta:
        db_table = 'ip_client_custom'
        indexes = (
            (('client', 'client_custom_fieldid'), True),
        )

class IpClientNotes(BaseModel):
    client = IntegerField(db_column='client_id')
    client_note = TextField()
    client_note_date = DateField()
    client_note_id = PrimaryKeyField()

    class Meta:
        db_table = 'ip_client_notes'
        indexes = (
            (('client', 'client_note_date'), False),
        )

class IpClients(BaseModel):
    client_active = IntegerField(index=True)
    client_address_1 = TextField(null=True)
    client_address_2 = TextField(null=True)
    client_avs = CharField(null=True)
    client_birthdate = DateField(null=True)
    client_city = TextField(null=True)
    client_country = TextField(null=True)
    client_date_created = DateTimeField()
    client_date_modified = DateTimeField()
    client_email = TextField(null=True)
    client_fax = TextField(null=True)
    client_gender = IntegerField(null=True)
    client = PrimaryKeyField(db_column='client_id')
    client_insurednumber = CharField(null=True)
    client_language = CharField(null=True)
    client_mobile = TextField(null=True)
    client_name = TextField(null=True)
    client_phone = TextField(null=True)
    client_state = TextField(null=True)
    client_surname = CharField(null=True)
    client_tax_code = TextField(null=True)
    client_vat = TextField(db_column='client_vat_id', null=True)
    client_veka = CharField(null=True)
    client_web = TextField(null=True)
    client_zip = TextField(null=True)

    class Meta:
        db_table = 'ip_clients'

class IpCustomFields(BaseModel):
    custom_field = PrimaryKeyField(db_column='custom_field_id')
    custom_field_label = CharField(null=True)
    custom_field_location = IntegerField(null=True)
    custom_field_order = IntegerField(null=True)
    custom_field_table = CharField(index=True, null=True)
    custom_field_type = CharField()

    class Meta:
        db_table = 'ip_custom_fields'
        indexes = (
            (('custom_field_table', 'custom_field_label'), True),
        )

class IpCustomValues(BaseModel):
    custom_values_field = IntegerField()
    custom_values = PrimaryKeyField(db_column='custom_values_id')
    custom_values_value = TextField()

    class Meta:
        db_table = 'ip_custom_values'

class IpEmailTemplates(BaseModel):
    email_template_bcc = TextField(null=True)
    email_template_body = TextField()
    email_template_cc = TextField(null=True)
    email_template_from_email = TextField(null=True)
    email_template_from_name = TextField(null=True)
    email_template = PrimaryKeyField(db_column='email_template_id')
    email_template_pdf_template = CharField(null=True)
    email_template_subject = TextField(null=True)
    email_template_title = TextField(null=True)
    email_template_type = CharField(null=True)

    class Meta:
        db_table = 'ip_email_templates'

class IpFamilies(BaseModel):
    family = PrimaryKeyField(db_column='family_id')
    family_name = TextField(null=True)

    class Meta:
        db_table = 'ip_families'

class IpImportDetails(BaseModel):
    import_detail = PrimaryKeyField(db_column='import_detail_id')
    import_ = IntegerField(db_column='import_id')
    import_lang_key = CharField()
    import_record = IntegerField(db_column='import_record_id')
    import_table_name = CharField()

    class Meta:
        db_table = 'ip_import_details'
        indexes = (
            (('import_', 'import_record'), False),
        )

class IpImports(BaseModel):
    import_date = DateTimeField()
    import_ = PrimaryKeyField(db_column='import_id')

    class Meta:
        db_table = 'ip_imports'

class IpInvoiceAmounts(BaseModel):
    invoice_amount = PrimaryKeyField(db_column='invoice_amount_id')
    invoice_balance = DecimalField(null=True)
    invoice = IntegerField(db_column='invoice_id', index=True)
    invoice_item_subtotal = DecimalField(null=True)
    invoice_item_tax_total = DecimalField(null=True)
    invoice_paid = DecimalField(null=True)
    invoice_sign = CharField()
    invoice_tax_total = DecimalField(null=True)
    invoice_total = DecimalField(null=True)

    class Meta:
        db_table = 'ip_invoice_amounts'
        indexes = (
            (('invoice_paid', 'invoice_balance'), False),
        )

class IpInvoiceCustom(BaseModel):
    invoice_custom_fieldid = IntegerField()
    invoice_custom_fieldvalue = TextField(null=True)
    invoice_custom = PrimaryKeyField(db_column='invoice_custom_id')
    invoice = IntegerField(db_column='invoice_id')

    class Meta:
        db_table = 'ip_invoice_custom'
        indexes = (
            (('invoice', 'invoice_custom_fieldid'), True),
        )

class IpInvoiceGroups(BaseModel):
    invoice_group = PrimaryKeyField(db_column='invoice_group_id')
    invoice_group_identifier_format = CharField()
    invoice_group_left_pad = IntegerField(index=True)
    invoice_group_name = TextField(null=True)
    invoice_group_next = IntegerField(db_column='invoice_group_next_id', index=True)

    class Meta:
        db_table = 'ip_invoice_groups'

class IpInvoiceItemAmounts(BaseModel):
    item_amount = PrimaryKeyField(db_column='item_amount_id')
    item_discount = DecimalField(null=True)
    item = IntegerField(db_column='item_id', index=True)
    item_subtotal = DecimalField(null=True)
    item_tax_total = DecimalField(null=True)
    item_total = DecimalField(null=True)

    class Meta:
        db_table = 'ip_invoice_item_amounts'

class IpInvoiceItems(BaseModel):
    invoice = IntegerField(db_column='invoice_id')
    item_date = DateField(null=True)
    item_date_added = DateField()
    item_description = TextField(null=True)
    item_discount_amount = DecimalField(null=True)
    item = PrimaryKeyField(db_column='item_id')
    item_is_recurring = IntegerField(null=True)
    item_name = TextField(null=True)
    item_order = IntegerField()
    item_price = DecimalField(null=True)
    item_product = IntegerField(db_column='item_product_id', null=True)
    item_product_unit = CharField(null=True)
    item_product_unit_id = IntegerField(null=True)
    item_quantity = DecimalField()
    item_task = IntegerField(db_column='item_task_id', null=True)
    item_tax_rate = IntegerField(db_column='item_tax_rate_id')

    class Meta:
        db_table = 'ip_invoice_items'
        indexes = (
            (('invoice', 'item_tax_rate', 'item_date_added', 'item_order'), False),
        )

class IpInvoiceSumex(BaseModel):
    sumex_casedate = DateField()
    sumex_casenumber = CharField(null=True)
    sumex_diagnosis = CharField()
    sumex = PrimaryKeyField(db_column='sumex_id')
    sumex_invoice = IntegerField()
    sumex_observations = CharField()
    sumex_reason = IntegerField()
    sumex_treatmentend = DateField()
    sumex_treatmentstart = DateField()

    class Meta:
        db_table = 'ip_invoice_sumex'

class IpInvoiceTaxRates(BaseModel):
    include_item_tax = IntegerField()
    invoice = IntegerField(db_column='invoice_id')
    invoice_tax_rate_amount = DecimalField()
    invoice_tax_rate = PrimaryKeyField(db_column='invoice_tax_rate_id')
    tax_rate = IntegerField(db_column='tax_rate_id')

    class Meta:
        db_table = 'ip_invoice_tax_rates'
        indexes = (
            (('invoice', 'tax_rate'), False),
        )

class IpInvoices(BaseModel):
    client = IntegerField(db_column='client_id')
    creditinvoice_parent = IntegerField(db_column='creditinvoice_parent_id', null=True)
    invoice_date_created = DateField()
    invoice_date_due = DateField()
    invoice_date_modified = DateTimeField()
    invoice_discount_amount = DecimalField(null=True)
    invoice_discount_percent = DecimalField(null=True)
    invoice_group = IntegerField(db_column='invoice_group_id')
    invoice = PrimaryKeyField(db_column='invoice_id')
    invoice_number = CharField(null=True)
    invoice_password = CharField(null=True)
    invoice_status = IntegerField(db_column='invoice_status_id', index=True)
    invoice_terms = TextField()
    invoice_time_created = TimeField()
    invoice_url_key = CharField(unique=True)
    is_read_only = IntegerField(null=True)
    payment_method = IntegerField()
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'ip_invoices'
        indexes = (
            (('user', 'client', 'invoice_group', 'invoice_date_created', 'invoice_date_due', 'invoice_number'), False),
        )

class IpInvoicesRecurring(BaseModel):
    invoice = IntegerField(db_column='invoice_id', index=True)
    invoice_recurring = PrimaryKeyField(db_column='invoice_recurring_id')
    recur_end_date = DateField()
    recur_frequency = CharField()
    recur_next_date = DateField()
    recur_start_date = DateField()

    class Meta:
        db_table = 'ip_invoices_recurring'

class IpItemLookups(BaseModel):
    item_description = TextField()
    item_lookup = PrimaryKeyField(db_column='item_lookup_id')
    item_name = CharField()
    item_price = DecimalField()

    class Meta:
        db_table = 'ip_item_lookups'

class IpMerchantResponses(BaseModel):
    invoice = IntegerField(db_column='invoice_id', index=True)
    merchant_response = CharField()
    merchant_response_date = DateField(index=True)
    merchant_response_driver = CharField()
    merchant_response_id = PrimaryKeyField()
    merchant_response_reference = CharField()

    class Meta:
        db_table = 'ip_merchant_responses'

class IpPaymentCustom(BaseModel):
    payment_custom_fieldid = IntegerField()
    payment_custom_fieldvalue = TextField(null=True)
    payment_custom = PrimaryKeyField(db_column='payment_custom_id')
    payment = IntegerField(db_column='payment_id')

    class Meta:
        db_table = 'ip_payment_custom'
        indexes = (
            (('payment', 'payment_custom_fieldid'), True),
        )

class IpPaymentMethods(BaseModel):
    payment_method = PrimaryKeyField(db_column='payment_method_id')
    payment_method_name = TextField(null=True)

    class Meta:
        db_table = 'ip_payment_methods'

class IpPayments(BaseModel):
    invoice = IntegerField(db_column='invoice_id', index=True)
    payment_amount = DecimalField(index=True, null=True)
    payment_date = DateField()
    payment = PrimaryKeyField(db_column='payment_id')
    payment_method = IntegerField(db_column='payment_method_id', index=True)
    payment_note = TextField()

    class Meta:
        db_table = 'ip_payments'

class IpProducts(BaseModel):
    family = IntegerField(db_column='family_id', null=True)
    product_description = TextField()
    product = PrimaryKeyField(db_column='product_id')
    product_name = TextField(null=True)
    product_price = DecimalField(null=True)
    product_sku = TextField(null=True)
    product_tariff = IntegerField(null=True)
    provider_name = TextField(null=True)
    purchase_price = DecimalField(null=True)
    tax_rate = IntegerField(db_column='tax_rate_id', null=True)
    unit = IntegerField(db_column='unit_id', null=True)

    class Meta:
        db_table = 'ip_products'

class IpProjects(BaseModel):
    client = IntegerField(db_column='client_id')
    project = PrimaryKeyField(db_column='project_id')
    project_name = TextField(null=True)

    class Meta:
        db_table = 'ip_projects'

class IpQuoteAmounts(BaseModel):
    quote_amount = PrimaryKeyField(db_column='quote_amount_id')
    quote = IntegerField(db_column='quote_id', index=True)
    quote_item_subtotal = DecimalField(null=True)
    quote_item_tax_total = DecimalField(null=True)
    quote_tax_total = DecimalField(null=True)
    quote_total = DecimalField(null=True)

    class Meta:
        db_table = 'ip_quote_amounts'

class IpQuoteCustom(BaseModel):
    quote_custom_fieldid = IntegerField()
    quote_custom_fieldvalue = TextField(null=True)
    quote_custom = PrimaryKeyField(db_column='quote_custom_id')
    quote = IntegerField(db_column='quote_id')

    class Meta:
        db_table = 'ip_quote_custom'
        indexes = (
            (('quote', 'quote_custom_fieldid'), True),
        )

class IpQuoteItemAmounts(BaseModel):
    item_amount = PrimaryKeyField(db_column='item_amount_id')
    item_discount = DecimalField(null=True)
    item = IntegerField(db_column='item_id', index=True)
    item_subtotal = DecimalField(null=True)
    item_tax_total = DecimalField(null=True)
    item_total = DecimalField(null=True)

    class Meta:
        db_table = 'ip_quote_item_amounts'

class IpQuoteItems(BaseModel):
    item_date_added = DateField()
    item_description = TextField(null=True)
    item_discount_amount = DecimalField(null=True)
    item = PrimaryKeyField(db_column='item_id')
    item_name = TextField(null=True)
    item_order = IntegerField()
    item_price = DecimalField(null=True)
    item_product = IntegerField(db_column='item_product_id', null=True)
    item_product_unit = CharField(null=True)
    item_product_unit_id = IntegerField(null=True)
    item_quantity = DecimalField(null=True)
    item_tax_rate = IntegerField(db_column='item_tax_rate_id', index=True)
    quote = IntegerField(db_column='quote_id')

    class Meta:
        db_table = 'ip_quote_items'
        indexes = (
            (('quote', 'item_date_added', 'item_order'), False),
        )

class IpQuoteTaxRates(BaseModel):
    include_item_tax = IntegerField()
    quote = IntegerField(db_column='quote_id', index=True)
    quote_tax_rate_amount = DecimalField(null=True)
    quote_tax_rate = PrimaryKeyField(db_column='quote_tax_rate_id')
    tax_rate = IntegerField(db_column='tax_rate_id', index=True)

    class Meta:
        db_table = 'ip_quote_tax_rates'

class IpQuotes(BaseModel):
    client = IntegerField(db_column='client_id')
    invoice_group = IntegerField(db_column='invoice_group_id')
    invoice = IntegerField(db_column='invoice_id', index=True)
    notes = TextField(null=True)
    quote_date_created = DateField()
    quote_date_expires = DateField()
    quote_date_modified = DateTimeField()
    quote_discount_amount = DecimalField(null=True)
    quote_discount_percent = DecimalField(null=True)
    quote = PrimaryKeyField(db_column='quote_id')
    quote_number = CharField(null=True)
    quote_password = CharField(null=True)
    quote_status = IntegerField(db_column='quote_status_id', index=True)
    quote_url_key = CharField()
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'ip_quotes'
        indexes = (
            (('user', 'client', 'invoice_group', 'quote_date_created', 'quote_date_expires', 'quote_number'), False),
        )

class IpSessions(BaseModel):
    data = TextField()
    id = CharField()
    ip_address = CharField()
    timestamp = IntegerField(index=True)

    class Meta:
        db_table = 'ip_sessions'
        primary_key = False

class IpSettings(BaseModel):
    setting = PrimaryKeyField(db_column='setting_id')
    setting_key = CharField(index=True)
    setting_value = TextField()

    class Meta:
        db_table = 'ip_settings'

class IpTasks(BaseModel):
    project = IntegerField(db_column='project_id')
    task_description = TextField()
    task_finish_date = DateField()
    task = PrimaryKeyField(db_column='task_id')
    task_name = TextField(null=True)
    task_price = DecimalField(null=True)
    task_status = IntegerField()
    tax_rate = IntegerField(db_column='tax_rate_id')

    class Meta:
        db_table = 'ip_tasks'

class IpTaxRates(BaseModel):
    tax_rate = PrimaryKeyField(db_column='tax_rate_id')
    tax_rate_name = TextField(null=True)
    tax_rate_percent = DecimalField()

    class Meta:
        db_table = 'ip_tax_rates'

class IpUnits(BaseModel):
    unit = PrimaryKeyField(db_column='unit_id')
    unit_name = CharField(null=True)
    unit_name_plrl = CharField(null=True)

    class Meta:
        db_table = 'ip_units'

class IpUploads(BaseModel):
    client = IntegerField(db_column='client_id')
    file_name_new = TextField()
    file_name_original = TextField()
    upload = PrimaryKeyField(db_column='upload_id')
    uploaded_date = DateField()
    url_key = CharField()

    class Meta:
        db_table = 'ip_uploads'

class IpUserClients(BaseModel):
    client = IntegerField(db_column='client_id')
    user_client = PrimaryKeyField(db_column='user_client_id')
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'ip_user_clients'
        indexes = (
            (('user', 'client'), False),
        )

class IpUserCustom(BaseModel):
    user_custom_fieldid = IntegerField()
    user_custom_fieldvalue = TextField(null=True)
    user_custom = PrimaryKeyField(db_column='user_custom_id')
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'ip_user_custom'
        indexes = (
            (('user', 'user_custom_fieldid'), True),
        )

class IpUsers(BaseModel):
    user_active = IntegerField(null=True)
    user_address_1 = TextField(null=True)
    user_address_2 = TextField(null=True)
    user_all_clients = IntegerField()
    user_city = TextField(null=True)
    user_company = TextField(null=True)
    user_country = TextField(null=True)
    user_date_created = DateTimeField()
    user_date_modified = DateTimeField()
    user_email = TextField(null=True)
    user_fax = TextField(null=True)
    user_gln = BigIntegerField(null=True)
    user_iban = CharField(null=True)
    user = PrimaryKeyField(db_column='user_id')
    user_language = CharField(null=True)
    user_mobile = TextField(null=True)
    user_name = TextField(null=True)
    user_password = CharField()
    user_passwordreset_token = CharField(null=True)
    user_phone = TextField(null=True)
    user_psalt = TextField(null=True)
    user_rcc = CharField(null=True)
    user_state = TextField(null=True)
    user_subscribernumber = CharField(null=True)
    user_tax_code = TextField(null=True)
    user_type = IntegerField()
    user_vat = TextField(db_column='user_vat_id', null=True)
    user_web = TextField(null=True)
    user_zip = TextField(null=True)

    class Meta:
        db_table = 'ip_users'

class IpVersions(BaseModel):
    version_date_applied = CharField(index=True)
    version_file = CharField()
    version = PrimaryKeyField(db_column='version_id')
    version_sql_errors = IntegerField()

    class Meta:
        db_table = 'ip_versions'

