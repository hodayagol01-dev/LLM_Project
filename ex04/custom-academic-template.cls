\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{custom-academic-template}[2026/06/10 Custom Academic Template]

\LoadClass[12pt,a4paper]{article}

\RequirePackage{fontspec}
\RequirePackage{geometry}
\RequirePackage{hyperref}
\RequirePackage{graphicx}
\RequirePackage{booktabs}

\geometry{margin=1in}


\newcommand{\maketitlepage}{
    \begin{titlepage}
        \centering
        \vspace*{2cm}
        {\Huge\bfseries \@title \par}
        \vspace{1.5cm}
        {\Large \@author \par}
        \vspace{2cm}
        \vfill
        {\large \@date \par}
    \end{titlepage}
}
