#!/usr/bin/env python

import ROOT as r

minX, maxX  = 10., 100.
minY, maxY  = 0.0, 0.2
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
frame.GetXaxis().SetTitle('Muon #it{p}_{T} [GeV]')
frame.GetXaxis().SetTitleOffset(1.2)
frame.GetYaxis().SetTitle('Fake factor')
frame.GetYaxis().SetTitleOffset(1.1)
frame.GetYaxis().SetNdivisions(5,5,0)

data_zjet = [
	[12.5,  2.5, 1.052E-01, 0.1053*1.052E-01],
	[17.5,  2.5, 9.529E-02, 0.1861*9.529E-02],
	[22.5,  2.5, 8.639E-02, 0.2995*8.639E-02],
	[62.5, 37.5, 7.853E-02, 0.4005*7.853E-02],
]

data_dijet = [
	[12.5,  2.5, 1.455E-01, 0.0211*1.455E-01],
	[17.5,  2.5, 1.168E-01, 0.0187*1.168E-01],
	[22.5,  2.5, 1.084E-01, 0.0201*1.084E-01],
	[62.5, 37.5, 7.958E-02, 0.0494*7.958E-02],
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
c1.SaveAs('ff_mu_data.pdf')
