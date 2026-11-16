# Personal Academic Website

This repository hosts Carol Rodriguez's academic homepage.

Publications live in `_publications/` as one Markdown file per entry. Each file
starts with YAML front matter:

```yaml
title: ...
venue: ...
year: ...
citation: ...
codeurl: ...   # optional; rendered as a "Code" link
```

`_includes/archive-single.html` renders the optional `codeurl` field as a code
link on the publication list. Entries without `codeurl` simply show no link.
