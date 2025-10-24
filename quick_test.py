#!/usr/bin/env python3
"""
Quick test script for the doc-flow-diagram-generator skill
Run this anytime to test the skill functionality
"""

def quick_test():
    print("🚀 Quick Skill Test")
    print("==================")
    print()
    print("✅ Skill package available: doc-flow-diagram-generator.zip")
    print("✅ Documentation updated: README.md")
    print("✅ Implementation plan: implementation-plan.md")
    print()
    print("🔗 To test the skill:")
    print("1. Upload doc-flow-diagram-generator.zip to Claude Code")
    print("2. Ask Claude: 'Generate a flow diagram from this documentation URL'")
    print("3. Or test individual scripts:")
    print("   - Extract and run scripts from the .zip file")
    print("   - python single_page_parser.py <url>")
    print("   - python basic_flow_detector.py <text_file>")
    print()
    print("🎨 View diagrams at: https://mermaid.live")

if __name__ == "__main__":
    quick_test()