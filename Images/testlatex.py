import pylatex
import numpy as np
import os
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, StandAloneGraphic
from pylatex import Document, PageStyle, Head, MiniPage, Foot, LargeText, \
    MediumText, LineBreak, simple_page_number
from pylatex.utils import italic, bold, NoEscape

import matplotlib as mlt
import matplotlib.pyplot as plt
import re
import requests

def generate_header():
    geometry_options = {"margin": "0.7in"}
    doc = Document(geometry_options=geometry_options)
    # Add document header
    header = PageStyle("header")
    # Create left header
    with header.create(Head("L")):
        header.append("__")
        header.append(LineBreak())
        header.append("_")
    # Create center header
    with header.create(Head("C")):
        header.append("____")
    # Create right header
    with header.create(Head("R")):
        header.append(simple_page_number())
    # Create left footer
    with header.create(Foot("L")):
        header.append("Left Footer")
    # Create center footer
    with header.create(Foot("C")):
        header.append("Center Footer")
    # Create right footer
    with header.create(Foot("R")):
        header.append("Right Footer")

    doc.preamble.append(header)
    doc.change_document_style("header")

    # Add Heading
    with doc.create(MiniPage(align='l')):
        doc.append(LargeText(bold("INVESTMENT PROPERTY - BUY & HOLD")))
        doc.append(LineBreak())
        doc.append(MediumText(bold(" ")))
    doc.generate_pdf("header", clean_tex=False)

    return print('nice')

generate_header()



def details():
    if __name__ == '__main__':


        image_filename = os.path.join(os.path.dirname(__file__), 'kitten.jpg')
        logo_file = os.path.join(os.path.dirname(__file__),'sample-logo.png')

        geometry_options = {"tmargin": "1cm", "lmargin": "3cm"}
        doc = Document(geometry_options=geometry_options)
        header = PageStyle("header")
        with header.create(Head("R")):
            header.append(simple_page_number())
        with header.create(Foot("C")):
            header.append("Center Footer")
        first_page = PageStyle("firstpage")
        with first_page.create(Head("L")) as header_left:
        with header_left.create(MiniPage(width=NoEscape(r"0.49\textwidth"),pos='c')) as logo_wrapper

        with doc.create(MiniPage(align='l')):
            doc.append(LargeText(bold("INVESTMENT PROPERTY - BUY & HOLD")))
            doc.append(LineBreak())
            doc.append(MediumText(bold(" ")))
        logo_wrapper.append(StandAloneGraphic(image_options="width=120px",
                                              filename=logo_file))
        with doc.create(Section('Home Adress')):
            doc.append('Some regular text and some')
            doc.append(italic('italic text. '))
            doc.append('\nAlso some crazy characters: $&#{}')
            with doc.create(Subsection('Math that is incorrect')):
                doc.append(Math(data=['2*3', '=', 9]))

            with doc.create(Subsection('Table of something')):
                with doc.create(Tabular('rc|cl')) as table:
                    table.add_hline()
                    table.add_row((1, 2, 3, 4))
                    table.add_hline(1, 2)
                    table.add_empty_row()
                    table.add_row((4, 5, 6, 7))

        a = np.array([[100, 10, 20]]).T
        M = np.matrix([[2, 3, 4],
                       [0, 0, 1],
                       [0, 0, 2]])

        with doc.create(Section('The fancy stuff')):
            with doc.create(Subsection('Correct matrix equations')):
                doc.append(Math(data=[Matrix(M), Matrix(a), '=', Matrix(M * a)]))

            with doc.create(Subsection('Alignat math environment')):
                with doc.create(Alignat(numbering=False, escape=False)) as agn:
                    agn.append(r'\frac{a}{b} &= 0 \\')
                    agn.extend([Matrix(M), Matrix(a), '&=', Matrix(M * a)])

            with doc.create(Subsection('Beautiful graphs')):
                with doc.create(TikZ()):
                    plot_options = 'height=4cm, width=6cm, grid=major'
                    with doc.create(Axis(options=plot_options)) as plot:
                        plot.append(Plot(name='model', func='-x^5 - 242'))

                        coordinates = [
                            (-4.77778, 2027.60977),
                            (-3.55556, 347.84069),
                            (-2.33333, 22.58953),
                            (-1.11111, -493.50066),
                            (0.11111, 46.66082),
                            (1.33333, -205.56286),
                            (2.55556, -341.40638),
                            (3.77778, -1169.24780),
                            (5.00000, -3269.56775),
                        ]

                        plot.append(Plot(name='estimate', coordinates=coordinates))

            with doc.create(Subsection('Cute kitten pictures')):
                with doc.create(Figure(position='h!')) as kitten_pic:
                    kitten_pic.add_image(image_filename, width='120px')
                    kitten_pic.add_caption('Look it\'s on its back')

        doc.generate_pdf('full', clean_tex=False)
    return print("good")

details()