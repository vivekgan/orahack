from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
from pywebio.exceptions import SessionClosedException
import warnings
import argparse
from main import *

warnings.filterwarnings("ignore")

def main():
    put_markdown(
        '''
        # Conversion to OBIEE made easy
        '''
        , lstrip=True
    )
    tool = select("Choose your current analytics tool",options=['Power BI','Tableau'])
    put_text("Check how your "+tool+" report is going to look in OBIEE")
    f = file_upload("Choose your PDF to convert")
    open('assets/dashboard.pdf', 'wb').write(f['content'])
    put_info("Converting...")
    descriptions = get_images_descriptions(tool)
    images = []
    for i in range(len(descriptions)):
        images.append(open('assets/'+str(i)+'.jpg', 'rb').read())
    output = [[put_text("Chart in your dashboard"),put_text("Chart type in "+tool),put_text("Replacement in OBIEE")]]
    for i in range(len(images)):
        output.append([put_image(images[i], width='200px', height='100px'),put_text(descriptions[i]), put_text('map'+descriptions[i])])
    clear()
    put_markdown(
        '''
        # Conversion to OBIEE made easy
        '''
        , lstrip=True
    )
    put_text("You can download the OBIEE template here")
    # put_link()
    put_grid(output, cell_width='400px', cell_height='200px')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(main, port=args.port)
