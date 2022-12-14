from re import L
from fpdf import FPDF
import pandas as pd
from pyparsing import And


data = pd.read_csv('emma.csv', encoding="utf8")
data.loc[:, "Reach"] = data["Reach"].round(-3).map('{:,d}'.format)
data["State"] = data["State"].fillna(-1)
state_placements = []
national_placements = []
international_placements = []

for i in data["State"]:
    if i != -1:
        print(i)

# print(data)
count = 0
for i in data["State"]: 
    if data['Country'][count] != "United States":
        international_placements.append({"date": data['Alternate Date Format'][count], "source": data["Source"][count],  "url": data["URL"][count], "country": data["Country"][count], "reach": data["Reach"][count]})
    if data['Country'][count] == "United States" and i != -1:
        national_placements.append({"date": data['Alternate Date Format'][count], "source": data["Source"][count], "url": data["URL"][count], "state": data["State"][count], "reach": data["Reach"][count]})
    if i == "Missouri": 
        state_placements.append({"date": data['Alternate Date Format'][count], "source": data["Source"][count], "url": data["URL"][count], "city": data["City"][count], "reach": data["Reach"][count]})
    # if data['Country'][count] == "United States": 
    #     print(data["State"][count])
    # print(data["State"][count])
    count += 1
# print(state_placements)

# Instantiation of inherited class
pdf = FPDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)
pdf.cell(0, 10, 'Aug. 26, 2022', 0, 1)
pdf.set_font('Times', 'B', 12)
pdf.cell(0, 10, 'News Release: ', 0, 10)
pdf.set_font('Times', 'U', 12)
pdf.set_text_color(r = 0, g = 0, b = 255 )
pdf.cell(0, txt = 'Therapy dogs aren’t always the answer to help children with autism', link = 'https://showme.missouri.edu/2022/therapy-dogs-arent-always-the-answer-to-help-children-with-autism/')
pdf.cell(0,10, '', 0, 1)
pdf.set_font('Times', 'B', 12)
pdf.set_text_color(r = 0, g = 0, b = 0 )
pdf.cell(0, 10, "State Placements", 0, 1)
pdf.set_font('Times', '', 12)
for i in state_placements:
    pdf.cell(0, 10, f'{i["date"]} {i["source"]} ({i["reach"]} potential reach)' , 0, 1)
pdf.set_font('Times', 'B', 12)
pdf.cell(0, 10, "State Radio Placements", 0, 1)
pdf.set_font('Times', '', 12)
# for i in range(1, 41):
#     pdf.cell(0, 10, '8-3-22 Branson Tri-Lakes News (49,000 potential reach, Hollister, MO) ' + str(i), 0, 1)
pdf.set_font('Times', 'B', 12)
pdf.cell(0, 10, "National Placements", 0, 1)
pdf.set_font('Times', '', 12)
for i in national_placements:
    pdf.cell(0, 10, f'{i["date"]} {i["source"]} ({i["reach"]} potential reach) ', 0, 1)
pdf.set_font('Times', 'B', 12)
pdf.cell(0, 10, "International Placements", 0, 1)
pdf.set_font('Times', '', 12)
for i in international_placements:
    pdf.cell(0, 10, f'{i["date"]} {i["source"]} ({i["reach"]} potential reach, {i["country"]}) ', 0, 1)

placements = len(international_placements) + len(national_placements) + len(state_placements)

pdf.cell(0, 10, f'Totals: {placements} placements, {placements} potential reach')

pdf.output('tuto.pdf', 'F')