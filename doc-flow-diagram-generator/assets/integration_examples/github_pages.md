# GitHub Pages Integration

This template shows how to embed generated flow diagrams in GitHub Pages documentation.

## Basic Integration

Add this to your markdown files to display Mermaid diagrams:

```markdown
# Your Documentation Title

## Workflow Overview

```mermaid
flowchart TD
    A[Start] --> B[Step 1]
    B --> C[Step 2]
    C --> D[End]

    click A "https://your-docs.github.io/page#start" "Go to Start"
    click B "https://your-docs.github.io/page#step-1" "View Step 1"
    click C "https://your-docs.github.io/page#step-2" "View Step 2"
    click D "https://your-docs.github.io/page#end" "Go to End"
```

## Advanced Integration with Jekyll

### _config.yml Configuration

```yaml
# Enable Mermaid support
markdown: kramdown
highlighter: rouge

plugins:
  - jekyll-mermaid

# Mermaid configuration
mermaid:
  src: 'https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js'
```

## Best Practices

### 1. Responsive Design
```css
.mermaid svg {
    max-width: 100%;
    height: auto;
}
```

### 2. Link Validation
Test all diagram links before publishing.

### 3. SEO Optimization
Add diagram descriptions for accessibility.