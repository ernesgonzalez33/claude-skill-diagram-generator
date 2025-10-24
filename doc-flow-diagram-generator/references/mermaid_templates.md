# Mermaid Templates and Best Practices

This reference provides templates and guidelines for generating consistent, interactive Mermaid flowcharts.

## Basic Flowchart Template

```mermaid
flowchart TD
    A[Start: Page Title] --> B[Step 1: Action]
    B --> C[Step 2: Action]
    C --> D[End: Completion]

    %% Clickable links back to documentation
    click A "https://docs.example.com#getting-started" "Go to Getting Started"
    click B "https://docs.example.com#step-1" "Go to Step 1"
    click C "https://docs.example.com#step-2" "Go to Step 2"
    click D "https://docs.example.com#completion" "Go to Completion"
```

## Node Types and Shapes

### Process Nodes (Rectangles)
```mermaid
A[Standard Process Step]
```
**Use for**: Regular workflow steps, actions, processes

### Decision Nodes (Diamonds)
```mermaid
B{Decision Point?}
```
**Use for**: Conditional branches, yes/no questions, choices

### Start/End Nodes (Rounded)
```mermaid
C([Start Process])
D([End Process])
```
**Use for**: Clear workflow boundaries, entry/exit points

## Best Practices

### Node Naming
- **Be concise**: Max 3-4 words per node
- **Use action verbs**: "Configure", "Install", "Verify"
- **Be specific**: "Install CLI" vs "Install"
- **Consistent tense**: Use imperative form

### Flow Organization
- **Top to bottom**: Primary flow direction
- **Left to right**: For parallel processes
- **Minimize crossings**: Reduce line complexity

### Link Strategy
- **Every node should be clickable** when possible
- **Use descriptive link text**: Helpful for accessibility
- **Test all links**: Ensure they point to correct sections