#!/usr/bin/env python3
"""
Basic Flow Detector - Identify sequential workflows in documentation content

This script analyzes text content to identify step-by-step workflows
using common patterns like numbered lists and temporal indicators.
"""

import re
from dataclasses import dataclass
from typing import List

@dataclass
class FlowStep:
    number: int
    text: str
    confidence: float
    step_type: str

@dataclass
class DetectedFlow:
    title: str
    steps: List[FlowStep]
    confidence: float

class BasicFlowDetector:
    def __init__(self):
        self.numbered_patterns = [
            r'^(\d+)\.?\s+(.+)$',  # "1. Step text"
            r'^Step\s+(\d+):?\s*(.+)$',  # "Step 1: Step text"
        ]

        self.temporal_keywords = [
            'first', 'then', 'next', 'after', 'finally', 'lastly'
        ]

    def detect_numbered_flows(self, lines: List[str]) -> List[DetectedFlow]:
        """Detect flows based on numbered lists"""
        flows = []
        current_steps = []

        for line in lines:
            line = line.strip()
            if not line:
                continue

            for pattern in self.numbered_patterns:
                match = re.match(pattern, line, re.IGNORECASE)
                if match:
                    step_num = int(match.group(1))
                    step_text = match.group(2).strip()

                    if step_num == 1 and current_steps:
                        # Save previous flow
                        if len(current_steps) >= 2:
                            flows.append(DetectedFlow(
                                title="Workflow",
                                steps=current_steps,
                                confidence=0.8
                            ))
                        current_steps = []

                    step = FlowStep(
                        number=step_num,
                        text=step_text,
                        confidence=0.9,
                        step_type='numbered'
                    )
                    current_steps.append(step)
                    break

        # Add final flow
        if len(current_steps) >= 2:
            flows.append(DetectedFlow(
                title="Workflow",
                steps=current_steps,
                confidence=0.8
            ))

        return flows

    def detect_flows(self, content: str) -> List[DetectedFlow]:
        """Main method to detect flows in content"""
        lines = content.split('\n')
        return self.detect_numbered_flows(lines)