# Flow Detection Patterns

This reference document contains patterns for identifying user workflows in documentation.

## Basic Sequential Patterns

### Numbered Lists
- **Pattern**: `1.`, `2.`, `3.` or `Step 1`, `Step 2`, `Step 3`
- **Context**: Usually found in tutorials, getting started guides
- **Example**: "1. Install the CLI 2. Configure your credentials 3. Run your first command"

### Temporal Indicators
- **Keywords**: "first", "then", "next", "after", "finally", "lastly"
- **Pattern**: Sentences starting with these keywords often indicate workflow steps
- **Example**: "First, create an account. Then, verify your email. Finally, log in to the dashboard."

### Procedural Headings
- **Pattern**: `## Step 1:`, `### Getting Started`, `#### Configure Settings`
- **Context**: Documentation sections that break down processes
- **Confidence**: High when combined with action verbs

## Advanced Flow Patterns

### Conditional Workflows
- **Keywords**: "if", "unless", "when", "depending on", "choose", "select"
- **Pattern**: Decision points that branch the workflow
- **Example**: "If you're using OAuth, follow these steps. Otherwise, use API keys."

### Alternative Paths
- **Keywords**: "alternatively", "or", "instead", "another option"
- **Pattern**: Multiple ways to achieve the same goal
- **Structure**: Usually parallel paths that converge

## Quality Indicators

### High Confidence Signals
- Multiple sequential indicators in close proximity
- Action verbs paired with sequential markers
- Code examples that build on each other
- Clear start and end points

### Low Confidence Signals
- Single isolated sequential words
- Reference material without procedural context
- FAQ sections (usually not workflow-oriented)
- Troubleshooting sections (reactive, not proactive flows)