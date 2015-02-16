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
\RequirePackage{rotating}
\RequirePackage{bigdelim}
\RequirePackage{tabularx}
\RequirePackage{listliketab}
\RequirePackage{dcolumn}
\RequirePackage{cancel}
\RequirePackage{mathtools}
\RequirePackage{chapterbib}


% Latin
\DeclareRobustCommand{\eg}{\textit{e.g.\ }}
\DeclareRobustCommand{\ie}{\textit{i.e.\ }}
\DeclareRobustCommand{\cf}{\textit{c.f.\ }}

% Line spacing
\setfrontmatterspacing{onehalf}
\setmainmatterspacing{onehalf}
\setappendixspacing{onehalf}
\setbackmatterspacing{onehalf}


% Fix hyperref labels in PDFTeX
\@ifpackageloaded{hyperref}{%
	\pdfstringdefDisableCommands{%
		\def\pp{pp }%
		\def\WW{WW }%
		\def\HWW{HWW }%
		\def\Wjets{W+jets }%
		\def\DY{Z/gamma* }%
		\def\ggH{ggH }%
		\def\Wgamma{Wgamma }%
		\def\Wgstar{Wgamma* }%
	}%
}{}

% tabularx centred column
\newcolumntype{Y}{>{\centering\arraybackslash}X}
\newcolumntype{Z}{>{\raggedleft\arraybackslash}X}
% dcolumn aligns decimal places
\newcolumntype{d}[1]{D{.}{.}{#1}}

% Make bibliography a section rather than a chapter (for Springer)
\makeatletter
\renewenvironment{thebibliography}[1]
     {\section*{\bibname}% <-- this line was changed from \chapter* to \section*
      %\@mkboth{\MakeUppercase\bibname}{\MakeUppercase\bibname}%
      \list{\@biblabel{\@arabic\c@enumiv}}%
           {\settowidth\labelwidth{\@biblabel{#1}}%
            \leftmargin\labelwidth
            \advance\leftmargin\labelsep
            \@openbib@code
            \usecounter{enumiv}%
            \let\p@enumiv\@empty
            \renewcommand\theenumiv{\@arabic\c@enumiv}}%
      \sloppy
      \clubpenalty4000
      \@clubpenalty \clubpenalty
      \widowpenalty4000%
      \sfcode`\.\@m}
     {\def\@noitemerr
       {\@latex@warning{Empty `thebibliography' environment}}%
      \endlist}
\makeatother
