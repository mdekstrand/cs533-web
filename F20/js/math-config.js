window.MathJax = {
    tex: {
      inlineMath: [["\\(", "\\)"]],
      displayMath: [["\\[", "\\]"]],
      processEscapes: true,
      processEnvironments: true,
      macros: {
        E: "\\mathrm{E}",
        F: "\\mathcal{F}",
        P: "P",
        Cov: "\\mathrm{Cov}",
        Var: "\\mathrm{Var}",
        log: "\\operatorname{log}",
        Odds: "\\operatorname{Odds}",
        OR: "\\operatorname{OR}",
        IND: "\\mathbb{I}",
        Reals: "\\mathbb{R}"
      }
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    }
  };
