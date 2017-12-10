import pdfkit
from jinja2 import Environment, FileSystemLoader, Template, meta


def loader(invoice,client,items,amounts,issuer):
    temp_name = "invoice.html"
    path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    env = Environment(loader=FileSystemLoader(r'C:\Users\german\PycharmProjects\billing\utils\templates'))
    print(items)
    template = env.get_template(temp_name)
    template_source = env.loader.get_source(env, temp_name)[0]
    parsed_content = env.parse(template_source)
    variables = meta.find_undeclared_variables(parsed_content)
    temp_st = template.render(invoice=invoice,client=client,items=items,amounts=amounts[0], issuer=issuer) #qr_image='imagen')
    pdfkit.from_string(temp_st, '{}.pdf'.format(invoice.invoice),configuration=config)
    #pdfkit.from_file(temp_st, 'out1_flsk.pdf')



