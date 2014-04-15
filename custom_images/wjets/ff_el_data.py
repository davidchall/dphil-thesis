#!/usr/bin/env python

import ROOT as r

minX, maxX  = 10., 100.
minY, maxY  = 0.0, 0.01
zjet_color  = r.kBlue
dijet_color = r.kRed
wjet_color  = r.kGreen+3

c1 = r.TCanvas('c1', 'canvas', 600, 400)
c1.SetMargin(0.13, 0.03, 0.15, 0.03)
frame = c1.DrawFrame(minX, minY, maxX, maxY)
frame.SetLabelFont(43, "xy");
frame.SetLabelSize(18, "xy");
frame.SetTitleFont(43, "xy");
frame.SetTitleSize(18, "xy");
frame.GetYaxis().SetDecimals()
frame.GetXaxis().SetTitle('Electron #it{p}_{T} [GeV]')
frame.GetXaxis().SetTitleOffset(1.2)
frame.GetYaxis().SetTitle('Fake factor')
frame.GetYaxis().SetTitleOffset(1.3)
frame.GetYaxis().SetNdivisions(5,5,0)

data_zjet = [
	[12.5,  2.5, 8.067E-03, 0.205*8.067E-03],
	[17.5,  2.5, 6.523E-03, 0.390*6.523E-03],
	[22.5,  2.5, 5.303E-03, 0.577*5.303E-03],
	[62.5, 37.5, 7.051E-03, 0.375*7.051E-03],
]

data_dijet = [
	[12.5,  2.5, 7.133E-03, 0.0347*7.133E-03],
	[17.5,  2.5, 8.555E-03, 0.0535*8.555E-03],
	[22.5,  2.5, 7.539E-03, 0.0434*7.539E-03],
	[62.5, 37.5, 4.897E-03, 0.0553*4.897E-03],
]


gr_data_zjet  = r.TGraphErrors()
gr_data_dijet = r.TGraphErrors()


for i, datum in enumerate(data_zjet):
	gr_data_zjet.SetPoint     (i, datum[0], datum[2])
	gr_data_zjet.SetPointError(i, datum[1], datum[3])
for i, datum in enumerate(data_dijet):
	gr_data_dijet.SetPoint     (i, datum[0], datum[2])
	gr_data_dijet.SetPointError(i, datum[1], datum[3])


# Set styles
gr_data_zjet .SetMarkerColor(zjet_color)
gr_data_zjet .SetLineColor  (zjet_color)
gr_data_dijet.SetMarkerColor(dijet_color)
gr_data_dijet.SetLineColor  (dijet_color)

gr_data_zjet .SetMarkerStyle(20)
gr_data_dijet.SetMarkerStyle(20)

gr_data_dijet.Draw('p same')
gr_data_zjet.Draw('p same')

# legend
legend = r.TLegend(0.8, 0.8, 0.96, 0.96)
legend.AddEntry(gr_data_dijet, 'dijet',    'p')
legend.AddEntry(gr_data_zjet,  'Z+jet',    'p')
legend.SetFillColor(0);
legend.SetBorderSize(0);
legend.SetTextFont(43)
legend.SetTextSize(18);
legend.Draw('same')


c1.RedrawAxis()
c1.SaveAs('ff_el_data.pdf')
