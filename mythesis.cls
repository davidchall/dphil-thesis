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

\setspacing{double}