(TeX-add-style-hook
 "main"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("NTNUoving" "11pt" "a4paper" "norsk")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("fontenc" "T1")))
   (TeX-run-style-hooks
    "latex2e"
    "NTNUoving"
    "NTNUoving11"
    "inputenc"
    "fontenc"
    "mathrsfs")
   (TeX-add-symbols
    '("RomanNumeralCaps" 1)))
 :latex)

