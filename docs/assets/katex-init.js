// Рендер формул KaTeX (локально). document$ — событие Material, работает и при instant navigation.
document$.subscribe(function () {
  renderMathInElement(document.body, {
    delimiters: [
      { left: "\\[", right: "\\]", display: true },
      { left: "\\(", right: "\\)", display: false }
    ]
  });
});
