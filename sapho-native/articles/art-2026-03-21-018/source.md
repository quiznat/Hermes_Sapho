---
version: source-capture.v1
article_id: art-2026-03-21-018
ticket_id: ticket-import-art-2026-03-21-018
source_url: https://huggingface.co/blog/royswastik/evaluating-agentic-ai-systems-part-1
canonical_url: https://huggingface.co/blog/royswastik/evaluating-agentic-ai-systems-part-1
source_title: "Part 1: From Static Models to Autonomous Agents \u2014 The Evolving\
  \ Landscape of AI Evaluation"
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-21T22:53:48Z'
---
# Source Capture

## Title

Part 1: From Static Models to Autonomous Agents — The Evolving Landscape of AI Evaluation

## Body

Part 1: From Static Models to Autonomous Agents — The Evolving Landscape of AI Evaluation
Hugging Face
Models
Datasets
Spaces
Buckets new
Docs
Enterprise
Pricing
Log In
Sign Up
Back to Articles
Part 1: From Static Models to Autonomous Agents — The Evolving Landscape of AI Evaluation
Community Article Published
March 10, 2026
Upvote -
Swastik Roy royswastik Follow
Introduction
The Three Eras of AI Evaluation Era 1: Classical Machine Learning (Pre-2018)
Era 2: Large Language Models and Benchmarks (2018–2023)
Era 3: Agentic AI Systems (2023–Present)
Why Traditional Metrics Fail for Agentic Systems
Emerging Evaluation Taxonomies The Eleven-Dimensional Taxonomy (Baduwal and Paudel, 2026)
The Four-Pillar Framework (Akshathala et al., 2025)
The Evaluation-Regulation Framework (Farooq et al., 2025)
The Benchmark Landscape for Agentic AI
A Conceptual Architecture for Agent Evaluation
Implementing Basic Agent Evaluation: A Code Example
Open Challenges Identified by the Research Community
Series Roadmap
References
Introduction
The rapid evolution of artificial intelligence from static, single-turn models to autonomous, multi-step agentic systems has fundamentally challenged how we evaluate AI capabilities. For decades, the AI community relied on well-established metrics — accuracy, F1-score, BLEU, perplexity — designed for systems that receive an input and produce an output in a single pass. These metrics served the field well when the dominant paradigm was supervised learning on fixed benchmarks. However, as Baduwal and Paudel observe in their comprehensive 2026 survey, "existing evaluation practices, largely inherited from supervised learning and short-horizon reinforcement learning, fail to capture essential agentic properties such as long-horizon coherence, robustness under uncertainty, autonomy, safety, and adaptive behavior" [1].
This blog post — the first in a seven-part series on evaluating agentic AI systems — traces the evolution of AI evaluation from classical metrics through the LLM benchmark era to the emerging challenges posed by agentic systems. It synthesizes the major evaluation taxonomies proposed by the research community and establishes the conceptual foundation for the detailed evaluation dimensions explored in subsequent posts.
The Three Eras of AI Evaluation
The history of AI evaluation can be broadly organized into three overlapping eras, each defined by the dominant system architecture and the corresponding evaluation paradigm.
Era 1: Classical Machine Learning (Pre-2018)
In the classical machine learning era, evaluation was relatively straightforward. Models were trained on labeled datasets and evaluated on held-out test sets using well-defined metrics. For classification tasks, accuracy, precision, recall, and F1-score provided clear performance signals. For regression, mean squared error and R-squared sufficed. For natural language processing, BLEU [2] and ROUGE [3] scores measured generation quality against reference outputs.
The key assumption underlying all these metrics was stationarity : the test distribution matched the training distribution, and the model's task was a single, well-defined function mapping inputs to outputs. Evaluation was a one-shot affair — give the model an input, compare its output to a ground truth, aggregate the scores.
Era 2: Large Language Models and Benchmarks (2018–2023)
The emergence of large language models, beginning with BERT [4] and accelerating through GPT-3 [5] and beyond, introduced new evaluation challenges. These models were not trained for a single task but exhibited broad capabilities across many tasks simultaneously. This necessitated multi-task benchmarks that could assess a model's breadth of knowledge and reasoning ability.
The Massive Multitask Language Understanding (MMLU) benchmark, introduced by Hendrycks et al. in 2021, became one of the most widely cited evaluation instruments, comprising 15,908 multiple-choice questions across 57 academic subjects [6]. Stanford's Holistic Evaluation of Language Models (HELM) framework went further, evaluating models across multiple dimensions including accuracy, calibration, robustness, fairness, bias, toxicity, and efficiency [7]. MT-Bench introduced multi-turn conversation evaluation using LLM-as-judge methodology [8].
These benchmarks represented a significant advance over single-task metrics, but they still evaluated models in a fundamentally passive mode: the model receives a prompt, generates a response, and is scored. There is no planning, no tool use, no environment interaction, and no multi-step execution.
Era 3: Agentic AI Systems (2023–Present)
The current era is defined by the emergence of agentic AI systems — autonomous systems capable of multi-step planning, subgoal generation, tool use, adaptation, and sustained decision-making [1] [9]. As Acharya, Kuppan, and Divya define in their widely cited IEEE Access survey, agentic AI refers to "an emerging paradigm in artificial intelligence" involving "autonomous systems" that can "plan, act, and make real decisions" in complex environments [9].
The ReAct framework, introduced by Yao et al. in 2022, formalized the paradigm of interleaving reasoning traces with task-specific actions, establishing the architectural pattern that underlies most modern agentic systems [10]. Since then, frameworks such as LangChain, AutoGen, and CrewAI have made it practical to build agents that can browse the web, execute code, query databases, and collaborate with other agents.
This shift from passive response generation to active environment interaction creates evaluation challenges that no existing benchmark was designed to address.
Why Traditional Metrics Fail for Agentic Systems
The fundamental mismatch between traditional evaluation and agentic systems can be understood through five key dimensions where the assumptions of classical evaluation break down.
Non-determinism and path dependence. Traditional evaluation assumes that for a given input, there is a correct output (or a small set of acceptable outputs). Agentic systems, however, may solve the same problem through radically different trajectories. Two agents might both successfully resolve a GitHub issue — one by modifying a single file, another by refactoring three files — yet a simple diff-based evaluation would score them differently. As Akshathala et al. note, "existing evaluations rely on binary task completion metrics that fail to capture" the behavioral uncertainty introduced by non-deterministic execution [11].
Long-horizon coherence. Classical metrics evaluate individual outputs in isolation. Agentic tasks may require dozens or hundreds of sequential steps, where the quality of early decisions constrains the space of later possibilities. SWE-bench Pro demonstrated this challenge starkly: while top-tier models achieved over 70% success on standard SWE-bench tasks, performance dropped to approximately 23% on long-horizon variants requiring sustained coherent planning [12].
Tool use and environment interaction. Traditional NLP evaluation has no concept of tool invocation. Yet in agentic systems, the ability to correctly select, parameterize, and sequence tool calls is often more important than the quality of generated text. The Berkeley Function-Calling Leaderboard (BFCL) evaluates this dimension specifically, testing models across 2,000 function-calling scenarios in multiple programming languages [13].
Safety and side effects. A language model that generates an incorrect summary causes no harm beyond providing bad information. An agent that executes incorrect code, sends unauthorized emails, or modifies production databases can cause real-world damage. Traditional evaluation has no mechanism for assessing whether an agent's actions are safe, reversible, or aligned with user intent.
Autonomy and human intervention. Classical evaluation is fully automated — there is no concept of an AI system requesting help, escalating to a human, or recognizing the limits of its own competence. Agentic systems must be evaluated not only on what they accomplish but on whether they appropriately seek human oversight when needed.
Emerging Evaluation Taxonomies
The research community has responded to these challenges by proposing multi-dimensional evaluation frameworks. Three major taxonomies have emerged, each offering a complementary perspective.
The Eleven-Dimensional Taxonomy (Baduwal and Paudel, 2026)
The most comprehensive taxonomy to date was proposed by Baduwal and Paudel in their TechRxiv survey [1]. Their framework organizes evaluation into eleven dimensions, which we summarize in the following table:
Dimension
What It Measures
Example Metrics
Task Success
Whether the agent achieves its goal
Completion rate, goal satisfaction
Output Quality
Quality of generated artifacts
Correctness, coherence, relevance
Planning and Reasoning
Multi-step planning capability
Plan validity, reasoning chain quality
Decision-Making Under Uncertainty
Handling of ambiguous or incomplete information
Calibration, risk-adjusted performance
Tool-Use Effectiveness
Correct selection and invocation of tools
Tool accuracy, API call correctness
Autonomy and Human Intervention
Appropriate balance of autonomy and escalation
Intervention frequency, escalation appropriateness
Learning and Adaptation
Ability to improve from experience
In-context learning rate, adaptation speed
Safety and Alignment
Adherence to safety constraints and human values
Harm rate, constraint violation frequency
Efficiency and Resource Utilization
Computational and financial cost
Token usage, latency, cost per task
Multi-Agent Collaboration
Coordination in multi-agent settings
Communication efficiency, task allocation quality
Long-Term Memory Consistency
Coherence over extended interactions
Memory recall accuracy, consistency score
The Four-Pillar Framework (Akshathala et al., 2025)
Akshathala et al. proposed a complementary framework grounded in their industry collaboration with MontyCloud Inc. [11]. Their Agent Assessment Framework evaluates agentic systems across four pillars:
LLM Pillar : Evaluates the underlying language model's reasoning, instruction following, and generation quality.
Memory Pillar : Assesses how effectively the agent stores, retrieves, and utilizes information across interactions.
Tools Pillar : Measures the agent's ability to correctly invoke external tools and APIs.
Environment Pillar : Evaluates the agent's interaction with its deployment context, including error handling and state management.
This framework is notable for its emphasis on runtime behavioral analysis rather than static benchmark scores, reflecting the practical reality that agent behavior in production often diverges from benchmark performance.
The Evaluation-Regulation Framework (Farooq et al., 2025)
Farooq et al. contributed a framework that bridges technical evaluation with regulatory considerations, examining how benchmarks and metrics can inform governance and compliance requirements for agentic AI [14]. This perspective is increasingly important as regulatory frameworks such as the EU AI Act begin to mandate specific evaluation requirements for high-risk AI systems.
The Benchmark Landscape for Agentic AI
The proliferation of agentic AI benchmarks reflects the community's recognition that new evaluation instruments are needed. The following table summarizes the major benchmarks, organized by their primary evaluation focus:
Benchmark
Year
Primary Focus
Scale
Key Innovation
WebShop [15]
2022
Web interaction
1.18M products, 12K tasks
Grounded language agents in realistic e-commerce
AgentBench [16]
2023
Multi-environment reasoning
8 environments
First systematic multi-environment agent evaluation
WebArena [17]
2023
Autonomous web tasks
812 tasks, 4 domains
Self-hosted realistic web environment
GAIA [18]
2023
General AI assistance
466 tasks, 3 levels
Human-annotated multi-modal tasks
SWE-bench [19]
2024
Software engineering
2,294 GitHub issues
Real-world code generation and repair
BFCL [13]
2024
Function calling
2,000 scenarios
Multi-language tool invocation evaluation
AgentDojo [20]
2024
Security (prompt injection)
Dynamic environment
Adversarial robustness evaluation
ToolEmu [21]
2024
Safety risk identification
LM-emulated sandbox
Risk assessment without real execution
MINT [22]
2024
Multi-turn tool interaction
Multi-turn dialogues
Language feedback integration
SWE-bench Pro [12]
2025
Long-horizon SE tasks
Extended tasks
Tests sustained coherent planning
A critical observation from this landscape is that no single benchmark covers all evaluation dimensions . SWE-bench excels at measuring task completion in software engineering but does not assess safety. AgentDojo evaluates security robustness but not general task performance. GAIA tests breadth but not depth. This fragmentation means that a comprehensive evaluation of any agentic system requires combining multiple benchmarks — a practice that introduces its own challenges around standardization and comparability.
A Conceptual Architecture for Agent Evaluation
Drawing from the frameworks surveyed above, we can identify a layered evaluation architecture that the research community is converging toward. The following diagram illustrates this architecture:
Diagram
Layer 1 (Foundation Model Evaluation) assesses the base capabilities of the underlying language model using established benchmarks like MMLU and HumanEval. Layer 2 (Capability Evaluation) measures agentic-specific capabilities such as planning, tool use, and memory. Layer 3 (Behavioral Evaluation) evaluates emergent properties like safety, robustness, and appropriate autonomy. Layer 4 (System-Level Evaluation) assesses the complete system in terms of end-to-end task success, efficiency, and user satisfaction.
This layered architecture reflects a key insight: agentic evaluation is not a replacement for model evaluation but an extension of it . The foundation model's capabilities constrain the agent's potential, but the agent's architecture, tools, and orchestration logic determine how effectively that potential is realized.
Implementing Basic Agent Evaluation: A Code Example
To ground these concepts in practice, the following Python example demonstrates how to implement a basic evaluation harness for an agentic system. This code follows the patterns established in the evaluation literature, particularly the trajectory-based evaluation approach advocated by Akshathala et al. [11]:
"""
Basic Agent Evaluation Harness
Implements trajectory-based evaluation following the patterns
described in Akshathala et al. (2025) and Baduwal & Paudel (2026).
"""
from dataclasses import dataclass, field
from typing import List , Dict , Optional , Any
from enum import Enum
import time
import json
class ActionType ( Enum ):
"""Types of actions an agent can take."""
REASONING = "reasoning"
TOOL_CALL = "tool_call"
RESPONSE = "response"
ESCALATION = "escalation"
@dataclass
class AgentAction :
"""Represents a single action in an agent's trajectory."""
action_type: ActionType
content: str
timestamp: float
metadata: Dict [ str , Any ] = field(default_factory= dict )
tool_name: Optional [ str ] = None
tool_args: Optional [ Dict ] = None
tool_result: Optional [ str ] = None
@dataclass
class AgentTrajectory :
"""Complete trajectory of an agent solving a task."""
task_id: str
actions: List [AgentAction] = field(default_factory= list )
final_output: Optional [ str ] = None
success: Optional [ bool ] = None
total_tokens: int = 0
total_cost: float = 0.0
@dataclass
class EvaluationResult :
"""Multi-dimensional evaluation result."""
task_success: float # 0.0 to 1.0
output_quality: float # 0.0 to 1.0
planning_coherence: float # 0.0 to 1.0
tool_use_accuracy: float # 0.0 to 1.0
efficiency_score: float # 0.0 to 1.0
safety_score: float # 0.0 to 1.0
details: Dict [ str , Any ] = field(default_factory= dict )
class AgentEvaluator :
"""
Multi-dimensional agent evaluator.
Evaluates agent trajectories across the dimensions identified
in the agentic AI evaluation literature [1][11].
"""
def __init__ ( self, unsafe_patterns: Optional [ List [ str ]] = None ):
self.unsafe_patterns = unsafe_patterns or [
"rm -rf" , "DROP TABLE" , "sudo" ,
"password" , "secret" , "DELETE FROM"
]
def evaluate_trajectory (
self,
trajectory: AgentTrajectory,
ground_truth: Optional [ str ] = None ,
max_expected_steps: int = 20 ,
max_expected_tokens: int = 10000
) -> EvaluationResult:
"""
Evaluate a complete agent trajectory across multiple dimensions.
This implements the multi-dimensional evaluation approach
described in Baduwal & Paudel (2026), assessing task success,
output quality, planning coherence, tool use, efficiency,
and safety.
"""
return EvaluationResult(
task_success=self._evaluate_task_success(
trajectory, ground_truth
),
output_quality=self._evaluate_output_quality(
trajectory, ground_truth
),
planning_coherence=self._evaluate_planning(trajectory),
tool_use_accuracy=self._evaluate_tool_use(trajectory),
efficiency_score=self._evaluate_efficiency(
trajectory, max_expected_steps, max_expected_tokens
),
safety_score=self._evaluate_safety(trajectory),
details={
"num_steps" : len (trajectory.actions),
"num_tool_calls" : sum (
1 for a in trajectory.actions
if a.action_type == ActionType.TOOL_CALL
),
"num_escalations" : sum (
1 for a in trajectory.actions
if a.action_type == ActionType.ESCALATION
),
"total_tokens" : trajectory.total_tokens,
}
)
def _evaluate_task_success (
self, trajectory: AgentTrajectory,
ground_truth: Optional [ str ]
) -> float :
"""Binary or graded task success evaluation."""
if trajectory.success is not None :
return 1.0 if trajectory.success else 0.0
if ground_truth and trajectory.final_output:
# Normalized string similarity as a simple proxy
# In practice, use LLM-as-judge or task-specific metrics
return self._string_similarity(
trajectory.final_output, ground_truth
)
return 0.0
def _evaluate_output_quality (
self, trajectory: AgentTrajectory,
ground_truth: Optional [ str ]
) -> float :
"""Evaluate the quality of the final output."""
if not trajectory.final_output:
return 0.0
score = min ( len (trajectory.final_output) / 100 , 1.0 )
if ground_truth:
score = (
score + self._string_similarity(
trajectory.final_output, ground_truth
)
) / 2
return score
def _evaluate_planning (
self, trajectory: AgentTrajectory
) -> float :
"""
Evaluate planning coherence by analyzing the reasoning
chain structure. Checks for presence of reasoning steps,
logical ordering, and absence of redundant loops.
"""
reasoning_steps = [
a for a in trajectory.actions
if a.action_type == ActionType.REASONING
]
if not reasoning_steps:
return 0.0
# Check reasoning-to-action ratio
total_steps = len (trajectory.actions)
reasoning_ratio = len (reasoning_steps) / total_steps
ratio_score = min (reasoning_ratio / 0.3 , 1.0 )
# Check for redundant consecutive identical actions
redundancy_penalty = 0.0
for i in range ( 1 , len (trajectory.actions)):
if (trajectory.actions[i].content ==
trajectory.actions[i- 1 ].content):
redundancy_penalty += 0.1
return max ( 0.0 , ratio_score - redundancy_penalty)
def _evaluate_tool_use (
self, trajectory: AgentTrajectory
) -> float :
"""
Evaluate tool use accuracy: correct tool selection,
valid arguments, and successful execution.
"""
tool_calls = [
a for a in trajectory.actions
if a.action_type == ActionType.TOOL_CALL
]
if not tool_calls:
return 1.0 # No tool calls needed
successful = sum (
1 for tc in tool_calls
if tc.tool_result and "error" not in tc.tool_result.lower()
)
return successful / len (tool_calls)
def _evaluate_efficiency (
self, trajectory: AgentTrajectory,
max_steps: int , max_tokens: int
) -> float :
"""
Evaluate efficiency relative to expected resource usage.
"""
step_efficiency = max (
0.0 , 1.0 - len (trajectory.actions) / max_steps
)
token_efficiency = max (
0.0 , 1.0 - trajectory.total_tokens / max_tokens
)
return (step_efficiency + token_efficiency) / 2
def _evaluate_safety (
self, trajectory: AgentTrajectory
) -> float :
"""
Evaluate safety by checking for unsafe patterns in
tool calls and generated content.
"""
violations = 0
total_checks = 0
for action in trajectory.actions:
if action.action_type == ActionType.TOOL_CALL:
total_checks += 1
content = json.dumps(action.tool_args or {}).lower()
if any (p in content for p in self.unsafe_patterns):
violations += 1
if action.action_type == ActionType.RESPONSE:
total_checks += 1
if any (
p in action.content.lower()
for p in self.unsafe_patterns
):
violations += 1
if total_checks == 0 :
return 1.0
return 1.0 - (violations / total_checks)
@staticmethod
def _string_similarity ( a: str , b: str ) -> float :
"""Simple Jaccard similarity between token sets."""
tokens_a = set (a.lower().split())
tokens_b = set (b.lower().split())
if not tokens_a or not tokens_b:
return 0.0
intersection = tokens_a & tokens_b
union = tokens_a | tokens_b
return len (intersection) / len (union)
# --- Example Usage ---
if __name__ == "__main__" :
# Simulate an agent trajectory
trajectory = AgentTrajectory(task_id= "task_001" )
trajectory.actions = [
AgentAction(
action_type=ActionType.REASONING,
content= "I need to find the population of France. "
"Let me search for this information." ,
timestamp=time.time()
),
AgentAction(
action_type=ActionType.TOOL_CALL,
content= "Calling search API" ,
timestamp=time.time(),
tool_name= "web_search" ,
tool_args={ "query" : "population of France 2024" },
tool_result= "France population: approximately 68.4 million"
),
AgentAction(
action_type=ActionType.REASONING,
content= "The search returned the population figure. "
"Let me formulate the response." ,
timestamp=time.time()
),
AgentAction(
action_type=ActionType.RESPONSE,
content= "The population of France in 2024 is approximately "
"68.4 million people." ,
timestamp=time.time()
),
]
trajectory.final_output = (
"The population of France in 2024 is approximately "
"68.4 million people."
)
trajectory.success = True
trajectory.total_tokens = 1500
# Evaluate
evaluator = AgentEvaluator()
result = evaluator.evaluate_trajectory(
trajectory,
ground_truth= "The population of France is about 68.4 million." ,
max_expected_steps= 10 ,
max_expected_tokens= 5000
)
print ( "=== Evaluation Results ===" )
print ( f"Task Success: {result.task_success: .2 f} " )
print ( f"Output Quality: {result.output_quality: .2 f} " )
print ( f"Planning Coherence: {result.planning_coherence: .2 f} " )
print ( f"Tool Use Accuracy: {result.tool_use_accuracy: .2 f} " )
print ( f"Efficiency Score: {result.efficiency_score: .2 f} " )
print ( f"Safety Score: {result.safety_score: .2 f} " )
print ( f"Details: {result.details} " )
This implementation demonstrates several principles from the evaluation literature. First, it captures the complete trajectory rather than just the final output, following the trajectory-based evaluation approach. Second, it evaluates across multiple dimensions simultaneously, reflecting the multi-dimensional taxonomies proposed by the research community. Third, it separates capability evaluation (tool use, planning) from behavioral evaluation (safety), mirroring the layered architecture described above.
Open Challenges Identified by the Research Community
The evaluation literature consistently identifies several persistent challenges that remain unresolved:
Benchmark overfitting and contamination. As Baduwal and Paudel note, there is growing concern that agent performance on established benchmarks may not reflect genuine capability but rather memorization or optimization for specific benchmark patterns [1]. The dramatic performance gap between SWE-bench and SWE-bench Pro (70%+ vs. ~23%) illustrates how benchmark-specific optimization can inflate perceived capability [12].
Reproducibility. The non-deterministic nature of LLM-based agents means that evaluation results can vary significantly across runs. Standardized evaluation protocols that account for this variance remain an open problem [11].
Evaluation cost. Comprehensive agent evaluation is expensive. Running an agent through hundreds of multi-step tasks, each requiring multiple LLM calls and tool invocations, can cost thousands of dollars. This creates a barrier to thorough evaluation, particularly for academic researchers [1].
The evaluator problem. Many modern evaluation approaches use LLMs as judges (the "LLM-as-judge" paradigm). However, this introduces circular dependencies: the systems being evaluated are also the systems doing the evaluating. The reliability and biases of LLM-based evaluation remain active areas of research [8].
Series Roadmap
This post has established the conceptual foundation for understanding why agentic AI evaluation requires fundamentally new approaches. The remaining posts in this series will dive deep into specific evaluation dimensions:
Part 2: Evaluating Novelty and Scientific Discovery — Methods and metrics for assessing whether agents can produce genuinely novel outputs.
Part 3: Observability and Interpretability — Tracing, monitoring, and debugging autonomous decision-making.
Part 4: Security Evaluation — Threat taxonomies, adversarial benchmarks, and red-teaming methodologies.
Part 5: Safety, Alignment, and Guardrails — Evaluating responsible behavior in autonomous agents.
Part 6: Generalizability and Robustness — Cross-domain transfer, out-of-distribution performance, and the benchmark overfitting problem.
Part 7: Toward Unified Evaluation Frameworks — Synthesis, open challenges, and future research directions.
References
[1]: Baduwal, M. & Paudel, P. (2026). "Evaluating Agentic Artificial Intelligence: A Comprehensive Survey of Metrics, Benchmarks, and Methodologies." TechRxiv. https://doi.org/10.36227/techrxiv.177162480.04513202
[2]: Papineni, K. et al. (2002). "BLEU: A Method for Automatic Evaluation of Machine Translation." ACL 2002.
[3]: Lin, C.-Y. (2004). "ROUGE: A Package for Automatic Evaluation of Summaries." Text Summarization Branches Out, ACL Workshop.
[4]: Devlin, J. et al. (2019). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding." NAACL 2019.
[5]: Brown, T. et al. (2020). "Language Models are Few-Shot Learners." NeurIPS 2020.
[6]: Hendrycks, D. et al. (2021). "Measuring Massive Multitask Language Understanding." ICLR 2021.
[7]: Liang, P. et al. (2022). "Holistic Evaluation of Language Models." arXiv:2211.09110.
[8]: Zheng, L. et al. (2023). "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena." NeurIPS 2023.
[9]: Acharya, D.B., Kuppan, K. & Divya, B. (2025). "Agentic AI: Autonomous Intelligence for Complex Goals — A Comprehensive Survey." IEEE Access.
[10]: Yao, S. et al. (2022). "ReAct: Synergizing Reasoning and Acting in Language Models." ICLR 2023. arXiv:2210.03629.
[11]: Akshathala, S. et al. (2025). "Beyond Task Completion: An Assessment Framework for Evaluating Agentic AI Systems." arXiv:2512.12791.
[12]: SWE-bench Pro (2025). "Can AI Agents Solve Long-Horizon Software Engineering Tasks?" arXiv:2509.16941.
[13]: Yan, F. et al. (2024). "Berkeley Function-Calling Leaderboard." arXiv:2402.15671.
[14]: Farooq, A. et al. (2025). "Evaluating and Regulating Agentic AI: A Study of Benchmarks, Metrics, and Regulation." SSRN.
[15]: Yao, S. et al. (2022). "WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents." NeurIPS 2022.
[16]: Liu, X. et al. (2023). "AgentBench: Evaluating LLMs as Agents." ICLR 2024.
[17]: Zhou, S. et al. (2023). "WebArena: A Realistic Web Environment for Building Autonomous Agents." ICLR 2024.
[18]: Mialon, G. et al. (2023). "GAIA: A Benchmark for General AI Assistants." arXiv:2311.12983.
[19]: Jimenez, C.E. et al. (2024). "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?" ICLR 2024.
[20]: Debenedetti, E. et al. (2024). "AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents." NeurIPS 2024.
[21]: Ruan, Y. et al. (2024). "Identifying the Risks of LM Agents with an LM-Emulated Sandbox." ICLR 2024.
[22]: Wang, X. et al. (2024). "MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback." ICLR 2024.
Community
Edit Preview
Upload images, audio, and videos by dragging in the text input, pasting, or clicking here .
Tap or paste here to upload images
Comment · Sign up or log in to comment
Upvote -
System theme
Company
TOS Privacy About Careers Website
Models Datasets Spaces Pricing Docs

## Import Provenance

- imported_from: canonical-openclaw-runtime
- runtime_article_bundle_path: research/articles/art-2026-03-21-018.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-21-018.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-21-018.txt
- runtime_filter_state: pending
- runtime_last_stage: facts
- refreshed_live_source: false
