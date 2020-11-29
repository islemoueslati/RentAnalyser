import pylatex
import numpy as np
import os
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat, StandAloneGraphic, Tabularx, MultiColumn, TextColor, Tabu, LongTabu, NewPage, \
    SubFigure, Itemize, Command, MultiRow
from pylatex import Document, PageStyle, Head, MiniPage, Foot, LargeText, \
    MediumText, LineBreak, simple_page_number
from pylatex.utils import italic, bold, NoEscape

import matplotlib as mlt
import matplotlib.pyplot as plt
import re
import requests


def generate_unique():
    geometry_options = {
        "head": "40pt",
        "margin": "0.5in",
        "bottom": "0.6in",
        "includeheadfoot": True
    }
    doc = Document(geometry_options=geometry_options)

    # Generating first page style
    first_page = PageStyle("firstpage")
    # Header image
    with first_page.create(Head("C")) as header_center:
        with header_center.create(MiniPage(width=NoEscape(r"0.50\textwidth"),
                                           pos='c')) as logo_wrapper:
            logo_file = os.path.join(os.path.dirname(__file__),
                                     'sample-logo.png')
            logo_wrapper.append(StandAloneGraphic(image_options="width=300px",
                                                  filename=logo_file))

    # Add document title
    # Add footer
    with first_page.create(Foot("C")) as footer:
        message = "Important message please read"
        with footer.create(Tabularx(
                "X X X X",
                width_argument=NoEscape(r"\textwidth"))) as footer_table:
            branch_address = MiniPage(
                width=NoEscape(r"0.25\textwidth"),
                pos='t')

            document_details = MiniPage(width=NoEscape(r"0.25\textwidth"),
                                        pos='t', align='r')
            document_details.append(LineBreak())
            document_details.append(simple_page_number())

            footer_table.add_row([branch_address, branch_address,
                                  branch_address, document_details])

    doc.preamble.append(first_page)
    # End first page style

    # Add customer information
    with doc.create(Tabu("X[l] X[r]")) as first_page_table:
        customer = MiniPage(width=NoEscape(r"0.49\textwidth"), pos='h')

        # Add branch information
        branch = MiniPage(width=NoEscape(r"0.49\textwidth"), pos='t!',
                          align='r')

        first_page_table.add_row([customer, branch])
        first_page_table.add_empty_row()

    doc.change_document_style("firstpage")
    doc.add_color(name="lightgray", model="gray", description="0.80")
    print("Enter the Region")
    R = input(str)

    with doc.create(MiniPage(align='c')):
        doc.append(LargeText(bold("\n\n\n\n\n\n" + R)))
        doc.append(LineBreak())
    print("Enter the adress of home ")
    A = input(str)
    image_filename = os.path.join(os.path.dirname(__file__), 'home.jpg')
    with doc.create(Section('Example : ' + A)):
        with doc.create(Figure(position='h!')) as home_pic:
            home_pic.add_image(image_filename, width='490px')
    with doc.create(Section('Property information :')):
        with doc.create(Itemize()) as itemize:
            print("enter property type")
            x = input(str)
            itemize.add_item(bold("Property type : " + x))
            print("How many bedrooms ?")
            y = input(int)
            itemize.add_item(bold("Bedroom : " + y))
            print("How many bathrooms?")
            z = input(float)
            itemize.add_item(bold("Bathroom : " + z))
            print('Enter the year of built please:')
            a = input(int)
            itemize.add_item(bold("Year built : " + a))
            print('Enter the finished sqft :')
            b = input(int)
            itemize.add_item(bold("Finished sqft : " + b))
            print("Enter the estimate price")
            p1 = input(float)
            print('enter the estimate rent')
            p2 = input(float)
            doc.append(LineBreak())
            table1 = Tabular('|c|c|')
            table1.add_hline()
            table1.add_row(('Estimate price', 'Estimate rent'))
            table1.add_hline()
            table1.add_row((p1 + '$', p2 + '$'))
            table1.add_hline()

        doc.append(table1)
    with doc.create(Section('Financing')):
        with doc.create(Itemize()) as itemize:
            print('Enter type of loan')
            lo = input(str)
            itemize.add_item(bold("Loan Type: " + lo))
            print("Enter loan amount")
            la = input(float)
            itemize.add_item(bold("Loan Amount: " + la))
            print("enter the interest rate with %")
            IR = input(float)
            itemize.add_item(bold("Interest Rate: " + IR + "%"))
            print("enter LTV")
            LTV = input(float)
            itemize.add_item(bold("Loan to Value (LTV): " + LTV + "%"))
            print("enter loan term")
            LT = input(int)
            itemize.add_item(bold("Loan Term: " + LT + "years"))
            print("enter loan payment monthly")
            LPM = input(int)
            print("enter loan payment yearly")
            LPY = input(int)
            itemize.add_item(bold("Loan Payment: " + LPM + "(monthly), " + LPY + "(yearly)"))

    with doc.create(Section('Assumptions')):
        with doc.create(Itemize()) as itemize:
            print("enter vacancy rate")
            vr = input(float)
            itemize.add_item(bold('Vacancy Rate' + vr))
            print("property managment")
            pr = input(float)
            itemize.add_item(bold('Property Managment' + pr))
            print("yearly expense")
            yex = input(float)
            itemize.add_item(bold('Yearly Expense incr' + yex))
            print("yearly rent")
            yr = input(float)
            itemize.add_item(bold('Yearly Rent incr' + yr))
            print("yearly equity")
            ye = input(float)
            itemize.add_item(bold('Yearly Equity incr' + ye))
            print("land value")
            lv = input(float)
            itemize.add_item(bold('Land Value' + lv))

        section = Section('Financial projection and expences analysis')
        test1 = Subsection(bold('Financial Projection'))
        test2 = Subsection(bold('Expences'))

        table2 = Tabular('|c|c|c|c|c|c|c|c|c|c|')
        table2.add_hline()
        table2.add_row(("Type", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5", "Year 10", "Year 15", "Year 20", "Year 30"))
        table2.add_hline()
        table2.add_row(("Total Annuel Income", 6, 7, 8, 8, 8, 8, 8, 8, 8))
        table2.add_hline()
        table2.add_row(("Total Annuel Expenses", 6, 7, 8, 8, 8, 8, 8, 8, 8))
        table2.add_hline()
        table2.add_row(("Total Annuel Operating Expenses", 6, 7, 8, 8, 8, 8, 8, 8, 8))
        table2.add_hline()
        table2.add_row(("Total Annual Cash Flow", 6, 7, 8, 8, 8, 8, 8, 8, 8))
        table2.add_hline()
        table2.add_row(("Property Value", 6, 7, 8, 8, 8, 8, 8, 8, 8))
        table2.add_hline()
        table2.add_row(("Cash on Cash ROI", 6, 7, 8, 8, 8, 8, 8, 8, 8))
        table2.add_hline()
        table2.add_row(("Loan Balance", 6, 7, 8, 8, 8, 8, 8, 8, 8))
        table2.add_hline()
        table2.add_row(("Cumulative Cash Flow", 6, 7, 8, 8, 8, 8, 8, 8, 8))
        table2.add_hline()
        table2.add_row(("Equity", 6, 7, 8, 8, 8, 8, 8, 8, 8))
        table2.add_hline()



        table3 = Tabular('|c|c|c|')
        table3.add_hline()
        table3.add_row(("   ", "Monthly", "Annually"))
        table3.add_hline()
        table3.add_row(("Repair Cost", 6, 7))
        table3.add_hline()
        table3.add_row(("Vacancy", 6, 7))
        table3.add_hline()
        table3.add_row(("Insurance", 6, 7))
        table3.add_hline()
        table3.add_row(("Taxes", 6, 7))
        table3.add_hline()
        table3.add_row(("hoe", 6, 7))
        table3.add_hline()
        table3.add_row(("Capital Expenditures", 6, 7))
        table3.add_hline()
        table3.add_row(("Property Managment", 6, 7))
        table3.add_hline()
        table3.add_row(("Other Expences", 6, 7))
        table3.add_hline()
        table3.add_row((LargeText(bold("Total")), 6, 7))
        table3.add_hline()

        test1.append(table2)
        test2.append(table3)
        section.append(test1)
        section.append(test2)
        doc.append(section)
        doc.append(LineBreak)
        print('Cap Rate')
        cap = input()
        print('Cash on Cash Return')
        cac = input()
        print('Retur on investment')
        roi = input()

    doc.append(LargeText(bold('Cap Rate :'+cap+'\n\n'+"Cash on Cash Return"+cac+"\n\n"+"Return on Investment"+roi)))
    doc.generate_pdf("complex_report", clean_tex=False)


generate_unique()
