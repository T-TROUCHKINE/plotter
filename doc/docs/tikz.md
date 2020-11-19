---
layout: page
title: Tikz exporting
permalink: /tikz/
---
# Tikz exporting
It is possible to export the figure as a Tikz code for using it in a `.tex` file
using the `export_tikz()` method of the `Plotter` class.

### Example
```python
from plotter import Plotter, PlotterType

to_plot = [
    {
        "type": PlotterType.MULTITRACE,
        "data": [[4,5,8,6,4,5,6,5,2,3,6,4,8,4,5,7,5,4,2,3,1,5,5],
                 [8,4,6,6,9,5,6,5,2,4,5,6,4,8,8,7,9,6,3,1,2,3,6,5,8,4,6,5,5]],
    }
]

pl = Plotter(to_plot)
pl.export_tikz()
```

### Result
{% raw %}
```tex
% This file was created by tikzplotlib v0.8.5.
\begin{tikzpicture}

\definecolor{color0}{rgb}{0.12156862745098,0.466666666666667,0.705882352941177}
\definecolor{color1}{rgb}{1,0.498039215686275,0.0549019607843137}

\begin{axis}[
tick align=outside,
tick pos=left,
x grid style={white!69.01960784313725!black},
xmin=-1.4, xmax=29.4,
xtick style={color=black},
y grid style={white!69.01960784313725!black},
ymin=0.6, ymax=9.4,
ytick style={color=black}
]
\addplot [semithick, color0]
table {\%
0 4
1 5
2 8
3 6
4 4
5 5
6 6
7 5
8 2
9 3
10 6
11 4
12 8
13 4
14 5
15 7
16 5
17 4
18 2
19 3
20 1
21 5
22 5
};
\addplot [semithick, color1]
table {%
0 8
1 4
2 6
3 6
4 9
5 5
6 6
7 5
8 2
9 4
10 5
11 6
12 4
13 8
14 8
15 7
16 9
17 6
18 3
19 1
20 2
21 3
22 6
23 5
24 8
25 4
26 6
27 5
28 5
};
\end{axis}

\end{tikzpicture}
```
{% endraw %}

[{% fa_svg fas.fa-download %} Download file]({{site.baseurl}}/assets/tex/tikz_fig.tex){: .btn}

## Tex file importing the figure
```tex
\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{pgfplots}
\DeclareUnicodeCharacter{2212}{−}
\usepgfplotslibrary{groupplots,dateplot}
\usetikzlibrary{patterns,shapes.arrows}
\pgfplotsset{compat=newest}

\begin{document}

\input{tikz_fig}

\end{document}
```

[{% fa_svg fas.fa-download %} Download file]({{site.baseurl}}/assets/tex/doc.tex){: .btn}
{% fa_svg_generate %}

## Compiling the figure
`pdflatex doc.tex`

### Result
<object data="{{site.baseurl}}/assets/pdf/doc.pdf" width="725" height="950" type='application/pdf'></object>

## Adding a legend
In some cases, in particular in the `bar` plots, the legend is not set in the
Tikz file. It can be added using the following code.

```tex
\addlegendimage{legend image with text=\tikz{\draw[color0, fill=color0] (0,0) rectangle (0.05,0.05);}}
\addlegendentry{Legend 1}
\addlegendimage{legend image with text=\tikz{\draw[color1, fill=color1] (0,0) rectangle (0.05,0.05);}}
\addlegendentry{Legend 2}
```
