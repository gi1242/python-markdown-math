## Math extension for Python-Markdown

This extension adds math formulas support to [Python-Markdown].

[Python-Markdown]: https://github.com/Python-Markdown/markdown

This extension stops markdown from processing text inside math delimiters, so
that it can be rendered by MathJax/KaTeX. Without this extension enabled the
markdown code:

    $a*b*c$
    \begin{align*}
      x &= y\\
      y &= z
    \end{align*}

will get borked, as the `*`'s will be replaced by `<em>...</em>`.

To use this extension, you need to
include MathJax or KaTeX in your HTML files.

* [Instructions to include MathJAX](https://www.mathjax.org/#gettingstarted)
* [Instructions to include KaTeX](https://katex.org/docs/browser.html)
* Alternately, a full fledged extension that renders KaTeX server side can be
  found [here](https://pypi.org/project/markdown-katex/)

To render markdown with this extension enabled, use `mdx_math` as extension
name:

```python
import markdown
md = markdown.Markdown(extensions=['mdx_math'])
md.convert( r'\(a*b*c\)' )
```

Alternately, to pass options, use the `MathExtension` function:
```python
import markdown, mdx_math
md = markdown.Markdown( extensions=[
        mdx_math.MathExtension(enable_dollar_delimiter=True) )
md.convert( '$a*b*c$' )
```

If the fragment you rendered uses math, then `uses_math` property will be
`True`. This property will be cleared when the `reset()` method is called.

```python
md.reset()
md.convert( ... )
if md.uses_math:
    # Also include MathJAX / KaTeX in your document.
```

### Usage from the command line:

```shell
$ echo '\(a*b*c\)' | python3 -m markdown -x mdx_math
<p>\( a*b*c \)</p>
```

### Math Delimiters

* Inline math: `\(...\)`.
* Standalone math: `$$...$$`, `\[...\]` or `\begin...\end`.
* The single-dollar delimiter (`$...$`) for inline math is disabled by
  default, but can be enabled by passing `enable_dollar_delimiter=True` in the
  extension configuration. In this case, remember to also enable it with
  MathJax / KaTeX.

## Notes

The code was based on an extension of the same name by Dmitry Shachnev. The
current version is essentially a complete rewrite.
* It uses the new, faster `InlineProcessor` framework of Python Markdown.
* It leaves math regions unchanged, instead of using the `<script
  type='text/math'>...</script>`. In MathJax 3 (which offers a huge speed
  increase) these tags are not used anymore.
* All the Travis CI stuff was also removed, since I don't know what that is 😂
* All PyPI stuff was removed so it doesn't cause confusion / conflict with the
  original extension.
* The testdata from the old version is still here and left unchanged. So all
  tests fail (since the new version doesn't use the `<script>` tags), but I
  left them there so that if I eventually update the data I can use it.
