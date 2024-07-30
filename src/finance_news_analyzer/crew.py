from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_huggingface import HuggingFaceEndpoint

from finance_news_analyzer.tools.bloomberg_tool import BloombergTool

@CrewBase
class FinanceNewsAnalyzerCrew():
	"""FinanceNewsAnalyzer crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	llm = HuggingFaceEndpoint(
		repo_id="mistralai/Mistral-7B-Instruct-v0.2",
		task="text-generation",
		max_new_tokens=512,
		do_sample=False,
		repetition_penalty=1.03,
	)

	@agent
	def analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['analyst'],
			tools=[BloombergTool()],
			verbose=True,
			llm = self.llm
		)


	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['analyst_task'],
			agent=self.analyst(),
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=2
		)