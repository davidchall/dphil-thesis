\ProvidesClass{mythesis}

% Pass options to hepthesis class, but ensure sftitles enabled
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{hepthesis}}
\ProcessOptions\relax
\LoadClass[sftitles, oneside]{hepthesis}

\RequirePackage{graphicx}
\usepackage[italic]{hepparticles}
\RequirePackage[italic]{hepnames}
\RequirePackage{hepunits}
\RequirePackage{thesismath}
\RequirePackage{thesisphysics}
\RequirePackage{cite}
\RequirePackage[utf8]{inputenc}
\RequirePackage{subcaption}
\RequirePackage{amssymb}
\RequirePackage{multirow}
\RequirePackage{enumitem}

\DeclareRobustCommand{\eg}{\textit{e.g.\ }}
\DeclareRobustCommand{\ie}{\textit{i.e.\ }}
\DeclareRobustCommand{\cf}{\textit{c.f.\ }}

% Line spacing
\setfrontmatterspacing{double}
\setmainmatterspacing{double}
\setappendixspacing{double}
\setbackmatterspacing{onehalf}


% Fix hyperref labels in PDFTeX
\@ifpackageloaded{hyperref}{%
	\pdfstringdefDisableCommands{%
		\def\pi{pi}%
		\def\gamma{gamma}%
		\def\WW{WW}%
		\def\HWW{HWW}%
		\def\Wjets{W+jets}%
		\def\Zjets{Z+jets}%
		\def\ggH{ggH}%
	}%
}{}
