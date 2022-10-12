from re import L
from fpdf import FPDF
import pandas as pd
from pyparsing import And
pdf = FPDF()


def create_report(file, date, title, url, pdf_title):

    # function for displaying american placements in PDF report
    def american_placements():
        if "https://" in i["url"]:
            pdf.set_text_color(r = 0, g = 0, b = 255)
            pdf.set_font('Times', 'U', 12)
            pdf.cell(0, 10, txt = f'{str(i["date"])} {i["source"]} ({i["reach"]} potential reach)', link = f'{i["url"]}')
            pdf.cell(0, 10, '', 0, 1)
            pdf.set_text_color(r = 0, g = 0, b = 0 )
            pdf.set_font('Times', '', 12)
        else:
            pdf.cell(0, 10, f'{str(i["date"])} {i["source"]} ({i["reach"]} potential reach)', 0, 1 )

    # load csv file, alter data to make processing + displaying easier 
    data = pd.read_csv(file)
    data.loc[:, "Reach"] = data["Reach"].round(-3).map('{:,d}'.format)
    data["State"] = data["State"].fillna(-1)

    # creating spaces for placement seperation, var to hold total potential reach 
    state_placements = []
    national_placements = []
    international_placements = []
    reach = 0
    social_echo = 0

    # loop thru entire data set, seperate into international, national, state placements 
    # add each publications info (date, source, url, country, reach) to seperate buckets for later display
    # add each publications reach to the running total
    count = 0
    for i in data['State']: 
        if data['Country'][count] != "United States":
            international_placements.append({"date": data['Alternate Date Format'][count], "source": data["Source"][count],  "url": data["URL"][count], "country": data["Country"][count], "reach": data["Reach"][count]})
            reach += int(data["Reach"][count].replace(",", ""))
            social_echo += int(data["Twitter Social Echo"][count]) + int(data["Facebook Social Echo"][count]) + int(data["Reddit Social Echo"][count])
        if i != "Missouri" and i != -1:
            national_placements.append({"date": data['Alternate Date Format'][count], "source": data["Source"][count], "url": data["URL"][count], "state": data["State"][count], "reach": data["Reach"][count]})
            reach += int(data["Reach"][count].replace(",", ""))
            social_echo += int(data["Twitter Social Echo"][count]) + int(data["Facebook Social Echo"][count]) + int(data["Reddit Social Echo"][count])
        if i == "Missouri": 
            state_placements.append({"date": data['Alternate Date Format'][count], "source": data["Source"][count], "url": data["URL"][count], "city": data["City"][count], "reach": data["Reach"][count]})
            reach += int(data["Reach"][count].replace(",", ""))
            social_echo += int(data["Twitter Social Echo"][count]) + int(data["Facebook Social Echo"][count]) + int(data["Reddit Social Echo"][count])


        count += 1

        
    # creation of PDF report 
    pdf.alias_nb_pages()
    pdf.add_page()
    times_reg()
    pdf.cell(0, 10, f'{date}', 0, 1)
    times_bold()
    pdf.cell(0, 10, 'News Release: ', 0, 10)
    times_underline()
    blue()
    pdf.cell(0, txt = f'{title}', link = f'{url}')
    spacer()
    times_bold()
    black()
    pdf.cell(0, 10, "State Placements", 0, 1)
    times_reg()

    for i in state_placements:
        american_placements()

    times_bold()
    pdf.cell(0, 10, "State Radio Placements", 0, 1)
    times_reg()
    pdf.cell(0, 10, '8-3-22 Branson Tri-Lakes News (49,000 potential reach, Hollister, MO) ', 0, 1)
    times_bold()
    pdf.cell(0, 10, "National Placements", 0, 1)
    times_reg()

    for i in national_placements:
        american_placements()

    times_bold()
    pdf.cell(0, 10, "International Placements", 0, 1)
    times_reg()

    for i in international_placements:
        if "https://" in i["url"]:
            pdf.set_text_color(r = 0, g = 0, b = 255)
            pdf.set_font('Times', 'U', 12)
            pdf.cell(0, 10, txt = f'{str(i["date"])} {i["source"]} ({i["reach"]} potential reach, {i["country"]})', link = f'{i["url"]}')
            pdf.cell(0, 10, '', 0, 1)
            pdf.set_text_color(r = 0, g = 0, b = 0 )
            pdf.set_font('Times', '', 12)
        else:
            pdf.cell(0, 10, f'{str(i["date"])} {i["source"]} ({i["reach"]} potential reach, {i["country"]})', 0, 1 )

    # calculate total placements, add space, display totals, output PDF report 
    placements = len(state_placements) + len(national_placements) + len(international_placements)
    spacer()
    pdf.cell(0, 10, f'Totals: {placements} placements, {reach} potential reach, {social_echo} social media impressions')
    pdf.output(f'{pdf_title}.pdf', 'F')


# functions to make styling document simpler
def times_reg():
    pdf.set_font('Times', '', 12)

def times_bold():
    pdf.set_font('Times', 'B', 12)

def times_underline():
    pdf.set_font('Times', 'U', 12)

def blue():
    pdf.set_text_color(r = 0, g = 0, b = 255 )

def black():
    pdf.set_text_color(r = 0, g = 0, b = 0 )

def spacer():
    pdf.cell(0,10, '', 0, 1)
