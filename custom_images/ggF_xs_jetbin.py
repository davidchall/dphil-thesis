#!/usr/bin/env python

import os, ROOT, array

ROOT.gROOT.SetBatch(1);
ROOT.gStyle.SetOptStat(0);


zero_err = [0.0, 0.0, 0.0]

# FO CI
foci_x    = [3, 13, 23]
foci_y    = [11.83, 5.15, 2.29]
foci_yerr = [ 2.13, 2.19, 1.60]

# FO JVE
fojve_x    = [5, 15, 25]
fojve_y    = [11.55, 4.75, 2.97]
fojve_yerr = [ 2.64, 1.64, 1.09]

# Res JVE
resjve_x    = [7, 17, 27]
resjve_y    = [11.81, 4.59, 2.87]
resjve_yerr = [ 1.66, 1.03, 0.73]

# Powheg
powheg_y      = [11.47, 5.43, 2.37]

# Powheg reweighted
powheg_rwgt_y = [12.33, 4.53, 2.41]



hist = ROOT.TH1D( "hist", "Cross Sections", 3, 0, 30 )

for i in xrange(hist.GetNbinsX() ):
    hist.GetXaxis().SetBinLabel(i+1, "")
    pass

hist.SetTitle("")
hist.GetXaxis().SetTicks("");
hist.GetXaxis().SetBinLabel( 1, "0-jet" )
hist.GetXaxis().SetBinLabel( 2, "1-jet" )
hist.GetXaxis().SetBinLabel( 3, "#geq2-jet" )
hist.SetMaximum(15)
hist.SetYTitle("Cross Section [pb]")
hist.GetXaxis().SetLabelSize(0.08)
hist.GetYaxis().SetLabelSize(0.04)
hist.GetYaxis().SetTitleSize(0.04)

foci = ROOT.TGraphErrors( len(foci_x), array.array('d', foci_x), array.array('d', foci_y), array.array('d', zero_err) , array.array('d', foci_yerr) )
foci.SetMarkerStyle(20)
foci.SetMarkerColor( ROOT.kRed )
foci.SetLineColor( ROOT.kRed )
foci.SetMarkerSize(1.2)

fojve = ROOT.TGraphErrors( len(fojve_x), array.array('d', fojve_x), array.array('d', fojve_y), array.array('d', zero_err) , array.array('d', fojve_yerr) )
fojve.SetMarkerStyle(21)
fojve.SetMarkerColor( ROOT.kGreen+3 )
fojve.SetLineColor( ROOT.kGreen+3 )
fojve.SetMarkerSize(1.2)

resjve = ROOT.TGraphErrors( len(resjve_x), array.array('d', resjve_x), array.array('d', resjve_y), array.array('d', zero_err) , array.array('d', resjve_yerr) )
resjve.SetMarkerStyle(22)
resjve.SetMarkerColor( ROOT.kBlue )
resjve.SetLineColor( ROOT.kBlue )
resjve.SetMarkerSize(1.2)

powheg = ROOT.TH1D( 'powheg', 'powheg', 3, 0, 30 )
for i in xrange(3):
	powheg.SetBinContent(i+1, powheg_y[i])
powheg.SetLineColor( ROOT.kBlack )

powheg_rwgt = ROOT.TH1D( 'powheg_rwgt', 'powheg_rwgt', 3, 0, 30 )
for i in xrange(3):
	powheg_rwgt.SetBinContent(i+1, powheg_rwgt_y[i])
powheg_rwgt.SetLineColor( ROOT.kBlack )
powheg_rwgt.SetLineStyle(2)


c1 = ROOT.TCanvas()
hist.Draw()
powheg_rwgt.Draw("SAME hist")
powheg.Draw("SAME hist")
foci.Draw("SAME p")
fojve.Draw("SAME p")
resjve.Draw("SAME p")


leg = ROOT.TLegend( 0.55, 0.65, 0.88, 0.88 )
leg.SetFillColor( ROOT.kWhite )
leg.SetLineColor( ROOT.kWhite )
leg.AddEntry( foci, "Fixed order CI", "ep" )
leg.AddEntry( fojve, "Fixed order JVE", "ep" )
leg.AddEntry( resjve, "Resummed JVE", "ep" )
leg.AddEntry( powheg, "Powheg", "l" )
leg.AddEntry( powheg_rwgt, "Powheg (reweight #it{p}_{T,#it{H}} )", "l" )


leg.Draw()
c1.Print("ggF_xs_jetbin.pdf")


        
