# neddwyer.com

Source for [neddwyer.com](https://neddwyer.com). Hugo-built, deployed to GitHub Pages via Actions.

## Structure

```
content/        # Markdown for pages and posts
themes/neddwyer # Custom theme (templates + CSS)
hugo.toml       # Site config
```

## Writing a new post

```bash
cd ~/projects/neddwyer-com
hugo new posts/my-new-post.md
# edit content/posts/my-new-post.md
hugo server   # preview at http://localhost:1313
git add content/posts/my-new-post.md
git commit -m "Add post: my-new-post"
git push      # action builds and deploys
```

## Deployment

- Source branch: `source` (this branch)
- Output branch: `master` (auto-built by Action, serves at neddwyer.com)
- GitHub Action: `.github/workflows/hugo.yml`

The Action triggers on every push to `source`, builds Hugo, and force-pushes
the `public/` directory to `master`.

## Local preview

```bash
hugo server --buildDrafts
```

Open http://localhost:1313.

## Theme

Custom theme at `themes/neddwyer/`:
- Coral accent (`#e15554`) on white
- EB Garamond for body & headings
- Inter for metadata
- Single-column, ~680px max content width
- No JavaScript

## Drafts

Mark a post as a draft with `draft: true` in the frontmatter. Drafts only
appear in `hugo server --buildDrafts`, never in the deployed site.
