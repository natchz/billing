import pdfkit
from jinja2 import Environment, FileSystemLoader, Template, meta


def loader(temp_name):
    path_wkthmltopdf = r'/home/german/templates/wkhtmltox/bin/wkhtmltopdf'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(temp_name)
    template_source = env.loader.get_source(env, temp_name)[0]
    parsed_content = env.parse(template_source)
    variables = meta.find_undeclared_variables(parsed_content)
    data = "HOLA HOLA"
    temp_st = template.render(data=data, qr_image="qr/img.png")
#    pdfkit.from_file(temp_st, 'out1_flsk.pdf')
    print("ahora desde string")
    pdfkit.from_string(temp_st, 'out2_flsk.pdf',configuration=config)

if __name__ == "__main__":
    loader("invoice1.html")

