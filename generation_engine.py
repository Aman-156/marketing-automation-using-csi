# generation_engine.py
import os
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

def create_portfolio_pdf(client_name: str, services: list[str]) -> str:
    """
    Generates a PDF portfolio from a template.

    Args:
        client_name: The name of the client.
        services: A list of services to include in the report.

    Returns:
        The file path of the generated PDF.
    """
    # Set up Jinja2 to load templates from the 'templates' folder
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('template.html')

    # Render the HTML template with the provided data
    html_out = template.render(client_name=client_name, services=services)

    # Create an output folder if it doesn't exist
    output_dir = "portfolios"
    os.makedirs(output_dir, exist_ok=True)
    
    # Define the output PDF filename
    pdf_filename = f"{client_name.replace(' ', '_').lower()}_portfolio.pdf"
    pdf_filepath = os.path.join(output_dir, pdf_filename)

    # Generate the PDF using WeasyPrint
    # We need to provide the path to the css file as a base_url
    css_path = os.path.join('templates', 'style.css')
    HTML(string=html_out, base_url=os.path.dirname(os.path.abspath(css_path))).write_pdf(pdf_filepath)
    
    print(f"📄 PDF successfully generated at: {pdf_filepath}")
    return pdf_filepath

# Example of how to run this function directly for testing
if __name__ == '__main__':
    sample_client = "Example Corp"
    sample_services = ["Web Design", "SEO Optimization", "Content Marketing"]
    create_portfolio_pdf(sample_client, sample_services)