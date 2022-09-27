(TeX-add-style-hook
 "NTNUoving"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("geometry" "margin=3cm")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "babel"
    "graphicx"
    "amssymb"
    "amsmath"
    "amsfonts"
    "lastpage"
    "geometry")
   (TeX-add-symbols
    '("thanks" 1)
    '("author" 1)
    '("ovingnr" 1)
    '("oving" 1)
    '("fag" 1)
    '("semester" 1)
    '("oppgaveoverskrift" 1)
    '("ovingstekst" 1)
    '("institutt" 1)
    "Punktkolon"
    "PunktInn"
    "NTNULogo"
    "thesemester"
    "logofil"
    "addto"
    "PageText"
    "NTNUa"
    "LANGINFO"
    "NTNUi"
    "OVING"
    "thefootnote"
    "maketitle"
    "sectionmark"
    "subsectionmark"
    "version"
    "innerfoot"
    "centerfoot"
    "outerfoot"
    "innerhead"
    "centerhead"
    "outerhead")
   (LaTeX-add-environments
    '("oppgave" LaTeX-env-args ["argument"] 0)
    "punkt")
   (LaTeX-add-pagestyles
    "titlepage"
    "tech")
   (LaTeX-add-counters
    "Oppg"
    "Punkt"))
 :latex)

