(TeX-add-style-hook
 "actividad2"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "spanish" "12pt" "letterpaper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("babel" "spanish") ("inputenc" "utf8")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art12"
    "babel"
    "inputenc"
    "authblk"
    "listings"
    "dsfont"
    "lscape"
    "multirow")
   (LaTeX-add-labels
    "tabla:sencilla"))
 :latex)

