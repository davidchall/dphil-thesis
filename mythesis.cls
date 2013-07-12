\ProvidesClass{mythesis}

% Pass options to hepthesis class, but ensure sftitles enabled
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{hepthesis}}
\ProcessOptions\relax
\LoadClass[sftitles]{hepthesis}

\RequirePackage{graphicx}
\RequirePackage[italic]{hepnicenames}
\RequirePackage{hepunits}
