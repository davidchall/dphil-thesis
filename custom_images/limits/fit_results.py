#!/usr/bin/env python

from array import array
from collections import OrderedDict

import ROOT as r
r.gROOT.SetBatch(1);
r.gStyle.SetOptStat(0);

all_energies = ['7', '8', '7+8']
energy_colors = {'7': r.kGreen+2, '8': r.kRed, '7+8': r.kBlue}
energy_labels = {'7': '7 TeV', '8': '8 TeV', '7+8': 'Combined'}


class FitResult(object):
	def __init__(self, energy, z, mu_nom, mu_hi, mu_lo):
		self.energy = energy
		self.z = z
		self.mu_nom = mu_nom
		self.mu_hi = mu_hi
		self.mu_lo = mu_lo

		assert energy in all_energies

	def _get_graph(self):
		graph = r.TGraphAsymmErrors()
		graph.SetLineColor(energy_colors[self.energy])
		graph.SetMarkerColor(energy_colors[self.energy])
		graph.SetLineWidth(3)
		return graph

	def draw_z(self, y):
		if not self.z:
			return

		self.graph_z = self._get_graph()
		self.graph_z.SetPoint(0, 0.0, y)
		self.graph_z.SetPointError(0, 0.0, self.z, 0.0, 0.0)
		self.graph_z.Draw('PZ SAME')

	def draw_mu(self, y):
		if not self.mu_nom:
			return

		self.graph_mu = self._get_graph()
		self.graph_mu.SetMarkerStyle(34)
		self.graph_mu.SetPoint(0, self.mu_nom, y)
		self.graph_mu.SetPointError(0, abs(self.mu_lo), self.mu_hi, 0.0, 0.0)
		self.graph_mu.Draw('PZ SAME')


class FitGroup(object):
	def __init__(self, name, level, a, b, c):
		self.name = name
		self.level = level
		self.results = {}
		self.results[a.energy] = a
		self.results[b.energy] = b
		self.results[c.energy] = c

		self.energy_dy = 1.7
		self.name_dy = -1.5

		assert set(self.results.keys()) == set(all_energies)

	def _draw_z(self, y):
		self.results['7']  .draw_z(y + self.energy_dy)
		self.results['8']  .draw_z(y)
		self.results['7+8'].draw_z(y - self.energy_dy)

	def _draw_mu(self, y):
		self.results['7']  .draw_mu(y + self.energy_dy)
		self.results['8']  .draw_mu(y)
		self.results['7+8'].draw_mu(y - self.energy_dy)

	def draw(self, y, canvas, pad_z, pad_mu):
		pad_z.cd()
		self._draw_z(y)
		pad_mu.cd()
		self._draw_mu(y)
		canvas.cd()
		y_ndc = (y + self.name_dy - pad_z.GetY1()) / (pad_z.GetY2() - pad_z.GetY1())
		self.tex = r.TLatex(0.02, y_ndc, '   '*self.level+self.name)
		self.tex.SetNDC()
		self.tex.SetTextFont(43)
		self.tex.SetTextSize(18)
		self.tex.Draw()


DF = '#it{#scale[0.9]{e}#mu}/#it{#mu#scale[0.9]{e}}'
SF = '#it{#scale[0.9]{ee}}/#it{#mu#mu}'

results = []
results.append( FitGroup('Total', 0,
	FitResult('7',   0.56, 0.38, +0.70, -0.70),      # TODO
	FitResult('8',   4.12, 1.26, +0.41, -0.35),    # TODO
	FitResult('7+8', 6.07, 1.10, +0.23, -0.21)) )
results.append( FitGroup('0-jet', 1,
	FitResult('7',   0.56, 0.38, +0.70, -0.70),      # TODO
	FitResult('8',   4.12, 1.26, +0.41, -0.35),
	FitResult('7+8', 3.80, 1.15, +0.29, -0.26)) )   # TODO
results.append( FitGroup(DF, 2,
	FitResult('7',   0.40, 0.29, +0.70, -0.70),      # TODO
	FitResult('8',   4.36, 1.39, +0.45, -0.37),
	FitResult('7+8', 3.80, 1.15, +0.29, -0.26)) )   # TODO
results.append( FitGroup(SF, 2,
	FitResult('7',   0.54, 0.81, +0.70, -0.70),      # TODO
	FitResult('8',   0.42, 0.33, +0.74, -0.76),
	FitResult('7+8', 3.80, 1.15, +0.29, -0.26)) )   # TODO
results.append( FitGroup('1-jet', 1,
	FitResult('7',   1.43, 1.58, +0.70, -0.70),      # TODO
	FitResult('8',   2.41, 0.97, +0.54, -0.42),
	FitResult('7+8', 3.80, 1.15, +0.29, -0.26)) )   # TODO
results.append( FitGroup(DF, 2,
	FitResult('7',   1.60, 1.96, +0.70, -0.70),      # TODO
	FitResult('8',   2.70, 1.17, +0.56, -0.48),
	FitResult('7+8', 3.80, 1.15, +0.29, -0.26)) )   # TODO
results.append( FitGroup(SF, 2,
	FitResult('7',   0.05, 0.03, +0.70, -0.70),      # TODO
	FitResult('8',   0.25, 0.24, +1.21, -1.07),
	FitResult('7+8', 3.80, 1.15, +0.29, -0.26)) )   # TODO
results.append( FitGroup('#geq2-jet (ggF)', 1,
	FitResult('7',   None, None, None, None),
	FitResult('8',   1.49, 1.25, +1.01, -0.85),
	FitResult('7+8', None, None, None, None)) )
results.append( FitGroup('#geq2-jet (VBF)', 1,
	FitResult('7',   0.56, 0.38, +0.70, -0.70),      # TODO
	FitResult('8',   3.68, 1.59, +0.65, -0.54),
	FitResult('7+8', 3.80, 1.15, +0.29, -0.26)) )   # TODO
results.append( FitGroup(DF, 2,
	FitResult('7',   0.56, 0.38, +0.70, -0.70),      # TODO
	FitResult('8',   2.78, 1.27, +0.67, -0.54),
	FitResult('7+8', 3.80, 1.15, +0.29, -0.26)) )   # TODO
results.append( FitGroup(SF, 2,
	FitResult('7',   0.56, 0.38, +0.70, -0.70),      # TODO
	FitResult('8',   2.96, 2.60, +1.34, -1.07),
	FitResult('7+8', 3.80, 1.15, +0.29, -0.26)) )   # TODO



if __name__ == '__main__':
	canvas = r.TCanvas('canvas', 'canvas', 600, 500)
	canvas.Range(0.0, 0.0, 1.0, 1.0)
	x_start, x_split = 0.2, 0.5
	y_min, y_max = 0.0, 100.0
	frame_width = 3


	# Significance pad
	pad_z  = r.TPad('z', 'z', x_start, 0.0, x_split, 1.0)
	pad_z.SetTickx()
	pad_z.SetMargin(0.05, 0.03, 0.1, 0.08)
	pad_z.SetFrameLineWidth(frame_width)
	pad_z.Draw()
	pad_z.cd()
	frame_z = pad_z.DrawFrame(0.0, y_min, 6.99, y_max)
	frame_z.SetLabelFont(43)
	frame_z.SetLabelSize(14)
	frame_z.SetTitleFont(43)
	frame_z.SetTitleSize(14)
	frame_z.GetYaxis().SetTickLength(0)
	frame_z.GetXaxis().SetTickLength(0.02)
	frame_z.GetYaxis().SetLabelSize(0)
	frame_z.GetXaxis().SetTitle('Significance (#it{Z}_{obs})')
	frame_z.GetXaxis().SetTitleOffset(1.2)
	frame_z.Draw()
	line_3sig = r.TLine(3.0, y_min, 3.0, y_max)
	line_3sig.SetLineStyle(3)
	line_3sig.Draw()
	line_5sig = r.TLine(5.0, y_min, 5.0, y_max)
	line_5sig.SetLineStyle(3)
	line_5sig.Draw()
	canvas.cd()


	# Signal strength pad
	pad_mu = r.TPad('mu', 'mu', 1.0 - x_split, 0.0, 1.0, 1.0)
	pad_mu.SetTickx()
	pad_mu.SetMargin(0.03, 0.05, 0.1, 0.08)
	pad_mu.SetFrameLineWidth(frame_width)
	pad_mu.Draw()
	pad_mu.cd()
	frame_mu = pad_mu.DrawFrame(-1.0, y_min, +3.0, y_max)
	frame_mu.SetLabelFont(43)
	frame_mu.SetLabelSize(14)
	frame_mu.SetTitleFont(43)
	frame_mu.SetTitleSize(14)
	frame_mu.GetYaxis().SetTickLength(0)
	frame_mu.GetXaxis().SetTickLength(0.02)
	frame_mu.GetYaxis().SetLabelSize(0)
	frame_mu.GetXaxis().SetTitle('Signal strength (#mu)')
	frame_mu.GetXaxis().SetTitleOffset(1.2)
	frame_mu.Draw()
	line_mu_nom = r.TLine(1.0, y_min, 1.0, y_max)
	line_mu_nom.SetLineStyle(1)
	line_mu_nom.Draw()
	line_mu_hi = r.TLine(1.3, y_min, 1.3, y_max)
	line_mu_hi.SetLineStyle(3)
	line_mu_hi.Draw()
	line_mu_lo = r.TLine(0.7, y_min, 0.7, y_max)
	line_mu_lo.SetLineStyle(3)
	line_mu_lo.Draw()
	line_mu_zero = r.TLine(0.0, y_min, 0.0, y_max)
	line_mu_zero.SetLineStyle(1)
	line_mu_zero.Draw()
	canvas.cd()


	# Draw results
	for i, category in enumerate(results):
		y = y_max - ((i+0.5) * y_max/len(results))
		category.draw(y, canvas, pad_z, pad_mu)

	# Draw horizontal separating lines
	line_indices = [0, 3, 6, 7]
	separation_lines = []
	for index in line_indices:
		y = y_max - ((index+1.0) * y_max/len(results))
		
		pad_z.cd()
		line = r.TLine(frame_z.GetXaxis().GetXmin(), y, frame_z.GetXaxis().GetXmax(), y)
		line.SetLineWidth(frame_width)
		line.Draw()
		separation_lines.append(line)

		pad_mu.cd()
		line = r.TLine(frame_mu.GetXaxis().GetXmin(), y, frame_mu.GetXaxis().GetXmax(), y)
		line.SetLineWidth(frame_width)
		line.Draw()
		separation_lines.append(line)
		

	# Labels
	canvas.cd()
	label = r.TLatex()
	label.SetTextFont(43)
	label.SetTextSize(20)
	label.DrawLatexNDC(0.25, 0.95, 'm_{H} = 125 GeV')
	for i, energy in enumerate(all_energies):
		label.SetTextColor(energy_colors[energy])
		label.DrawLatexNDC(0.55 + 0.13*i, 0.95, energy_labels[energy])




	pad_z .RedrawAxis()
	pad_mu.RedrawAxis()
	canvas.SaveAs('z_and_mu.pdf')
