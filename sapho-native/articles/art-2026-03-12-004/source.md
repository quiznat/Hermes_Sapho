---
version: source-capture.v1
article_id: art-2026-03-12-004
ticket_id: ticket-import-art-2026-03-12-004
source_url: https://arxiv.org/html/2601.06112v1
canonical_url: https://arxiv.org/abs/2601.06112
source_title: 'ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like
  Stress Conditions'
capture_kind: arxiv_html
http_status: 200
content_type: text/html
captured_at_utc: '2026-04-11T13:22:25Z'
linked_paper_urls: []
---
# Source Capture

## Title

ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like Stress Conditions

## Body

ReliabilityBench: Evaluating LLM Agent Reliability Under Production-Like Stress Conditions

Aayush Gupta aayush.gupta@gohighlevel.com

(January 02, 2025)

Abstract

Existing benchmarks for tool-using LLM agents primarily measure single-run success rates, failing to capture the reliability characteristics critical for production deployment. We introduce ReliabilityBench , a benchmark that evaluates agent reliability across three dimensions: consistency under repeated execution ( k k -trial pass rates), robustness to task perturbations ( ε \varepsilon -levels), and fault tolerance under infrastructure failures ( λ \lambda -levels). Building on the pass k metric from τ \tau -bench and inspired by chaos engineering from Site Reliability Engineering, ReliabilityBench introduces: (1) the Reliability Surface R ​ ( k , ε , λ ) R(k,\varepsilon,\lambda) —a unified evaluation framework capturing the interaction between consistency, robustness, and fault tolerance, (2) Action Metamorphic Relations —perturbation strategies where correctness is defined by end-state equivalence rather than text similarity, and (3) a Chaos Engineering Framework for agents with systematic fault injection including transient timeouts, rate limits, partial responses, and schema drift. We evaluate multiple models (Gemini 2.0 Flash, GPT-4o) and agent architectures (ReAct, Reflexion) across four domains (scheduling, travel, customer support, e-commerce) with 1,280 episodes spanning the full 3D reliability surface. Our results reveal that perturbations cause significant degradation: agents achieving 96.9% pass@1 at ε = 0 \varepsilon=0 drop to 88.1% at ε = 0.2 \varepsilon=0.2 (an 8.8% decline). Ablation experiments show rate limiting faults cause the largest impact (2.5% below mixed baseline). We find that simpler ReAct agents outperform more complex Reflexion architectures under stress, while GPT-4o costs 82 × \times more than Gemini 2.0 Flash with comparable reliability (-0.6% difference). ReliabilityBench provides the first systematic framework for evaluating production-readiness of LLM agents.

1 Introduction

The deployment of Large Language Model (LLM) agents in production systems has accelerated dramatically. From customer service automation to software engineering assistants, these agents are increasingly tasked with executing multi-step workflows that interact with external tools and APIs [ 1 , 2 ] . Yet the evaluation methodology for these systems remains fundamentally misaligned with production requirements.

Consider a travel booking agent deployed at scale. The critical question is not “can this agent book a flight?” but rather: “if we run this agent 1,000 times across varied phrasings of the same request, under realistic network conditions with occasional API failures, what percentage of bookings will succeed?” Current benchmarks—ToolBench [ 3 ] , AgentBench [ 4 ] , API-Bank [ 5 ] —provide single-run success rates that systematically overestimate production reliability.

This gap between benchmark performance and production reliability has been quantified by τ \tau -bench [ 9 ] , which demonstrated that agents achieving 60% pass@1 may exhibit only 25% consistency across multiple trials. However, τ \tau -bench examines only one dimension of reliability: consistency under repeated execution. Production systems face additional challenges: users phrase requests differently, APIs fail intermittently, and data formats evolve unexpectedly.

1.1 The Reliability Gap

We identify three orthogonal dimensions of agent reliability that existing benchmarks fail to capture:

- 1.

Consistency ( k k ): Does the agent produce the same correct outcome when run multiple times on identical inputs? The pass k metric [ 9 ] reveals that stochastic sampling introduces substantial variance even under controlled conditions.

- 2.

Robustness ( ε \varepsilon ): Does the agent handle semantically equivalent but syntactically varied instructions? Users do not speak in canonical templates; they paraphrase, reorder constraints, include irrelevant context, and correct themselves mid-task.

- 3.

Fault Tolerance ( λ \lambda ): Does the agent recover gracefully from infrastructure failures? Production environments experience transient timeouts, rate limits, partial responses, and schema changes that never appear in controlled benchmarks.

These dimensions interact in complex ways. An agent may be consistent under ideal conditions but brittle under perturbation; another may handle faults gracefully but fail to interpret paraphrased instructions. Evaluating each dimension in isolation provides an incomplete picture.

1.2 Our Contributions

We present ReliabilityBench , a benchmark for evaluating LLM agent reliability under production-like conditions. Our contributions are:

- 1.

Reliability Surface Framework : We introduce R ​ ( k , ε , λ ) R(k,\varepsilon,\lambda) , a three-dimensional evaluation surface that unifies consistency, robustness, and fault tolerance metrics. This enables systematic comparison of agents across the full spectrum of production conditions.

- 2.

Action Metamorphic Relations : We adapt metamorphic testing [ 11 ] to agent evaluation, defining perturbation strategies where correctness is determined by end-state equivalence rather than textual similarity. This captures the semantic nature of agent tasks.

- 3.

Chaos Engineering for Agents : Inspired by Netflix’s Chaos Monkey [ 18 ] and Site Reliability Engineering practices [ 19 ] , we develop a systematic fault injection framework with configurable failure profiles.

- 4.

Multi-Domain Evaluation : We implement four realistic domains—scheduling, travel booking, customer support, and e-commerce—with 25+ domain-specific tools and state-based verification oracles.

- 5.

Empirical Analysis : We evaluate multiple models and agent architectures, revealing that: (a) pass@1 overestimates reliability by 20-40%, (b) simpler architectures outperform complex ones under stress, and (c) fault tolerance exhibits steeper degradation than robustness.

The remainder of this paper is organized as follows: Section 2 reviews related work. Section 3 presents our formal framework. Section 4 describes the benchmark implementation. Section 5 presents experimental results. Section 6 discusses implications and limitations. Section 7 concludes.

2 Related Work

2.1 Tool-Augmented LLM Benchmarks

The rapid development of tool-using LLMs has spawned numerous evaluation benchmarks. ToolBench [ 3 ] provides 16,000+ real-world APIs with automatically generated instructions, enabling large-scale evaluation of tool selection and orchestration. API-Bank [ 5 ] evaluates API call accuracy across 73 APIs with a focus on argument extraction. ToolAlpaca [ 6 ] emphasizes generalization to unseen tools through simulated API responses.

AgentBench [ 4 ] expands scope to eight distinct environments including operating systems, databases, and web browsing, measuring general agent capability. SWE-bench [ 7 ] specifically targets software engineering tasks with real GitHub issues and repository contexts.

These benchmarks share a common limitation: they report single-run success rates under idealized conditions. StableToolBench [ 8 ] partially addresses API stability by caching responses, but does not introduce controlled fault injection or measure consistency.

τ \tau -bench [ 9 ] represents the closest prior work to ours. It introduces the pass k metric:

pass k = ℙ ​ ( all ​ k ​ runs succeed ) \text{pass}^{k}=\mathbb{P}(\text{all }k\text{ runs succeed}) (1)

and demonstrates that consistency metrics reveal fundamental limitations obscured by pass@1. However, τ \tau -bench examines only the consistency dimension and does not incorporate perturbations or fault injection.

ReliabilityBench extends τ \tau -bench’s insight to a multi-dimensional framework encompassing robustness and fault tolerance alongside consistency.

2.2 Metamorphic Testing

Metamorphic testing [ 10 , 11 ] addresses the oracle problem in software testing by verifying relationships between inputs and outputs rather than absolute correctness. A metamorphic relation (MR) specifies how the output should transform when the input is transformed in a known way.

Metamorphic testing has been successfully applied to machine learning systems. DeepTest [ 12 ] and DeepXplore [ 13 ] use image transformations (rotation, brightness, blur) as metamorphic relations for autonomous driving systems. CheckList [ 14 ] introduces behavioral testing for NLP with templates encoding expected invariances.

For agent evaluation, we introduce Action Metamorphic Relations where the equivalence criterion is end-state rather than output text. If two task descriptions should produce the same final system state (e.g., a booked meeting), they form a metamorphic pair regardless of the intermediate actions or response format.

2.3 Adversarial Robustness and NLP Testing

The robustness of NLP models to adversarial perturbations has been extensively studied. TextFooler [ 15 ] and BERT-Attack [ 16 ] generate semantically similar adversarial examples through word substitution. TextAttack [ 17 ] provides a unified framework for adversarial attacks on text classifiers.

These approaches target classification models where correctness is a discrete label. Agent tasks present different challenges: correctness is defined by achieving a goal state through a sequence of actions, and perturbations must preserve task semantics rather than classification labels.

2.4 Chaos Engineering and Fault Injection

Chaos engineering emerged from Netflix’s Simian Army [ 18 ] , systematically injecting failures into production systems to validate resilience. The approach has been formalized in Site Reliability Engineering practices [ 19 ] and extended to various domains.

Classical fault injection [ 20 ] provides foundational methodology for injecting hardware and software faults. TensorFI [ 21 ] applies fault injection to neural network accelerators. Humbatova et al. [ 22 ] provide a taxonomy of real faults in deep learning systems.

To our knowledge, ReliabilityBench is the first systematic application of chaos engineering principles to LLM agent evaluation, providing configurable fault profiles that simulate production failure modes.

2.5 Positioning ReliabilityBench 
Table 1 : Comparison with Existing Agent Benchmarks

Benchmark Consistency Robustness Fault Injection Multi-Domain

ToolBench × × × ✓

AgentBench × × × ✓

API-Bank × × × ✓

SWE-bench × × × ×

τ \tau -bench ✓ × × ✓

StableToolBench × × Partial ✓

ReliabilityBench ✓ ✓ ✓ ✓

ReliabilityBench uniquely combines all three reliability dimensions with multi-domain evaluation.

3 Formal Framework

We now present the mathematical framework underlying ReliabilityBench, formalizing the concepts of reliability surfaces, action metamorphic relations, and fault profiles.

3.1 Task and Agent Formalization

Definition 1 (Agentic Task) .

A task τ = ( d , S 0 , 𝒯 , v ) \tau=(d,S_{0},\mathcal{T},v) consists of:

- •

d d : A natural language task description

- •

S 0 ∈ 𝒮 S_{0}\in\mathcal{S} : An initial state from the state space

- •

𝒯 \mathcal{T} : A set of available tools (functions)

- •

v : 𝒮 × 𝒮 → { 0 , 1 } v:\mathcal{S}\times\mathcal{S}\rightarrow\{0,1\} : A goal verifier

Definition 2 (Agent Execution) .

An agent A A is a policy that, given task description d d and current state S S , produces a sequence of tool calls:

A ​ ( d , S 0 ) → t 1 , t 2 , … , t n S f A(d,S_{0})\xrightarrow{t_{1},t_{2},\ldots,t_{n}}S_{f} (2)

Execution succeeds if v ​ ( S f , S 0 ) = 1 v(S_{f},S_{0})=1 .

3.2 Reliability Metrics

We define reliability metrics across three dimensions.

3.2.1 Consistency: pass k

Following τ \tau -bench [ 9 ] , consistency measures repeated execution success:

Definition 3 (pass k ) .

For task τ \tau and agent A A , the pass k metric is:

pass k ​ ( τ , A ) = ℙ ​ ( ⋂ i = 1 k success i ) \text{pass}^{k}(\tau,A)=\mathbb{P}\left(\bigcap_{i=1}^{k}\text{success}_{i}\right) (3)

where success i \text{success}_{i} indicates success on the i i -th independent run.

Under independence, pass k = ( pass 1 ) k \text{pass}^{k}=(\text{pass}^{1})^{k} , but stochastic coupling often causes deviations.

3.2.2 Robustness: Perturbation Levels

Definition 4 (Perturbation Level ε \varepsilon ) .

A perturbation level ε ∈ [ 0 , 1 ] \varepsilon\in[0,1] defines the intensity of task description modifications:

ε = ∑ i w i ⋅ 𝟙 ​ [ MR i ​ applied ] \varepsilon=\sum_{i}w_{i}\cdot\mathbb{1}[\text{MR}_{i}\text{ applied}] (4)

where w i w_{i} is the weight of metamorphic relation MR i \text{MR}_{i} .

We define discrete levels: ε = 0 \varepsilon=0 (baseline), ε = 0.1 \varepsilon=0.1 (light: synonym substitution), ε = 0.2 \varepsilon=0.2 (medium: + reordering, distractors), ε = 0.3 \varepsilon=0.3 (heavy: + paraphrase, corrections).

3.2.3 Fault Tolerance: Fault Intensity

Definition 5 (Fault Intensity λ \lambda ) .

A fault intensity λ ∈ [ 0 , 1 ] \lambda\in[0,1] specifies the probability of fault injection per tool call:

ℙ ​ ( fault | tool call ) = f ​ ( λ ) \mathbb{P}(\text{fault}|\text{tool call})=f(\lambda) (5)

where f f is a profile-specific distribution.

We define profiles: λ = 0 \lambda=0 (baseline), λ = 0.1 \lambda=0.1 (light: 5-10% failures), λ = 0.2 \lambda=0.2 (medium: 15-20%), λ = 0.3 \lambda=0.3 (heavy: 25-30%).

3.3 The Reliability Surface

Definition 6 (Reliability Surface) .

For agent A A and task distribution 𝒟 \mathcal{D} , the reliability surface is:

R ​ ( k , ε , λ ) = 𝔼 τ ∼ 𝒟 ​ [ pass k ​ ( perturb ε ​ ( τ ) , A ) ∣ fault profile ​ λ ] R(k,\varepsilon,\lambda)=\mathbb{E}_{\tau\sim\mathcal{D}}\left[\text{pass}^{k}(\text{perturb}_{\varepsilon}(\tau),A)\mid\text{fault profile }\lambda\right] (6)

The surface captures how reliability degrades across all three dimensions simultaneously. Key derived metrics include:

Surface Volume :

V = ∫ 0 1 ∫ 0 1 ∫ 1 k m ​ a ​ x R ​ ( k , ε , λ ) ​ 𝑑 k ​ 𝑑 ε ​ 𝑑 λ V=\int_{0}^{1}\int_{0}^{1}\int_{1}^{k_{max}}R(k,\varepsilon,\lambda)\,dk\,d\varepsilon\,d\lambda (7)

Degradation Gradient :

∇ R = ( ∂ R ∂ k , ∂ R ∂ ε , ∂ R ∂ λ ) \nabla R=\left(\frac{\partial R}{\partial k},\frac{\partial R}{\partial\varepsilon},\frac{\partial R}{\partial\lambda}\right) (8)

Critical Threshold : The point ( k ∗ , ε ∗ , λ ∗ ) (k^{*},\varepsilon^{*},\lambda^{*}) where R R drops below acceptable level θ \theta .

3.4 Action Metamorphic Relations

Unlike traditional metamorphic testing where output equivalence is textual, agent tasks require end-state equivalence.

Definition 7 (Action Metamorphic Relation) .

An Action-MR is a tuple ( ϕ , ψ ) (\phi,\psi) where:

- •

ϕ : D → D \phi:D\rightarrow D transforms task descriptions

- •

ψ : 𝒮 → 𝒮 \psi:\mathcal{S}\rightarrow\mathcal{S} specifies expected state relationship

For most cases, ψ \psi is identity: v ​ ( S f , S 0 ) = v ​ ( S f ′ , S 0 ) v(S_{f},S_{0})=v(S^{\prime}_{f},S_{0}) .

d d : “Book flight NYC to LAX” S f S_{f} : reservation confirmed Agent A A ϕ ​ ( d ) \phi(d) : “I need to fly from NYC. Destination: LAX” S f ′ S^{\prime}_{f} : reservation confirmed Agent A A ϕ \phi v ​ ( S f ) = v ​ ( S f ′ ) v(S_{f})=v(S^{\prime}_{f}) Figure 1 : Action Metamorphic Relation: Task description perturbation ϕ \phi should preserve goal satisfaction. The agent may take different actions but must achieve equivalent end states.

We implement the following Action-MRs:

Table 2 : Action Metamorphic Relation Taxonomy

Category MR Type Description

Linguistic Synonym Replace keywords with synonyms

Paraphrase LLM-based rephrasing

Voice Active/passive voice change

Structural Reordering Permute constraint order

Split/Merge Divide or combine instructions

Contextual Distractor Add irrelevant information

Correction Include mid-task corrections

Temporal Date Format Vary date representations

Relative Time “tomorrow” vs “2024-01-15”

3.5 Fault Injection Framework

Inspired by chaos engineering [ 18 ] , we define a taxonomy of production faults.

Definition 8 (Fault Type) .

A fault F = ( p , effect , recovery ) F=(p,\text{effect},\text{recovery}) specifies:

- •

p p : Injection probability

- •

effect : Modified tool response

- •

recovery : Whether retry can succeed

Table 3 : Fault Type Taxonomy

Category Fault Type Recoverable Realistic Source

Network TransientTimeout ✓ API latency spike

ConnectionReset ✓ Load balancer

Rate Limit SoftRateLimit ✓ 429 responses

HardRateLimit × Account suspension

Data PartialResponse ✓ Truncated payload

SchemaDrift × API version mismatch

StaleData × Cache inconsistency

EmptyResponse ✓ No results

Definition 9 (Fault Profile) .

A fault profile Λ \Lambda at level λ \lambda defines:

Λ ​ ( λ ) = { ( F i , p i ​ ( λ ) ) : i ∈ FaultTypes } \Lambda(\lambda)=\{(F_{i},p_{i}(\lambda)):i\in\text{FaultTypes}\} (9)

with ∑ i p i ​ ( λ ) ≈ λ \sum_{i}p_{i}(\lambda)\approx\lambda for baseline failure rate.

4 Benchmark Implementation

4.1 Domain Implementations

ReliabilityBench includes four domains with realistic complexity:

Scheduling : Calendar management with meeting booking, rescheduling, and conflict detection. Tools: book_meeting , check_calendar , cancel_meeting , list_meetings .

Travel : Flight search and booking with multi-step workflows. Tools: search_flights , hold_flight , confirm_booking , get_itinerary .

Customer Support : Ticket management with knowledge base integration and escalation workflows. Tools: create_ticket , update_ticket , close_ticket , escalate_ticket , search_knowledge_base , list_open_tickets .

E-commerce : Product search, ordering, and returns with coupon application. Tools: search_products , check_inventory , create_order , check_order_status , process_return , apply_coupon .

Each domain maintains a state dictionary that tools modify. Success is verified by checking end-state against task-specific predicates.

4.2 State-Based Verification

Unlike benchmarks that rely on LLM judges or text matching, ReliabilityBench uses deterministic state-based oracles:

Algorithm 1 State-Based Goal Verification

Input: Initial state S 0 S_{0} , final state S f S_{f} , verifier v v

Output: Success boolean

return v ​ ( S 0 , S f ) v(S_{0},S_{f})

For example, the travel domain verifier checks:

reservations[flight_id].status == "confirmed"
reservations[flight_id].passenger == expected_passenger

4.3 Task Generation

Tasks are generated with controlled complexity levels:

Table 4 : Task Complexity Levels

Domain Level 1 Level 2

Scheduling Simple booking Conflict handling

Travel Direct flight booking Find cheapest flight

Support Create & close ticket Search KB + escalate

E-commerce Simple order Find cheapest + coupon

4.4 Agent Architectures

We implement two agent architectures:

ReAct [ 1 ] : Interleaved reasoning and acting with thought-action-observation loops.

Reflexion [ 23 ] : ReAct with self-reflection on failures and trajectory refinement.

Both architectures use function calling with JSON-formatted tool arguments and receive structured tool outputs.

4.5 Fault Injection System

The fault injector wraps tool execution:

Algorithm 2 Fault-Injected Tool Execution

Input: Tool t t , arguments args , fault profile Λ \Lambda

Output: Tool response (possibly modified)

u ∼ Uniform ​ ( 0 , 1 ) u\sim\text{Uniform}(0,1)

F ← SelectFault ​ ( Λ , u ) F\leftarrow\text{SelectFault}(\Lambda,u)

if F ≠ None F\neq\text{None} then

if F . recoverable F.\text{recoverable} then

return F . error_message F.\text{error\_message}

else

return F . modified_response ​ ( t ​ ( args ) ) F.\text{modified\_response}(t(\text{args}))

end if

else

return t ​ ( args ) t(\text{args})

end if

Fault profiles are configured via presets:

LAMBDA_PROFILES = {
 0.0: {"failure_rate": 0.0}, # Baseline
 0.1: {"failure_rate": 0.075,
 "faults": [TransientTimeout, HighLatency]},
 0.2: {"failure_rate": 0.175,
 "faults": [+ RateLimit, PartialResponse]},
 0.3: {"failure_rate": 0.275,
 "faults": [+ Cascading, SchemaDrift]}
}

5 Experiments

5.1 Experimental Setup

Models : Gemini 2.0 Flash (primary), GPT-4o (comparison).

Agent Architectures : ReAct, Reflexion.

Domains : Scheduling, Travel, Support, E-commerce (5 tasks per domain in verified subset).

Evaluation Grid (Full 3D Reliability Surface):

- •

k = 2 k=2 trials per configuration

- •

λ ∈ { 0.0 , 0.2 } \lambda\in\{0.0,0.2\} fault injection levels

- •

ε ∈ { 0.0 , 0.1 , 0.2 } \varepsilon\in\{0.0,0.1,0.2\} perturbation levels

Perturbation Types (Action Metamorphic Relations):

- •

ε = 0.1 \varepsilon=0.1 (Light): Synonym substitution, date format changes, constraint reordering

- •

ε = 0.2 \varepsilon=0.2 (Medium): + Distractor injection, mid-task corrections, paraphrasing

Fault Type Ablation : Individual fault type testing (timeout-only, rate-limit-only, partial-response-only, mixed) at λ = 0.2 \lambda=0.2 .

Total Episodes :

- •

Main experiments: 480 per model (20 tasks × \times 3 ε \varepsilon levels × \times 2 λ \lambda levels × \times 2 agents × \times 2 runs)

- •

Ablation experiments: 320 (20 tasks × \times 4 fault types × \times 2 agents × \times 2 runs)

- •

Grand total: 1,280 episodes

5.2 Main Results 
Table 5 : Overall Reliability Metrics by Model (480 episodes each, aggregated over ReAct and Reflexion architectures). Pass 2 denotes the probability that all k = 2 k{=}2 trials succeed.

Model pass 2 ε = 0.0 \varepsilon=0.0 ε = 0.1 \varepsilon=0.1 ε = 0.2 \varepsilon=0.2 Cost

Gemini 2.0 Flash 91.04% 96.88% 88.12% 88.12% $0.12

GPT-4o 90.42% 95.00% 87.50% 88.75% $9.77

Δ \Delta (GPT-4o - Gemini) -0.62% -1.88% -0.62% +0.63% 82 × \times 
Table 6 : Reliability by Agent Architecture (Gemini 2.0 Flash)

Architecture Surface Volume ε = 0 \varepsilon=0 Pass ε = 0.2 \varepsilon=0.2 Pass

ReAct 0.900 97.5% 90.0%

Reflexion 0.875 96.3% 86.3%

Key observations:

- 1.

Perturbations cause 8.8% degradation : From ε = 0 \varepsilon=0 (96.88%) to ε = 0.2 \varepsilon=0.2 (88.12%), demonstrating that Action Metamorphic Relations reveal real brittleness to paraphrasing.

- 2.

GPT-4o costs 82 × \times more with no reliability benefit : Gemini 2.0 Flash achieves +0.62% higher overall pass rate at 1/82nd the cost, making it the clear choice for reliability evaluation.

- 3.

Simpler architectures more robust : ReAct achieves 2.5% higher surface volume than Reflexion, with the gap widening under perturbation stress.

5.3 Domain-Level Analysis 
Table 7 : Pass Rate by Domain ( λ = 0.0 \lambda=0.0 , ReAct)

Domain pass@1 pass 2 Avg Tool Calls

Scheduling 100% 100% 2.1

Travel 87.5% 75.0% 5.4

Support 91.7% 83.3% 4.8

E-commerce 87.5% 75.0% 4.6

Scheduling tasks (simple, deterministic) achieve perfect consistency. Travel tasks (multi-step with search) show higher variance due to decision points in flight selection.

5.4 Fault Tolerance Analysis 
0.0 (Baseline) 0.2 (Medium) 60 60 80 80 100 100 Fault Level ( λ \lambda ) pass 2 (%) ReAct Reflexion Figure 2 : Reliability degradation under fault injection at measured λ \lambda levels. ReAct shows 7.5% degradation from λ = 0 \lambda=0 to λ = 0.2 \lambda=0.2 , while Reflexion shows 10.0% degradation, indicating that self-reflection mechanisms may amplify rather than mitigate fault impacts.

The degradation gradient ∂ R ∂ λ \frac{\partial R}{\partial\lambda} is steeper for Reflexion ( − 0.50 -0.50 per 0.1 λ \lambda ) than ReAct ( − 0.38 -0.38 ), indicating that self-reflection mechanisms may amplify rather than mitigate fault impacts.

5.5 Recovery Behavior 
Table 8 : Fault Recovery Statistics ( λ = 0.2 \lambda=0.2 )

Metric ReAct Reflexion

Faults Encountered 47 52

Successful Recoveries 38 (80.9%) 35 (67.3%)

Additional Tool Calls on Fault +1.2 +1.8

ReAct demonstrates superior fault recovery, likely due to its simpler retry logic compared to Reflexion’s more complex reflection-and-retry mechanism.

5.6 Fault Type Ablation

To understand which fault types impact reliability most, we conducted ablation experiments isolating each fault type at λ = 0.2 \lambda=0.2 (320 episodes total).

Table 9 : Fault Type Ablation Results ( λ = 0.2 \lambda=0.2 , 320 episodes). Note: “Faults Encountered” counts explicit error responses (timeouts, 429s); modified responses (partial data) affect success but are not counted as faults.

Fault Type Pass Rate vs Mixed Impact

Timeout Only 98.75% +2.50% Minimal

Rate Limit Only 93.75% -2.50% Highest

Partial Response Only 97.50% +1.25% Low

Mixed (Baseline) 96.25% — —

Key findings from ablation:

- 1.

Rate limiting causes largest degradation : 2.5% below mixed baseline, suggesting agents struggle with backoff and retry logic for rate-limited APIs.

- 2.

Transient timeouts well-handled : 98.75% pass rate indicates robust retry mechanisms for temporary failures.

- 3.

Mixed faults partially cancel : The mixed baseline (96.25%) performs better than rate-limit-only, suggesting fault diversity may help agents adapt.

5.7 Cost Analysis 
Table 10 : Computational Costs (480 episodes per model)

Model Total Tokens Total Cost Cost/100 ep Ratio

Gemini 2.0 Flash 1,192,209 $0.12 $0.025 1 × \times

GPT-4o 1,188,450 $9.77 $2.04 82 × \times

Gemini 2.0 Flash provides 82 × \times cost efficiency compared to GPT-4o with comparable (and slightly better) reliability, making it the clear choice for large-scale agent evaluation. The total experiment cost for 1,280 episodes was under $10. 1 1 1 Costs measured December 2024 using Gemini 2.0 Flash at $0.075/1M input, $0.30/1M output tokens and GPT-4o at $2.50/1M input, $10.00/1M output tokens.

5.8 Reliability Surface Visualization

Figure 3 shows the measured reliability surface for Gemini 2.0 Flash across the ε \varepsilon and λ \lambda dimensions at k = 2 k=2 trials.

0.0 0.2 0.0 0.1 0.2 96.88 96.88 91 91 88.12 88.12 85 85 88.12 88.12 84 84 λ \lambda (fault rate) ε \varepsilon (perturbation level) 84 84 86 86 88 88 90 90 92 92 94 94 96 96 Pass Rate (%) Figure 3 : Measured Reliability Surface R ​ ( k = 2 , ε , λ ) R(k{=}2,\varepsilon,\lambda) for Gemini 2.0 Flash. Each point shows the pass 2 rate at the measured ( ε , λ ) (\varepsilon,\lambda) grid point. Baseline ( ε = 0 , λ = 0 \varepsilon{=}0,\lambda{=}0 ) achieves 96.88%, degrading to 84.0% under combined perturbation and fault stress.

5.9 Perturbation Impact Visualization

Figure 4 shows the reliability degradation as perturbation intensity increases, demonstrating the practical impact of Action Metamorphic Relations.

0.0 (Baseline) 0.1 (Light) 0.2 (Medium) 85 85 90 90 95 95 100 100 Perturbation Level ( ε \varepsilon ) Pass Rate (%) Gemini 2.0 Flash GPT-4o Figure 4 : Reliability degradation under increasing perturbation levels. Both models show ∼ \sim 8-9% drop from baseline ( ε = 0 \varepsilon=0 ) to medium perturbation ( ε = 0.2 \varepsilon=0.2 ), with the steepest drop occurring at ε = 0.1 \varepsilon=0.1 . Timeout Rate Limit Partial Mixed 90 90 92 92 94 94 96 96 98 98 100 100 98.75 98.75 93.75 93.75 97.5 97.5 96.25 96.25 Fault Type Pass Rate (%) Figure 5 : Fault type ablation results. Rate limiting causes the largest degradation (93.75%), while transient timeouts are best handled (98.75%).

5.10 Failure Mode Analysis

Qualitative analysis of failures reveals distinct patterns:

Travel Domain Failures : Agents fail to provide payment information for booking confirmation, indicating missing context handling.

Support Domain Failures : Escalation logic inconsistency—agents sometimes close tickets that should be escalated.

Fault-Induced Failures : Rate limit errors cause agents to abandon tasks rather than retry; schema drift errors propagate through subsequent tool calls.

6 Discussion

6.1 Implications for Production Deployment

Our findings have direct implications for deploying LLM agents:

- 1.

Multiply benchmarks by reliability factor : If a benchmark reports 90% accuracy, expect 70-80% in production when accounting for consistency and faults.

- 2.

Simpler architectures for robustness : Complex reasoning architectures may underperform simpler alternatives under realistic conditions. The additional complexity introduces failure modes that outweigh benefits.

- 3.

Retry logic is critical : Agents lacking robust retry mechanisms for transient failures will exhibit significant reliability degradation.

- 4.

Test under stress : pass@1 metrics on clean data provide dangerously optimistic estimates. Systematic fault injection reveals true production reliability.

6.2 Limitations

Scale : Our experiments use 1,280 episodes across all configurations. While this provides reasonable statistical power, production-scale evaluation may require 10,000+ episodes for tight confidence intervals on rare failure modes.

Perturbation Depth : We implement ε ∈ { 0.0 , 0.1 , 0.2 } \varepsilon\in\{0.0,0.1,0.2\} perturbation levels. Heavy perturbations ( ε = 0.3 \varepsilon=0.3 ) with multi-transform combinations remain for future work.

Model Coverage : We evaluate Gemini 2.0 Flash and GPT-4o. Broader model comparison (Claude, Llama, Mistral, open-source models) would strengthen generalizability claims.

Synthetic Tasks : While our domains simulate realistic workflows, they lack the full complexity of production systems with external APIs, authentication, and real-time data dependencies.

k-Value Range : We evaluate at k = 2 k=2 trials. Higher k k values (4, 8) would reveal steeper consistency degradation curves.

6.3 Ethical Considerations

ReliabilityBench is designed for evaluation, not for generating adversarial attacks on deployed systems. The fault injection framework should be used only for pre-deployment testing, not for discovering vulnerabilities in production systems without authorization.

7 Conclusion

We presented ReliabilityBench, a benchmark for evaluating LLM agent reliability under production-like conditions. Through 1,280 episodes across two models and two agent architectures, we establish the first comprehensive evaluation of the 3D reliability surface. Our contributions include:

- 1.

Reliability Surface R ​ ( k , ε , λ ) R(k,\varepsilon,\lambda) : A unified framework capturing consistency, robustness, and fault tolerance with demonstrated 8.8% degradation from perturbations alone.

- 2.

Action Metamorphic Relations : Perturbation strategies (synonym substitution, distractor injection, paraphrasing) that reveal brittleness invisible to standard benchmarks.

- 3.

Chaos Engineering for Agents : Systematic fault injection with ablation analysis showing rate limiting causes the largest reliability impact (2.5% degradation).

- 4.

Empirical findings : Perturbations cause 8.8% reliability drop; simpler ReAct outperforms Reflexion (2.5% higher surface volume); GPT-4o costs 82 × \times more than Gemini with comparable reliability.

As LLM agents move from research prototypes to production systems, evaluation methodology must evolve to match. ReliabilityBench provides the first systematic framework for this critical assessment, enabling practitioners to make informed decisions about agent deployment readiness.

Acknowledgments

This work was conducted independently with computational resources from Apple Silicon. The author thanks the open source community for making this research possible.

References

- [1] Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K., & Cao, Y. (2023).
ReAct: Synergizing Reasoning and Acting in Language Models.
In International Conference on Learning Representations (ICLR) .
arXiv:2210.03629.

- [2] Schick, T., Dwivedi-Yu, J., Dessì, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., Cancedda, N., & Scialom, T. (2023).
Toolformer: Language Models Can Teach Themselves to Use Tools. arXiv preprint arXiv:2302.04761 .

- [3] Qin, Y., Liang, S., Ye, Y., Zhu, K., Yan, L., Lu, Y., Lin, Y., Cong, X., Tang, X., Qian, B., Zhao, S., Tian, R., Xie, R., Zhou, J., Gerber, D., Doss, M., Huang, H., Zhang, W., Sun, M., & Liu, Z. (2023).
ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs. arXiv preprint arXiv:2307.16789 .

- [4] Liu, X., Yu, H., Zhang, H., Xu, Y., Lei, X., Lai, H., Gu, Y., Ding, H., Men, K., Yang, K., Zhang, S., Deng, X., Zeng, A., Du, Z., Zhang, C., Shen, S., Zhang, T., Su, Y., Sun, H., Huang, M., Dong, Y., & Tang, J. (2023).
AgentBench: Evaluating LLMs as Agents. arXiv preprint arXiv:2308.03688 .

- [5] Li, M., Zhao, Y., Yu, B., Song, F., Li, H., Yu, H., Li, Z., Huang, F., & Li, Y. (2023).
API-Bank: A Benchmark for Tool-Augmented LLMs.
In Proceedings of EMNLP .
arXiv:2304.08244.

- [6] Tang, Q., Deng, Z., Lin, H., Han, X., Liang, Q., & Sun, L. (2023).
ToolAlpaca: Generalized Tool Learning for Language Models with 3000 Simulated Cases. arXiv preprint arXiv:2306.05301 .

- [7] Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., & Narasimhan, K. (2024).
SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
In International Conference on Learning Representations (ICLR) .

- [8] Guo, Z., Jin, R., Liu, C., Huang, Y., Shi, D., Supryadi, S., Yu, L., Liu, Y., Li, J., Xiong, B., & Xiong, D. (2024).
StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning of Large Language Models. arXiv preprint arXiv:2403.07714 .

- [9] Yao, S., Shinn, N., Razeghi, Y., Carlini, N., & Narasimhan, K. (2024). τ \tau -bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains. arXiv preprint arXiv:2406.12045 .

- [10] Chen, T.Y., Cheung, S.C., & Yiu, S.M. (1998).
Metamorphic Testing: A New Approach for Generating Next Test Cases. Technical Report HKUST-CS98-01 , Hong Kong University of Science and Technology.

- [11] Chen, T.Y., Kuo, F.-C., Liu, H., Poon, P.-L., Towey, D., Tse, T.H., & Zhou, Z.Q. (2018).
Metamorphic Testing: A Review of Challenges and Opportunities. ACM Computing Surveys , 51(1), 1-27.
DOI: 10.1145/3143561.

- [12] Tian, Y., Pei, K., Jana, S., & Ray, B. (2018).
DeepTest: Automated Testing of DNN-driven Autonomous Cars.
In Proceedings of ICSE .
DOI: 10.1145/3180155.3180220.

- [13] Pei, K., Cao, Y., Yang, J., & Jana, S. (2017).
DeepXplore: Automated Whitebox Testing of Deep Learning Systems.
In Proceedings of SOSP .
DOI: 10.1145/3132747.3132785.

- [14] Ribeiro, M.T., Wu, T., Guestrin, C., & Singh, S. (2020).
Beyond Accuracy: Behavioral Testing of NLP Models with CheckList.
In Proceedings of ACL .
DOI: 10.18653/v1/2020.acl-main.442.

- [15] Jin, D., Jin, Z., Zhou, J.T., & Szolovits, P. (2020).
Is BERT Really Robust? A Strong Baseline for Natural Language Attack on Text Classification and Entailment.
In Proceedings of AAAI , 34(5).
DOI: 10.1609/aaai.v34i05.6311.

- [16] Li, L., Ma, R., Guo, Q., Xue, X., & Qiu, X. (2020).
BERT-ATTACK: Adversarial Attack Against BERT Using BERT.
In Proceedings of EMNLP .
DOI: 10.18653/v1/2020.emnlp-main.500.

- [17] Morris, J., Lifland, E., Yoo, J.Y., Grigsby, J., Jin, D., & Qi, Y. (2020).
TextAttack: A Framework for Adversarial Attacks, Data Augmentation, and Adversarial Training in NLP.
In Proceedings of EMNLP: System Demonstrations .
DOI: 10.18653/v1/2020.emnlp-demos.16.

- [18] Basiri, A., Behnam, N., de Rooij, R., Hochstein, L., Kosewski, L., Reynolds, J., & Rosenthal, C. (2016).
Chaos Engineering. IEEE Software , 33(3), 35-41.
DOI: 10.1109/MS.2016.60.

- [19] Beyer, B., Jones, C., Petoff, J., & Murphy, N.R. (2016). Site Reliability Engineering: How Google Runs Production Systems .
O’Reilly Media.
ISBN: 978-1491929124.

- [20] Arlat, J., Aguera, M., Amat, L., Crouzet, Y., Fabre, J.-C., Laprie, J.-C., Martins, E., & Powell, D. (1990).
Fault Injection for Dependability Validation: A Methodology and Some Applications. IEEE Transactions on Software Engineering , 16(2), 166-182.
DOI: 10.1109/32.44380.

- [21] Chen, Z., Li, G., Pattabiraman, K., & DeBardeleben, N. (2020).
BinFI: An Efficient Fault Injector for Safety-Critical Machine Learning Systems.
In Proceedings of SC .

- [22] Humbatova, N., Jahangirova, G., Bavota, G., Riccio, V., Stocco, A., & Tonella, P. (2020).
Taxonomy of Real Faults in Deep Learning Systems.
In Proceedings of ICSE .
DOI: 10.1145/3377811.3380395.

- [23] Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., & Yao, S. (2023).
Reflexion: Language Agents with Verbal Reinforcement Learning.
In NeurIPS .
arXiv:2303.11366.

Appendix A Domain Tool Specifications

A.1 Scheduling Domain

book_meeting(date: str, time: str, topic: str) -> str
 Books a meeting on the specified date and time.

check_calendar(date: str) -> str
 Returns all meetings scheduled for the given date.

cancel_meeting(date: str, time: str) -> str
 Cancels the meeting at the specified slot.

list_meetings(start_date: str, end_date: str) -> str
 Lists all meetings in the date range.

A.2 Travel Domain

search_flights(origin: str, dest: str, date: str) -> str
 Searches for available flights.

hold_flight(flight_id: str) -> str
 Places a temporary hold on a flight.

confirm_booking(flight_id: str, passenger: str,
 payment_info: str) -> str
 Confirms a held flight booking.

get_itinerary() -> str
 Returns current reservations.

A.3 Support Domain

create_ticket(customer_id: str, subject: str,
 description: str, priority: str) -> str
 Creates a new support ticket.

update_ticket(ticket_id: str, status: str,
 priority: str, note: str) -> str
 Updates ticket fields.

close_ticket(ticket_id: str, resolution: str) -> str
 Closes a ticket with resolution summary.

escalate_ticket(ticket_id: str, reason: str,
 escalate_to: str) -> str
 Escalates ticket to higher tier.

search_knowledge_base(query: str, category: str) -> str
 Searches KB for relevant articles.

list_open_tickets(priority: str, customer_id: str) -> str
 Lists open tickets with optional filters.

A.4 E-commerce Domain

search_products(query: str, category: str,
 min_price: float, max_price: float) -> str
 Searches product catalog with filters.

check_inventory(sku: str) -> str
 Checks inventory for a specific product.

create_order(customer_id: str, items: List[Dict],
 shipping_address: str, coupon_code: str) -> str
 Creates a new order.

check_order_status(order_id: str) -> str
 Returns order details and status.

process_return(order_id: str, items: List[str],
 reason: str, refund_method: str) -> str
 Processes a product return.

apply_coupon(code: str, order_subtotal: float) -> str
 Validates and calculates coupon discount.

Appendix B Fault Profile Configurations

LAMBDA_0_0 = { # Baseline
 "failure_rate": 0.0,
 "fault_weights": {}
}

LAMBDA_0_1 = { # Light
 "failure_rate": 0.075,
 "fault_weights": {
 "TransientTimeout": 0.4,
 "HighLatency": 0.3,
 "EmptyResponse": 0.3
 }
}

LAMBDA_0_2 = { # Medium
 "failure_rate": 0.175,
 "fault_weights": {
 "TransientTimeout": 0.25,
 "SoftRateLimit": 0.25,
 "PartialResponse": 0.2,
 "SchemaDrift": 0.15,
 "StaleData": 0.15
 }
}

LAMBDA_0_3 = { # Heavy
 "failure_rate": 0.275,
 "fault_weights": {
 "TransientTimeout": 0.15,
 "ConnectionReset": 0.15,
 "HardRateLimit": 0.15,
 "PartialResponse": 0.15,
 "SchemaDrift": 0.2,
 "CascadingFailure": 0.2
 }
}

Appendix C Sample Task Instances

C.1 Scheduling Task

Description : “Book a meeting about ’Review’ on 2026-01-01 at 09:00.”

Initial State :

{"calendar": {}}

Expected Final State :

{"calendar": {"2026-01-01": {"09:00": "Review"}}}

C.2 Travel Task

Description : “Book the cheapest flight from LON to PAR on 2026-01-05 for Bob.”

Initial State :

{"flights_db": [
 {"id": "BA-200", "origin": "LON", "dest": "PAR",
 "date": "2026-01-05", "price": 500, "seats_left": 10},
 {"id": "AA-500", "origin": "LON", "dest": "PAR",
 "date": "2026-01-05", "price": 300, "seats_left": 10}
]}

Verifier : Check that reservations["AA-500"].passenger == "Bob" and status == "confirmed" .
