from xml.sax.saxutils import prepare_input_source

import pdfkit
from jinja2 import Environment, FileSystemLoader, Template, meta

def loader(invoice,invoice_party,invoice_lines,issuer,cufe):

    temp_name = "invoice.html"
    #path_wkthmltopdf = r'/usr/bin/wkthmltopdf'
    #config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    env = Environment(loader=FileSystemLoader(r'/home/german/TYR_project/billing/utils/templates'))
    template = env.get_template(temp_name)
    template_source = env.loader.get_source(env, temp_name)[0]
    parsed_content = env.parse(template_source)
    variables = meta.find_undeclared_variables(parsed_content)
    temp_st = template.render(invoice=invoice,party=invoice_party,
                              lines=invoice_lines,
                              issuer=issuer,logo=r"/home/german/TYR_project/billing/logo.png",
                              qr_image=r'/home/german/TYR_project/billing/utils/qr/{}.png'.format(cufe))
    pdfkit.from_string(temp_st, '{}.pdf'.format(invoice["number"]))
    #,configuration=config
    #pdfkit.from_file(temp_st, 'out1_flsk.pdf')



