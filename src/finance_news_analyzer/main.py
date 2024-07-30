#!/usr/bin/env python
import sys
from finance_news_analyzer.crew import FinanceNewsAnalyzerCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'us fund market',
    }
    FinanceNewsAnalyzerCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "fund market"
    }
    try:
        FinanceNewsAnalyzerCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        FinanceNewsAnalyzerCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
