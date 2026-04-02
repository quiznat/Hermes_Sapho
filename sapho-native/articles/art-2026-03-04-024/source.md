---
version: source-capture.v1
article_id: art-2026-03-04-024
ticket_id: ticket-import-art-2026-03-04-024
source_url: https://arxiv.org/abs/2510.10460
canonical_url: https://arxiv.org/abs/2510.10460
source_title: Testing and Enhancing Multi-Agent Systems for Robust Code Generation
capture_kind: arxiv_html
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-30T17:59:36Z'
linked_paper_urls: []
---
# Source Capture

## Title

Testing and Enhancing Multi-Agent Systems for Robust Code Generation

## Body

Testing and Enhancing Multi-Agent Systems for Robust Code Generation

Zongyi Lyu 0009-0001-1600-4378 The Hong Kong University of Science and Technology Hong Kong China zlyuaj@connect.ust.hk , Songqiang Chen 0000-0002-1220-8728 The Hong Kong University of Science and Technology Hong Kong China i9s.chen@connect.ust.hk , Zhenlan Ji 0000-0003-3167-0480 The Hong Kong University of Science and Technology Hong Kong China zjiae@cse.ust.hk , Liwen Wang 0009-0001-7831-6983 The Hong Kong University of Science and Technology Hong Kong China lwanged@cse.ust.hk , Shuai Wang 0000-0002-0866-0308 The Hong Kong University of Science and Technology Hong Kong China shuaiw@cse.ust.hk , Daoyuan Wu 0000-0002-3752-0718 Lingnan University Hong Kong China daoyuanwu@ln.edu.hk , Wenxuan Wang 0000-0002-9803-8204 Renmin University of China Beijing China jwxwang@gmail.com and Shing-Chi Cheung 0000-0002-3508-7172 The Hong Kong University of Science and Technology Hong Kong China scc@cse.ust.hk

Abstract.

Multi-agent systems (MASs) have emerged as a promising paradigm for automated
code generation, demonstrating impressive performance on established benchmarks
by decomposing complex coding tasks across specialized agents with different
roles. Despite their prosperous development and adoption, their robustness
remains pressingly under-explored, raising critical concerns for real-world
deployment.
This paper presents the first comprehensive study examining the robustness
of MASs for code generation through a fuzzing-based testing approach. By
designing a fuzzing pipeline incorporating semantic-preserving mutation
operators and a novel fitness function, we assess mainstream MASs
across multiple datasets and LLMs. Our findings reveal substantial
robustness flaws of various popular MASs: they fail to solve 7.9%–83.3% of problems they
initially resolved successfully after applying the semantic-preserving
mutations.
Through comprehensive failure analysis, we identify a common yet largely
overlooked cause of the robustness issue: miscommunications between planning and coding agents,
where plans lack sufficient detail and coding agents misinterpret intricate logic,
aligning with the challenges inherent in a multi-stage information transformation process.
Accordingly, we also propose a repairing method that encompasses
multi-prompt generation and introduces a new monitor agent to address this issue.
Evaluation shows that our repairing method
effectively enhances the robustness of MASs by solving 40.0%–88.9% of identified
failures. Re-execution of the fuzzing process on the repaired MASs shows that the number of found failures
decreases up to 85.7%, demonstrating that repaired MASs exhibit superior robustness.
Our work uncovers critical robustness
flaws in MASs and provides effective mitigation strategies, contributing
essential insights for developing more reliable MASs for code generation.

multi-agent systems, code generation, robustness 
† † conference: The ACM International Conference on the Foundations of Software Engineering; 5-9 July, 2026; Montreal, Canada † † ccs: Software and its engineering Software testing and repairing † † ccs: Software and its engineering Robustness

1. Introduction

The advent of large language models (LLMs) has fundamentally transformed
code generation methodologies, enabling the automated production of code
snippets that fulfill user requirements expressed in natural
language (Jiang et al., 2024 ; Chen et al., 2024a ) . Among these methodologies,
multi-agent systems (MASs) have exhibited particular promise. Implemented
through the same backend LLM, MASs decompose complex coding tasks into
manageable sub-tasks and distribute them among specialized agents with
distinct roles (Dong et al., 2024 ; Hong et al., 2023 ; Zhang et al., 2024a ; Islam et al., 2024 ; M. A. Islam, M. E. Ali, and M. R. Parvez, 2025 ) . For instance, planning agents are responsible for
planning the whole coding logic, while coding
agents focus on implementing the code based on the coding logic. Through the
deployment of carefully crafted prompts and communication protocols, these
specialized agents collaborate effectively, yielding impressive results
across diverse coding challenges on the benchmark
datasets (Chen et al., 2021b ; Austin et al., 2021 ; Dong et al., 2025 ; Li et al., 2022 ; Yu et al., 2024b ) .

Despite the effectiveness of MASs for code generation across various
benchmarks, their robustness remains pressingly under-explored. The lack of
robustness in MASs can pose significant risks to real-world deployment.
For instance, when deployed in production environments, non-robust MASs may
generate inconsistent and incorrect code solutions, resulting in system
failures and increased debugging costs (Mastropaolo et al., 2023 ) .
Moreover, the robustness issue in MASs can be further exacerbated by the
inherent instability of LLMs and the variability of users’ natural language
input (Wang et al., 2025 ) .

To understand the robustness characteristics of MASs, this paper conducts the first study on the robustness of MASs for code generation using a fuzzing-based approach. Inspired by existing efforts in the community on AI model robustness testing (Wang et al., 2023b ; Mastropaolo et al., 2023 ; Chen et al., 2021a ; Iakusheva et al., 2023 ; Xie et al., 2022 ; Rehman and Srinivasan, 2023 ) , we design four semantic-preserving mutation
operators over the input questions of MASs. The fuzzing is guided by a fitness
function that evaluates the deviation of MAS-generated plans and codes to
provide feedback for mutation. Our fuzzing results reveal serious robustness flaws: three mainstream
MASs (Dong et al., 2024 ; Hong et al., 2023 ; Zhang et al., 2024a ) fail to solve 7.9%–83.3% of questions that they initially resolved
correctly.

Based on the fuzzing results, we summarize several key observations that depict the robustness
flaws in contemporary MASs. In particular,
we for the first time reveal that the communication gap between coding agents and planning agents (“planner-coder gap”) constitutes a major cause of MASs’ robustness
flaws, accounting for an overwhelming 75.3% of all failures. Specifically, planning agents tend to generate coding plans that are logically
correct but lack certain detailed explanations, and coding agents
are prone to misinterpretations of specific expressions and complex logic.
We uncover that this gap
significantly compromises communication and understanding
between agents.
Through our analysis, we identify five error patterns that characterize this gap,
revealing that the key to enhancing MAS robustness lies in bridging the planner-coder gap.

To address these issues, we propose a novel repairing method to enhance the robustness of MASs. As the first step, we present a novel formulation of the code generation paradigm of MASs and demonstrate that this multi-stage transformation process can introduce information loss and semantic drift across agent boundaries. To mitigate the information loss, our repairing method incorporates two primary components: multi-prompt generation and monitor agent insertion.
Multi-prompt generation is designed to diversify the expressions in original input questions and reduce the chance that MASs misunderstand specific expressions. Specifically, we implement additional mutations on input questions to generate diverse prompts, providing the system with potentially better-formulated expressions that can reduce misinterpretation during agent communication.
Moreover, we introduce a specialized monitor agent to bridge the
planner-coder gap. This agent serves as
an intermediary to mitigate the information loss between the planning agent and the coding agent, facilitating better coordination through two key
processes: a plan interpretation process that enhances the coding agent’s
comprehension by providing a detailed interpretation of received plans, and a
code check process, where the monitor agent reviews and validates the
alignment of the generated code to the interpreted plan.

We conduct extensive experiments to evaluate our repairing method across
three prominent MASs (Dong et al., 2024 ; Hong et al., 2023 ; Zhang et al., 2024a ) with three backend LLMs (Achiam et al., 2023 ; Zhu et al., 2024 ; OpenAI, 2022 ) on four datasets (Dong et al., 2025 ; Li et al., 2022 ; Yu et al., 2024b ) . Results demonstrate that our approach can repair 40.0%–88.9% of failures identified during fuzzing. We also re-execute the
fuzzing process on the repaired MASs and find that the number of failures decreases up to 85.7%, showing
that repaired MASs exhibit superior robustness. Additionally, ablation
studies demonstrate the necessity of both multi-prompt generation and monitor agent
insertion to mitigate different robustness shortcomings of MASs.
Overall, we summarize our contributions as follows:

- •

We advocate the first systematic study on the robustness of MASs for
code generation, focusing on the impact of semantically equivalent requirements on MAS performance. Our fuzzing-based testing approach
incorporates semantic-preserving mutations and a well-designed fitness
function to effectively assess mainstream MASs. We summarize key findings
on the ill-robustness of current MASs in this domain.

- •

For the first time, we identify a major cause of robustness issues in MASs: the
“planner-coder gap,” which compromises communication and understanding between agents.
From our observation, we analyze the semantic drift across agent boundaries and formulate the code generation paradigm of MASs.
Accordingly, we propose a novel repairing method, which encompasses multi-prompt generation and a new monitor agent, to mitigate the planner-coder gap.

- •

We conduct comprehensive experiments validating our repairing method,
demonstrating its effectiveness in augmenting the robustness of MASs to a
large extent.

2. Background

Code generation has been a central focus of software engineering research,
aiming to automate programming tasks and enhance developer productivity by
generating desired code from natural language
specifications (Chen et al., 2022 ; Shin and Nam, 2021 ; Dehaerne et al., 2022 ; Chen et al., 2025 ; Cao et al., 2024 ; Du et al., 2024 ; Mathews and Nagappan, 2024 ; Gao et al., 2024 ) .
MASs are artificial intelligence systems that leverage LLMs as their core
computational engines to simulate domain experts with specialized
capabilities (Qian et al., 2023 ; Park et al., 2023 ; Xu et al., 2023 ) . With advances in prompt engineering (Liu et al., 2023 ) ,
developing MASs to enhance code generation has emerged as a prominent
research direction (He et al., 2024 ; Liu et al., 2024 ; Tran et al., 2025 ) .

A prevalent multi-agent approach to code generation employs role specialization
and iterative feedback mechanisms to provide code snippets that satisfy the user input (Liu et al., 2024 ) . As shown in Fig. 1 , the
typical architecture for code generation MASs consists of three primary parts:
planning, coding, and feedback-driven refinement, which are typically implemented through planner, coder, and tester (He et al., 2024 ) .

Figure 1. Pipeline of MASs for code generation.

Fig. 1 depicts a typical workflow of a code generation MAS.
Upon receiving a natural language requirement, the system routes the input to
the planning agent (planner) to generate a clear and correct coding plan. Note that the planning agent does not simply
paraphrase the user input. Instead, it serves as an important coding step that decomposes the coding problem
into a set of requirements and designs several key logical steps to solve the problem,
which determines the algorithm and the logic for code
implementation (Zhang et al., 2024a ; Dong et al., 2024 ) .
The coding agent (coder) then implements the solution following the
provided plan. Subsequently, the testing agent (tester) automatically generates test
cases and evaluates the implementation, producing a test report. If the code
fails, the report is returned to the coder for iterative refinement until the
solution passes all tests or the computational budget is exhausted.

This specialized multi-agent workflow represents a fundamental paradigm shift from single-LLM code generation approaches. Unlike the end-to-end paradigm where a unified model directly transforms natural language into
executable code (Chen et al., 2021b ; Wang et al., 2021 ; Fried et al., 2023 ; Nijkamp et al., 2022 ) , MASs decompose the complex task into specialized subtasks handled by domain-specific agents.
This paradigm demonstrates remarkable advantages in handling complex coding tasks. Nevertheless, our implication in Sec. 5 reveals critical
robustness issues concerning the interaction between planner and coder.

3. Motivation

MASs (Hong et al., 2023 ; Dong et al., 2024 ; Zhang et al., 2024a ; Huang et al., 2023 ; Zhang et al., 2024b ; Ishibashi and Nishimura, 2024 ) have emerged as
a transformative technology with immense commercial potential. IT
companies have put much effort into the development of MASs, with Google Cloud
announcing comprehensive enhancements to Vertex AI that include the Agent
Development Kit (ADK) and Agent Engine for building and deploying
enterprise-grade MASs at scale (clo, 2025 ) . OpenAI has also
launched new APIs and tools specifically designed for agentic applications,
including the Responses API and the Agents SDK for orchestrating
multi-agent workflows, demonstrating growing commercial interest in
MASs (ope, 2025 ) .

However, assessing the reliability and robustness of these complex systems
remains a blank. Unlike single agents and individual models, MASs involve intricate
inter-agent communications, dynamic role assignments, and collaborative
decision-making processes that make their behavior difficult to predict and
evaluate systematically (He et al., 2024 ) . This gap in assessment capabilities becomes
particularly concerning given the high-stakes commercial
applications these systems are designed to serve (Hong et al., 2023 ) .
Inspired by previous work that employs
testing to assess the robustness of AI
systems (Li et al., 2023 ; Mastropaolo et al., 2023 ; Xie et al., 2022 ) ,
we propose a new way to gauge the robustness of MASs for code generation
based on the semantically equivalent input mutations.
In particular, we presume that a robust MAS should sustain the consistency
when addressing semantically equivalent input and generating correct programs
regardless of how developers articulate their requirements.
This idea stems from the observation that developers’ requests typically
vary in vocabulary and phrasing due to the variability of natural
language.

To illustrate this idea, consider a simple example where a developer might
request: (1) “return n-th Fibonacci number,” (2) “give back the n-th number
in the Fibonacci sequence.” Although these requests use different phrasing,
their semantic meaning is identical. A robust MAS should generate functionally
correct solutions for both expressions. However, we find that even the
state-of-the-art MASs suffer from
inconsistencies in handling such semantically equivalent expressions. For example, PairCoder (Zhang et al., 2024a ) generates correct code for the first request, while failing on the second due to incorrect edge case handling.

4. Fuzzing MAS with Semantically Equivalent Requirements

To fill the blank in understanding of MAS’s robustness in code generation as discussed in Sec. 3 , in this work, we conduct the first fuzz testing with a framework specifically designed for MASs. Our approach systematically generates
semantically equivalent variations of programming requirements, exhaustively
testing MASs’ ability to handle diverse expressions of the same requirement (coding
problem), with the goal of comprehending the robustness of MASs.
In particular, this fuzzing framework is specifically designed to expose robustness flaws arising from the unique
inter-agent communication issues in MASs using a
dual-component fitness function, which,
for the first time, assesses the impact of mutations on both the final code
output and the intermediate planning artifacts.
This section elaborates on the design of this fuzzing methodology, the setup of fuzzing experiments, and the fuzzing results.

4.1. Fuzzing Methodology

We first present four semantic-preserving mutation operators that generate
alternative expressions of selected questions. Then, we introduce a fitness
function that calculates rewards based on the differences in both output code
and generated plans between the original and mutated questions, to provide
comprehensive guidance for subsequent fuzzing iterations.

Mutation Operators. Our mutation approach focuses on generating diverse expressions while preserving
the semantic meaning of input questions. To achieve this, we design four sentence-level
mutation operators that modify the expression styles of natural language requirements without altering the original
semantic content.

Table 1. Semantic-preserving mutation operators and description.

Operator Description Rephrase Instruct an LLM to rewrite a sentence using other words while maintaining the overall meaning. Insert Prompt an LLM to append one additional sentence at the end of the description based on the semantic content. Expand Use an LLM to expand one sentence into two by distributing its semantic content. Condense Apply an LLM to condense two consecutive sentences into one sentence using appropriate conjunctions.

Table 1 presents these four mutation operators: Rephrase , Insert , Expand , and Condense . We implement these
operators using GPT-4o (Achiam et al., 2023 ) , a state-of-the-art LLM, through
carefully designed prompts (available in our artifact 1 1 1 https://github.com/anonymous-for-submit/MAS_testing_repairing/tree/main/More_results/Mutation_opertors ).
Our approach effectively addresses two key challenges from previous
work (Wang et al., 2023b ; Mastropaolo et al., 2023 ) : (1) it avoids semantic
deviations that may occur during mutation, and (2) it produces natural and
fluent expressions in the mutated questions.

Following Yu et al. (Yu et al., 2024a ) , our operators cover prevalent
semantic-preserving transformations, providing comprehensive coverage of semantic
variations. Their preliminary work (Yu et al., 2024a ) demonstrates that
LLM-generated mutations effectively simulate diverse human expressions. Our
manual verification confirms that the mutated questions produced by our
operators maintain consistent human linguistic patterns while preserving the
original semantics, making them suitable for testing the robustness of
MASs.

Fitness Function. To determine whether a mutated question should be retained in the seed pool
for further mutation, we propose a novel fitness function that calculates
rewards for MAS outputs on mutated questions. Unlike previous coverage-driven fuzzing
approaches (Zalewski, 2025 ; Böhme et al., 2016 ; Ognawala et al., 2018 ; Veggalam et al., 2016 ) on software,
our fitness function considers the
multi-agent nature of MASs by comparing the output quality between the seed
questions and their mutated variants across two distinct aspects: code
and plan.

Code Reward. To mitigate the occasional failure
due to randomness rather than underlying robustness issues,
we execute MASs for n n times for each question.
We collect the generated code and calculate the rate of
completions passing all test cases provided in the dataset.
Based on the insight that an increasing number of failure trials on the mutated
questions indicate degraded MAS
performance (Wang et al., 2023a ; Chen et al., 2021b ) , we calculate the code
reward by measuring the difference between the pass rates of code generated
from original versus mutated questions:

(1) ℛ C = 1 n ​ ( ∑ i = 1 n c i − ∑ i = 1 n c ^ i ) \mathcal{R}_{C}=\frac{1}{n}\left(\sum_{i=1}^{n}c_{i}-\sum_{i=1}^{n}\hat{c}_{i}\right)

where n n represents the number of attempts, c i c_{i} and c ^ i \hat{c}_{i} indicates whether the i i -th generation passes the test (1 for pass, 0 for
fail). Positive rewards indicate that the mutated question reduces MAS
performance, making it valuable for identifying robustness issues
in subsequent fuzzing processes.

Plan Reward. Apart from the generated code, we also compare the semantic
of plans generated by the planning agent for the original and mutated
questions. Significant changes in the generated plans often indicate potential
robustness issues in the planning phase, which frequently make substantial
influence over the coding agent’s ability and the final code quality. We apply
Sentence-BERT (Reimers and Gurevych, 2019 ) to obtain the embedding and calculate
semantic similarity between corresponding plans. The plan reward is computed by
subtracting the normalized similarity from 1:

(2) ℛ P = 1 n ​ ∑ i = 1 n ( 1 − p ^ i ⋅ p i ‖ p ^ i ‖ ⋅ ‖ p i ‖ ) \mathcal{R}_{P}=\frac{1}{n}\sum_{i=1}^{n}\left(1-\frac{\hat{p}_{i}\cdot p_{i}}{||\hat{p}_{i}||\cdot||p_{i}||}\right)

where p i p_{i} and p ^ i \hat{p}_{i} represent the vector embeddings of plans
generated from the seed question and the mutated question, respectively, for
the i i -th generation.

The final fitness function is calculated as the sum of the code reward and the plan
reward.

Input: Multi-Agent System M M , Seed Pool 𝒮 \mathcal{S} , Mutation Operators 𝒪 \mathcal{O} , Fitness Function ℱ \mathcal{F} , Budget ℬ \mathcal{B} , Attempts n n

1

Output: Failure Questions Set ℛ \mathcal{R}

2

3 ℛ ← ∅ \mathcal{R}\leftarrow\emptyset ;

4 C ​ o ​ n ​ s ​ u ​ m ​ e ​ d ​ Q ​ u ​ e ​ r ​ i ​ e ​ s ← 0 ConsumedQueries\leftarrow 0 ;

5

6 while C ​ o ​ n ​ s ​ u ​ m ​ e ​ d ​ Q ​ u ​ e ​ r ​ i ​ e ​ s < ℬ ConsumedQueries<\mathcal{B} and 𝒮 ≠ ∅ \mathcal{S}\neq\emptyset do

7 s ​ e ​ e ​ d ← MCTS-exploring ​ ( 𝒮 ) seed\leftarrow\text{MCTS-exploring}(\mathcal{S}) ;

8 if s ​ e ​ e ​ d = null seed=\text{null} then

break; // No valid seed for mutation

9

o ​ p ​ e ​ r ​ a ​ t ​ o ​ r ← RandomlySelect ​ ( 𝒪 ) ; operator\leftarrow\text{RandomlySelect}(\mathcal{O}); // Randomly select one from four proposed mutation operators

m ​ u ​ t ​ a ​ t ​ e ​ d ​ _ ​ s ​ e ​ e ​ d ← o ​ p ​ e ​ r ​ a ​ t ​ o ​ r ​ ( s ​ e ​ e ​ d ) ; mutated\_seed\leftarrow operator(seed); // Apply LLM to mutate the seed question

10

11 f ​ a ​ i ​ l ​ u ​ r ​ e ​ s ← 0 failures\leftarrow 0 ;

12 for i = 1 i=1 to n n do

r ​ e ​ s ​ u ​ l ​ t ← Execute ​ ( M , m ​ u ​ t ​ a ​ t ​ e ​ d ​ _ ​ s ​ e ​ e ​ d ) ; result\leftarrow\text{Execute}(M,mutated\_seed); // Execute the MAS with the mutated seed

13 C ​ o ​ n ​ s ​ u ​ m ​ e ​ d ​ Q ​ u ​ e ​ r ​ i ​ e ​ s ← C ​ o ​ n ​ s ​ u ​ m ​ e ​ d ​ Q ​ u ​ e ​ r ​ i ​ e ​ s + 1 ConsumedQueries\leftarrow ConsumedQueries+1 ;

14 if FailOnTest( r ​ e ​ s ​ u ​ l ​ t result ) then

15 f ​ a ​ i ​ l ​ u ​ r ​ e ​ s ← f ​ a ​ i ​ l ​ u ​ r ​ e ​ s + 1 failures\leftarrow failures+1 ;

16

17

18

19 if f ​ a ​ i ​ l ​ u ​ r ​ e ​ s = n failures=n then

ℛ ← ℛ ∪ { m ​ u ​ t ​ a ​ t ​ e ​ d ​ _ ​ s ​ e ​ e ​ d } ; \mathcal{R}\leftarrow\mathcal{R}\cup\{mutated\_seed\}; // Add the mutated seed to the failure set

o ​ r ​ i ​ g ​ i ​ n ​ a ​ l ​ _ ​ s ​ e ​ e ​ d ← GetParent ​ ( s ​ e ​ e ​ d ) ; original\_seed\leftarrow\text{GetParent}(seed); // Get the original seed question

𝒮 ← 𝒮 ∖ { o ​ r ​ i ​ g ​ i ​ n ​ a ​ l ​ _ ​ s ​ e ​ e ​ d } ; \mathcal{S}\leftarrow\mathcal{S}\setminus\{original\_seed\}; // Stop fuzzing on this branch

20

21 else

r ​ e ​ w ​ a ​ r ​ d ← ℱ ​ ( r ​ e ​ s ​ u ​ l ​ t ) ; reward\leftarrow\mathcal{F}(result); // Use the fitness function to get the reward

22 if r ​ e ​ w ​ a ​ r ​ d > 0 reward>0 then

𝒮 ← 𝒮 ∪ { m ​ u ​ t ​ a ​ t ​ e ​ d ​ _ ​ s ​ e ​ e ​ d } ; \mathcal{S}\leftarrow\mathcal{S}\cup\{mutated\_seed\}; // Add the mutated seed to the seed pool

23

24

25

return ℛ \mathcal{R}

Algorithm 1 Fuzzing Pipeline

Fuzzing Pipeline. Following prior fuzzing
methodologies (Fioraldi et al., 2022 ; Zalewski, 2025 ) , our approach
encompasses four major components: seed pool initialization, seed
selection, mutation, and execution.  
The workflow of our fuzzing process is presented in Alg. 1 .
The algorithm takes the target MAS ℳ \mathcal{M} , seed pool 𝒮 , \mathcal{S}, mutation operates set 𝒪 \mathcal{O} , fitness function ℱ \mathcal{F} ,
fuzzing budget ℬ \mathcal{B} and total attempts n n as inputs, and output failure question set ℛ \mathcal{R} .
Specifically, we first create an initial seed pool from questions in
established datasets that the target MAS successfully resolves. For
each fuzzing iteration, following recent advances in fuzzing
methodologies (Yu et al., 2024a ) , we employ
MCTS-exploring (Yu et al., 2024a ) as our seed selection mechanism (line
4), which effectively identifies promising seeds while avoiding local
optima. Once a seed is selected, we randomly choose one of our four
semantic-preserving mutation operators to generate a semantically
equivalent version of the question (lines 7–8). Subsequently, the
mutated question is submitted to the MAS, which executes the code
generation process n n times (where n = 10 n=10 in our implementation) and
records the failure numbers and consumed queries (lines 10–14). If the
MAS fails to correctly solve the mutated question in all trials, we
identify this as an unsolvable variant and halt further fuzzing on that
branch (lines 15–18). If the MAS successfully handles the mutated
question, we calculate the reward using our fitness function to
determine whether to retain the mutation for further exploration (lines
20–22). We continue the above process until we reach predefined
resource constraints or exhaust valid seeds for mutation.

4.2. Experiment Setup

MASs. We evaluate three widely-adopted code generation MASs:
Self-Collaboration Code Generation (Dong et al., 2024 ) (SCCG in short),
MetaGPT (Hong et al., 2023 ) , and PairCoder (Zhang et al., 2024a ) . All
systems incorporate agents responsible for planning and coding. MetaGPT
represents one of the earliest MAS frameworks, applying five agents to
collaboratively develop software based on user instructions. SCCG first proposes the workflow of planning, coding and
testing, building a popular framework for many subsequent works (Zhang et al., 2024a ; Huang et al., 2023 ; Islam et al., 2024 ) . PairCoder is the state-of-the-art MAS that includes plan selection.

Backend LLMs. MASs employ the same backend LLM for all constituent agents. We use three
different LLMs as backend models for the aforementioned MASs:
GPT-3.5-Turbo (OpenAI, 2022 ) (GPT-3.5 in short),
GPT-4o (Achiam et al., 2023 ) , and Deepseek-Coder-V2 (Zhu et al., 2024 ) (Deepseek in short). All these LLMs are widely adopted and demonstrate
strong capabilities in code
generation (Joel et al., 2024 ; Zheng et al., 2024 ; Dai et al., 2025 ; Fakhoury et al., 2024 ; Guo et al., 2024 ; Jiang et al., 2023 , 2024 ) .
We apply the same parameters for the backend LLMs as the original MAS
papers (Dong et al., 2024 ; Hong et al., 2023 ; Zhang et al., 2024a ) ..

Datasets. We employ four code generation datasets: HumanEval
ET (Dong et al., 2025 ) , MBPP ET (Dong et al., 2025 ) ,
CodeContest (Li et al., 2022 ) and CoderEval (Yu et al., 2024b ) , which
are widely used for benchmarking MASs for code
generation (Dong et al., 2024 ; Lin et al., 2024 ) . HumanEval and MBPP (Dong et al., 2025 ) are commonly used datasets that
provide well-constructed coding problems along with test cases,
serving as standard benchmarks for code generation MASs.
CodeContest (Li et al., 2022 ) represents competitive programming
scenarios, offering more challenging problems. Notably, CoderEval (Yu et al., 2024b ) is one of the latest datasets that mirrors real-world development settings with data directly sourced from actual GitHub repositories, thereby offering a modern and realistic assessment of MASs.
These datasets, ranging from classical benchmarks to cutting-edge real-world scenarios, are chosen to evaluate the robustness of MASs across various coding contexts.

Dataset Splitting. It is important to note that we apply 50% of
the data in each dataset for fuzzing, and the rest for repairing (see
Sec. 6 ). In other words, this strictly prohibits using the same
data for both fuzzing and repairing in order to avoid data leakage. We use the
sanitized version of MBPP ET, the test set of CodeContest, and
the standalone-level of CoderEval to save resources.

Evaluation Metric. We adopt
Pass@ k (Chen et al., 2021b ) as our primary metric to
comprehensively assess MAS robustness. Following previous
works (Nijkamp et al., 2022 ; Chen et al., 2021b ; Li et al., 2022 ) , we
set k = 10 k=10 in our evaluation. Compared to Pass@1, Pass@10 mitigates the
influence of occasional failures due to randomness and can reflect more nuanced performance
differences among MASs. To measure Pass@10, we execute the system 10 times
( n = 10 n=10 ). If the MAS fails in all 10 trials, we consider the problem
unsolvable by the MAS.

Fuzzing Parameters. As mentioned in Sec. 4.1 ,
we use GPT-4o (Achiam et al., 2023 ) to generate
semantically equivalent mutations of seed questions.
Compared to alternative LLMs, GPT-4o demonstrates superior
reliability in generating equivalent expressions while preserving
semantic content. We set the query budget of our fuzzing method to 10,000.
For the MCTS-Explore algorithm, we apply identical parameter settings
as specified in (Yu et al., 2024a ) . To prevent local optima,
after a question is selected 15 times, we terminate fuzzing on the branch.

4.3. Fuzzing Results 
Table 2. Performance comparison on the original performance and performace after fuzzing.

MAS Backend LLM HumanEval ET MBPP ET CodeContest CoderEval

Fuzzing Original Drop Fuzzing Original Drop Fuzzing Original Drop Fuzzing Original Drop

SCCG GPT-3.5 0.4815 0.7160 ↓ \downarrow 32.6% 0.4590 0.5995 ↓ \downarrow 23.4% 0.0364 0.1091 ↓ \downarrow 66.7% 0.2540 0.4286 ↓ \downarrow 40.7%

GPT-4o 0.6975 0.8395 ↓ \downarrow 16.9% 0.5761 0.6909 ↓ \downarrow 16.6% 0.2121 0.3394 ↓ \downarrow 37.5% 0.3016 0.4921 ↓ \downarrow 38.7%

Deepseek 0.5617 0.7345 ↓ \downarrow 23.5% 0.4964 0.6440 ↓ \downarrow 22.9% 0.0242 0.0970 ↓ \downarrow 75.0% 0.1429 0.3810 ↓ \downarrow 62.5%

MetaGPT GPT-3.5 0.4085 0.7073 ↓ \downarrow 42.2% 0.5761 0.6651 ↓ \downarrow 13.4% 0.0242 0.0788 ↓ \downarrow 69.2% 0.3016 0.4127 ↓ \downarrow 26.9%

GPT-4o 0.6707 0.8170 ↓ \downarrow 17.9% 0.6089 0.6979 ↓ \downarrow 12.8% 0.1879 0.3091 ↓ \downarrow 39.2% 0.3333 0.4603 ↓ \downarrow 27.6%

Deepseek 0.5915 0.7378 ↓ \downarrow 19.8% 0.5972 0.6812 ↓ \downarrow 12.9% 0.0242 0.1515 ↓ \downarrow 83.3% 0.2540 0.3968 ↓ \downarrow 36.0%

PairCoder GPT-3.5 0.6829 0.7744 ↓ \downarrow 11.8% 0.6721 0.7307 ↓ \downarrow 8.0% 0.1030 0.2364 ↓ \downarrow 43.6% 0.0952 0.4127 ↓ \downarrow 76.0%

GPT-4o 0.7622 0.8475 ↓ \downarrow 10.1% 0.6791 0.7377 ↓ \downarrow 7.9% 0.4424 0.5273 ↓ \downarrow 16.1% 0.1587 0.4762 ↓ \downarrow 66.7%

Deepseek 0.7683 0.8536 ↓ \downarrow 10.0% 0.6417 0.7025 ↓ \downarrow 8.7% 0.1576 0.2788 ↓ \downarrow 43.5% 0.2698 0.4603 ↓ \downarrow 41.4%

Table 2 presents the performance differences of MASs
before and after fuzzing. The Drop represents the decrease rate of
pass@10 after fuzzing. Our results reveal that all MASs with
different backend LLMs experience performance degradation, with pass@10
decreases 7.9%– 83.3%. Specifically, SCCG (GPT-3.5) on CodeContest
demonstrates the highest accuracy drop, while PairCoder (GPT-4o) on MBPP-ET
exhibits the best robustness. These findings demonstrate that current MASs
suffer from robustness issues when confronted with semantically equivalent
questions, despite achieving promising results on original datasets.

Our fuzzing results reveal that different MASs exhibit varying degrees of robustness issues.
PairCoder consistently demonstrates the best robustness across most datasets,
while SCCG and MetaGPT show more severe performance degradation.
For instance, when using GPT-3.5 as the backend LLM on HumanEval ET,
PairCoder’s performance drops by only 11.8%, whereas SCCG and MetaGPT
experience over 30% decline. The superior robustness of PairCoder can be
attributed to its navigator agent that generates and selects optimal plans
from multiple candidates.
However, PairCoder’s advantage diminishes on CoderEval, where it
suffers the largest performance drop due to its heavy reliance on public
test cases for iterative code refinement, which CoderEval does not provide.
Meanwhile, MetaGPT shows better robustness on MBPP ET
and CoderEval, which contain shorter questions with minimal
explanations, aligning with MetaGPT’s design philosophy of processing brief user requirements.
These findings suggest that plan selection mechanisms and dataset characteristics
may influence MAS robustness.

We also notice that MASs exhibit more severe robustness issues when dealing with
longer and more complex questions. Among the four datasets analyzed, CodeContest and CoderEval show a larger
performance decline compared to HumanEval ET and MBPP ET. The questions in CodeContest are derived from programming
competitions and feature longer problem descriptions along with stricter input format requirements. While CoderEval mostly contains shorter questions, they involve more complex
problem settings that reflect real-world scenarios. Our results indicate that MASs struggle more with these complex
questions, where even slight mutations can cause failures. This suggests that MASs may encounter robustness issues
in real-world applications.

Furthermore, we observe that the capability
of the backend LLM affects MAS robustness, with more powerful LLMs
demonstrating superior robustness. Across all datasets, MASs with GPT-3.5
suffer sharper performance drops compared to those using GPT-4o.
This may be because weaker backend LLMs have limited capability in
precisely comprehending the semantics of different expressions, making them
more susceptible to robustness issues compared to stronger ones.

Our Findings: Existing MASs generally suffer from robustness
issues, manifesting a substantial performance drop when
processing semantically equivalent questions. This problem is
further exacerbated by longer and more complex questions, but can be
mitigated by using more powerful backend LLMs. Furthermore, our
results reveal that plan selection and refinement mechanisms may
enhance MAS robustness, indicating a potential direction to improve
MAS design.

5. Implications from Failure Cases

By observing many failure cases uncovered through our fuzzing approach, we further analyze the underlying reasons
for these failures to understand the robustness issues in MASs. Specifically, we randomly sample 20% of over 700
failures discovered through fuzzing and manually examine the generated code and internal outputs like plans to
comprehensively investigate the failure cases identified during the fuzzing process.
To mitigate
the effects of subjectivity, we invite two software developers to categorize the failure reasons and conduct cross-validation independently.
Following Pan et al. (Pan et al., 2025 ) , we employ Cohen’s Kappa
score (McHugh, 2012 ) to measure the agreement between the two
experts. In our case, the score is 0.88, indicating a high level of
agreement.

Table 3. Distribution of reasons for failures.

Category #Failure Percentage

Planner-Coder Gap 113 75.3%

Plan Logic Errors 23 15.3%

Invalid 14 9.3%

Our analysis reveals a surprising finding: in most failure cases, the
semantics of the generated plans maintained logical correctness; however, coding agents typically fail to properly
implement the correct code from these plans, and testing agents cannot
successfully rectify the issues, suggesting a substantial gap between coders and
planners. Our analysis indicates that this gap constitutes the primary
cause of most failure cases. As presented in
Table 3 , this substantial gap between planners
and coders constitutes the primary cause of failures, accounting for 75.3%
of all failure cases. In contrast, plan logic errors account for only 15.3%
of failures, and a small proportion of failures (9.3%) are categorized as invalid cases because
the requirements of these cases are ambiguous, leading to semantic changes after mutation.

This finding reveals an additional dimension beyond the prevailing focus in existing research. While
preliminary studies (Dong et al., 2024 ; Zhang et al., 2024a ; Hong et al., 2023 ) have
established that planning constitutes a critical coding step determining
implementation logic and that effective inter-agent communication is essential
for correct plan implementation, most of them have concentrated primarily on choosing the right algorithm and generating plans without logical flaws. Our analysis, however, demonstrates that even with
logically correct plans, the gap between planner and coder (“planner-coder gap”) emerges as a fundamental impediment to robust code
generation in MASs. This gap significantly compromises communication and
understanding between agents, thereby undermining the overall robustness of
MASs and substantially limiting their coding capabilities.

Through comprehensive analysis, we identify two principal underlying causes of this gap: 1) although the plan is logically correct, it
is typically brief and abstract, and may not clarify certain concepts and
conditions for coders; 2) coders are vulnerable to certain expressions and complex
logic if there are no detailed explanations.
Consequently, we systematically categorize the planner-coder gap into five distinct error patterns (EP) and analyze their respective distribution frequencies.

EP-1. Gap on Core Concepts (32.7%).:

Many failure questions involve
specific core concepts essential to problem-solving.
For example, the requirement of HumanEval-26 2 2 2 Short for
“the 26th question in HumanEval ET.” Similar notations are used
in the rest of the paper. is to “remove all duplicates in the
input list”. Here, “remove duplicates” means deleting all
elements that appear more than once. The planner provides correct
instructions to “remove all duplicates” but does not clarify
the meaning of “duplicate”. This leaves a gap that the coder
misinterprets “remove duplicate” as removing repeated
occurrences of elements, but keeping one instance of all
duplicates.

EP-2. Gap on Edge Cases (19.5%).:

In some cases, the
generated code returns incorrect results for edge cases. Although the
plan correctly identifies edge cases using expressions such as “handle
the cases where…”, the coder still fails to handle them when there
are no clear explanations of the expected results for edge cases,
revealing the gap in edge case handling.

EP-3. Gap on Complex Logic (15.9%).:

Coders can fail to follow
the logic when there are insufficient concrete explanations and
analysis. In some cases, steps in the plan contain complex logic like “sort the coordinates of each row by columns”, which the coder fails to comprehend.

EP-4. Gap on Relational Phrases (9.7%).:

Our case study
demonstrates that coders are prone to misunderstand phrases that
express relationships between variables, indicating the need for
further interpretation of these expressions. Expressions
like “at least as much as”, “repeated two multiply two times”
are often misunderstood by the coder in our experiments.

EP-5. Gap on Condition Judgments (22.1%).:

Many
questions require different logic paths for various situations. Code implementations sometimes omit
certain logic paths specified in the plan when there are no detailed
explanations of the condition for each logic path. For example,
in HumanEval-128, the plan
for the mutated question correctly illustrates the proper logic as
“calculate the product of signs and sum of all numbers”. However, the question requires special treatment when the number is zero. Without a detailed explanation for this requirement in the plan, the coder omits the logic path to check if the number is zero.

Each of these error patterns represents a distinct type of information loss or semantic drift between planning and coding agents in the communication process, highlighting the complexity of the planner-coder gap.
They are not merely
about the prompt understanding of planner, but more on the communication gap between planner
and coder.

6. Augmenting MAS Robustness

In this section, we first discuss the differences between single
LLMs and MASs and formulate the code generation paradigm of MASs to clarify our repairing goal. Then, we
introduce our repairing method to enhance MAS robustness by first presenting an
overview, and then elaborating on two components of our repairing
method: multi-prompt generation and monitor agent insertion .

6.1. Reflection and Formulation of Planner-Coder Gap

In this work, we aim to enhance the robustness of MASs, which differs from the single
LLM paradigm with a fundamental paradigm shift in the code generation process.
As discussed in Sec. 2 , unlike the single LLM that directly encodes the input description into code,
the MASs include a more structured workflow with specialized agents for
different sub-tasks, where the planner plays a crucial role that determines the
overall generation logic.
To better depict the robustness issue of MASs and the planner-coder gap to repair, we formulate the code generation
paradigm for MASs.

In MASs, the planner serves as the central orchestrator, deciding the logic of the code to generate.
As discussed in Sec. 2 , the
planner functions as a critical intermediary that must bridge the conceptual gap
between human-readable requirements and coder-executable logic.
Specifically, the planner performs two critical transformations: first, it decomposes
user inputs into a comprehensive requirement set; then, it designs the coding steps to fulfill these requirements (Dong et al., 2024 ; Hong et al., 2023 ) :

(3) ℛ \displaystyle\mathcal{R} = 𝒜 p r ​ e ​ q ​ ( r ) \displaystyle=\mathcal{A}_{p}^{req}(r)

(4) ℒ \displaystyle\mathcal{L} = 𝒜 p l ​ o ​ g ​ i ​ c ​ ( ℛ ) \displaystyle=\mathcal{A}_{p}^{logic}(\mathcal{R})

where r r represents the input natural language requirement, ℛ = { r 1 , r 2 , … , r n } \mathcal{R}=\{r_{1},r_{2},...,r_{n}\} denotes the decomposed requirement set, and ℒ = { l 1 , l 2 , … , l m } \mathcal{L}=\{l_{1},l_{2},...,l_{m}\} represents the coding logic steps expressed in natural language. The generated plan includes both decomposed requirements and coding logic steps:

(5) p = { ℛ , ℒ } p=\{\mathcal{R},\mathcal{L}\}

Instructed by the coding steps, the coder then translates each step l i l_{i} into corresponding code blocks:

(6) c = 𝒜 c ​ ( ℒ ) = ⋃ i = 1 m 𝒜 c ​ ( l i ) c=\mathcal{A}_{c}(\mathcal{L})=\bigcup_{i=1}^{m}\mathcal{A}_{c}(l_{i})

where c c represents the generated code. The planner-coder gap manifests in this transformation, where semantic misalignment occurs between the coding logic and code.
Our analysis reveals that this gap accounts for 75.3% of failures (Table 3 ), highlighting a severe robustness issue.

Fundamentally, the interaction between agents in MAS can be viewed as a cascade
of information transformations across agent boundaries, where each agent
receives, processes, and transmits information to the next stage.
Intuitively, this multi-stage transformation process
is inherently susceptible to information loss (Shannon, 1948 ; Cover and Thomas, 2006 ) .
The aforementioned issue of planner-coder gap is further exacerbated
by the sequential nature of the transformation process, as there are multiple transformation stages (see Eq. 3 , 4 , 6 ).
More specifically, each transformation stage can introduce subtle semantic shifts and information loss:
the planner might correctly identify what needs to be done but express
it in terms that are ambiguous to the coder, or the coder might technically
implement the logic steps but miss the underlying intent.
This issue stems from the inherent
complexity of inter-agent communication and the structural limitations of
current task distribution (Li et al., 2024 ; Han et al., 2024 ; Ji et al., 2023 ) . Consequently, without robust mechanisms to promote effective communication across agent boundaries, MASs remain vulnerable to systematic
failures.

Figure 2. Overall workflow of our repairing method. Multi-prompt
generation generates various semantically-equivalent versions of user
input. The monitor agent conducts plan interpretation and code check to boost communication between planner and
coder.

6.2. Overview of Our Repairing Method

To mitigate the information loss discussed in Sec. 6.1 , we propose a repairing method that
enhances both the diversity of input expressions and the quality of inter-agent
communication. Our approach comprises two principal components: multi-prompt generation and monitor agent insertion .

As illustrated in Fig. 2 , upon receiving an input requirement, we first mutate the
requirement and generate multiple semantic-equivalent expressions to reduce the chance that MASs misunderstand specific expressions. For each generation, the planner generates the
original plan and forwards it to the monitor, a new agent we introduce to mitigate the planner-coder gap. After receiving the plan from the planner, the monitor agent
interprets the plan by providing detailed explanations for core concepts, edge cases, complex logic, relational
phrases, and conditional judgments (see Sec. 5 ), which compensate for the information loss. Subsequently, the coder implements code based
on this interpreted plan. In addition, the monitor also checks the implementation to enhance the alignment with the
interpreted plan and requests regeneration when misalignments are detected.

6.3. Multi-Prompt Generation

Our analysis in Sec. 4 demonstrated that semantic-preserving mutations can expose robustness issues in MASs. Meanwhile, as the
mutation operators explore different expressions of the questions, we observe that these mutations can also clarify ambiguous expressions, potentially improving performance on certain formulations. Leveraging this insight, we propose a multi-generation approach that explores different expressions of the same requirement by reusing
the semantic-preserving mutation operators introduced in
Table 1 .

When the MAS receives an input question, we apply
these mutation operators to generate k k alternative expressions as
generated prompts, with k + 1 k+1 different versions including the original
one. During the code generation process, where n n represents the total
number of generation attempts, we execute the MAS with the original input
question and each mutated question for n k + 1 \frac{n}{k+1} times.

This approach enhances robustness by leveraging diverse yet semantically
equivalent expressions, allowing the MAS to explore multiple interpretation
paths for the same requirement. In our implementation, we employ the MAS’s
backend LLM for mutation generation to ensure consistency. We set k = 2 k=2 (three total prompts including the original one) to balance
improvement gains with computational efficiency, which also demonstrates generalizability across
different MAS architectures and datasets, as shown in Sec. 7.2 .

Figure 3. Prompt for the monitor agent. Blue describes the task, brown echoes the five EPs in Sec. 5 , while green provides the i/o format and examples.

6.4. Monitor Agent Insertion

To enhance plan quality and strengthen planner-coder alignment, we introduce a monitor agent between planner and coder. This new agent in the whole MAS pipeline performs two critical tasks: plan interpretation and code check . The monitor agent serves as a crucial mechanism to compensate for the information loss inherent in the process of code generation.

Plan Interpretation. Despite remarkable efforts in previous work (Dong et al., 2024 ; Zhang et al., 2024a ; Islam et al., 2024 ) to devise sophisticated prompting
structures for planning agents, they primarily focus on choosing the right algorithm without considering the information transmission loss in MASs (see Eq. 3 , 4 ).
As discussed in Sec. 6.1 , the multi-stage transformation process of MAS introduces information loss, where the planner generates generally correct logic but discards implementation-critical details, leading to incorrect code implementations by the coder.

To effectively address this issue and enhance plan quality, we prompt the inserted
monitor agent to interpret the plan generated by the planner to make it more
comprehensible to the coder. The monitor agent aims to enhance the clarity and completeness of the planned coding logic and mitigate the planner-coder gap, rather
than correcting the semantic content of the plan. Specifically, the monitor
interprets the decomposed requirement ℛ \mathcal{R} and coding logic ℒ \mathcal{L} with detailed explanations and clarifications targeting the five
error patterns identified in Sec. 5 , producing an
interpreted plan p ′ p^{\prime} that bridges the semantic gap between planning and coding.
Fig. 3 presents an illustrative example of our prompt for the
monitor agent. By interpreting and expanding the plan p p into p ′ p^{\prime} , the monitor effectively
reduces the information loss between the coding logic and
final implementation, which ensures that critical implementation details lost in
Eq. 3 , 4 are restored before code generation.
We employ few-shot prompting with carefully crafted examples to
guide the interpretation process, focusing on the fundamental components of
programming plans—such as core concepts, logic flows, and edge cases—rather
than being tailored to any specific problem domain. This task-agnostic design
provides general applicability across different code generation scenarios.

Clarification. Note that one might consider incorporating the monitor’s interpretation logic directly
into the planner’s prompt. However, our proposed approach of a separate monitor
agent offers advantages in terms of modularity and scalability. Rather than
modifying the planner’s core functionality, this separation of concerns allows
the monitor to be seamlessly integrated as a “quality gate” into various
existing MAS architectures without altering their fundamental agent logic or
task distribution. This design promotes reusability, easier maintenance, and
addresses robustness issues across different MAS implementations without
requiring architecture-specific modifications. We also follow the practice
of consistent backend in a MAS to build the monitor agent with the backend LLMs of the MAS. The complete prompt is available in our artifact. 3 3 3 https://github.com/anonymous-for-submit/MAS_testing_repairing/tree/main/More_results/Monitor

Code Check. Although the interpreted plan could preserve crucial details, the information loss between the interpreted plan p ′ p^{\prime} and generated code c c remains undetected (see Eq. 6 ), posing a potential issue of misalignment.
Therefore, we
further incorporate code check as another monitoring task to check semantic alignment between the generated code and the interpreted plan.

Instead of using the testcase-based testing approaches that require dynamic execution with
proper running environment, we directly prompt LLMs to perform static inspection and
evaluate code compliance with the detailed specifications in p ′ p^{\prime} ,
which has been shown to be effective with the rich contextual information provided by the interpreted plan (Wang et al., 2024b , a ) .
After the coder produces the solution code, we feed both the interpreted
plan and the code back to the monitor to check whether the code
complies with the plan regarding the different aspects of interpretation,
as shown in Fig. 3 (c). If the monitor identifies mismatches
between code implementation and the plan, it returns the implementation
to the coding agent for revision. By checking alignment between the interpreted plan p ′ p^{\prime} and generated code c c , the monitor creates a validation loop that detects and corrects information drift, effectively reducing the information loss that would otherwise accumulate through unchecked transformations.
For efficiency, we use
zero-shot prompting for code check and limit the process to execute
only once.

7. Evaluation

We evaluate our repairing method by answering the following three research
questions:

RQ1::

Can our repairing method effectively mitigate failures identified in fuzzing?

RQ2::

How do different components contribute to the overall performance?

RQ3::

Can our repairing method enhance the robustness of MASs against fuzzing?

Specifically, RQ1 first gauges the effectiveness of our method in
repairing the failures that are identified in fuzzing. Then, we conduct an
ablation study to evaluate the individual contributions of different components
within our repairing method in RQ2. In RQ3, we re-run the fuzzing process to
evaluate whether our method enhances MASs’ robustness against fuzzing.

7.1. RQ1: Can our repairing method effectively mitigate failures
identified in fuzzing? 
Table 4. RQ1: Repair results on failures identified through fuzzing.

MAS Backend LLM HumanEval ET MBPP ET CodeContest CoderEval

Total Solved Ratio Total Solved Ratio Total Solved Ratio Total Solved Ratio

SCCG GPT-3.5 39 30 76.9% 60 48 80.0% 12 9 75.0% 11 9 81.8%

GPT-4o 22 11 50.0% 49 21 42.9% 21 13 61.9% 12 5 41.7%

Deepseek 28 15 53.6% 63 34 53.9% 12 8 66.7% 15 7 46.7%

MetaGPT GPT-3.5 49 37 75.5% 38 23 60.5% 9 5 55.6% 10 8 80.0%

GPT-4o 24 13 54.2% 37 16 43.2% 20 13 65.0% 9 5 55.6%

Deepseek 24 17 70.8% 38 20 53.3% 21 14 66.7% 9 8 88.9%

PairCoder GPT-3.5 15 8 53.3% 25 14 56.0% 22 9 40.9% 19 10 52.6%

GPT-4o 14 7 50.0% 25 16 64.0% 16 7 43.8% 20 14 70.0%

Deepseek 14 7 50.0% 26 14 53.8% 20 8 40.0% 12 9 75.0%

To address RQ1, we evaluate the performance of our repairing method on the
failed questions identified during fuzzing. We collect the failures for each
MAS with different backend LLMs to form our evaluation dataset. Since all
MASs initially failed to solve these questions, the baseline success rate is
zero. After applying our repairing method, we re-evaluate the MASs on these questions.

Table 4 presents the compelling repair results: our method
enables MASs to successfully solve 40.0%–88.9% of the questions they
previously failed. This significant improvement demonstrates that enhanced
expression diversity and better planner-coder communication effectively reduce
information loss during agent communication and enhance the robustness of MASs.
Taking HumanEval-18 as an example, the original plan of MetaGPT (Deepseek) only
mentions “please handle the edge case when the substring is empty,”
leading to the coder’s misunderstanding. In contrast, the interpretation
generated by the monitor further explains the logic of this case by
providing examples and a detailed logic flow. Consequently, the coder
successfully implements the correct code.

Table 5. Repair ratios for different categories of failures from SCCG (GPT-3.5).

Category EP-1 EP-2 EP-3 EP-4 EP-5 Overall Plan Logic Error Invalid

Solved (%) 80.0 83.3 80.0 100.0 85.7 83.9 66.7 0.0

The improvement contributed by our method varies across different MAS architectures. As shown in Table 4 ,
SCCG and MetaGPT show exceptional improvement, achieving repair rates
exceeding 80%. PairCoder shows more modest gains of 40%–75%.
Given that PairCoder incorporates plan selection strategies, the readability and quality of plans generated by
PairCoder surpass those of other MASs, therefore suffering less from the planner-coder gap.
Similarly, the choice of backend LLM influences repair effectiveness. MASs
using GPT-3.5 or Deepseek as backend LLM benefit more from our method compared to those
using GPT-4o. These results
indicate that our method is more beneficial for less capable MASs
with less effective backend LLMs, which typically struggle more with plan comprehension and are more
susceptible to the planner-coder gap.

Dataset characteristics also affect repair performance. HumanEval and CoderEval generally
achieves better repair performance, while CodeContest exhibits relatively lower repair rates. This disparity reflects
the inherent question length differences: MASs generate
concrete, focused plans that are straightforward to interpret for HumanEval’s concise questions, whereas
CodeContest’s complex problems lead to verbose plans that challenge effective
interpretation, which may exacerbate the planner-coder gap. A potential improvement could
involve summarizing verbose questions to avoid excessively long questions
or plans.

To further understand the strengths of our method,
Table 5 presents the repair
results for different error patterns identified in SCCG (GPT-3.5).
Our repairing method demonstrates remarkable effectiveness in
handling failures originating from the planner-coder gap, successfully
resolving 83.9% of such cases. Among the five EPs illustrated in
Sec. 5 , our repairing method performs best on failures
originating from relational phrases, suggesting that emphasizing such
phrases can effectively enhance the coder’s understanding of these
expressions. As expected, our method shows limited effectiveness on plan
logic errors, since these represent the reasoning flaws of the planner
rather than communication issues that our interpretation mechanism
is designed to address.

After adopting our method, MASs successfully solve 40.0%–88.9% of
failures identified during fuzzing. Our repairing method demonstrates remarkable
effectiveness in handling failures originating from the planner-coder gap,
successfully repairing the five EPs identified in Sec. 5 .

7.2. RQ2: How do different components contribute to the overall performance? 
Figure 4. Comparison of repairing performance when removing different
components. Figure 5. Comparison of failures of the original and repaired MASs found in
fuzzing.

We conduct ablation studies to investigate the effectiveness of multi-prompt generation and monitor agent insertion
in our repairing method. For monitor agent insertion, we separately examine “Plan Interpretation” and “Code
Check” to provide in-depth analysis. We present results with GPT-3.5 as the backend LLM, as it represents a
typical configuration with other LLMs exhibiting similar patterns. Complete results are available in our artifact. 4 4 4 https://github.com/anonymous-for-submit/MAS_testing_repairing/tree/main/More_results/RQ2_all_result.pdf

From Table 4 , we can find that removing any component degrades repair performance
across all three MASs, indicating that all components contribute meaningfully and our design
outperforms all alternative configurations.

Examining each component’s contribution reveals distinct patterns across MAS architectures. While disabling “Code Check” causes the smallest
performance decrease, enabling “Code Check” still contributes to the overall repair performance and “Only Code
Check” contributes approximately 40% of our method’s full repair capability, demonstrating that post-generation
validation effectively catches misalignments even without enhanced plan interpretation. The relative importance of
“Plan Interpretation” versus “Multi-prompt” varies by MAS architecture. In MetaGPT, “Only Plan Interpretation”
substantially outperforms “Only Multi-prompt” because MetaGPT generates abstract plans that challenge coder
comprehension, where interpretation bridges critical understanding gaps. Conversely, PairCoder benefits more from
“Only Multi-prompt” since its plans have better readability, making the diversity of input expressions from
multi-prompt generation more beneficial. These findings demonstrate that both strategies are valuable as different
MASs exhibit unique flaws: MASs like MetaGPT with abstract plans benefit most from interpretation, while those like
PairCoder with clear but rigidly expressed plans gains more from prompt diversity.

Our repairing method achieves optimal performance among all ablation configurations, with each component
mitigating different information loss and enhancing the overall repair capability.

7.3. RQ3: Can our repairing method enhance the robustness of MASs against fuzzing?

While RQ1 demonstrates that our repairing method can effectively fix failures identified during the initial fuzzing process, it remains unclear whether our repairing method can prevent or reduce new failures when subjected to continued fuzzing.
Therefore, in this RQ, we apply our repairing method to all MASs and re-execute the
fuzzing process proposed in Sec. 4 .
Fig. 5 shows the number of failures discovered from the original MASs and the repaired ones through fuzzing.

From Fig. 5 , we observe that on all three MASs, the speed of
discovering failures (i.e., the slope of the blue line and the red line) slows
down, and failure numbers decrease after applying our repairing method, showing
that the repaired MASs exhibit superior robustness compared to their original
counterparts.
Notably, PairCoder
(GPT-4o) exhibits the most remarkable robustness improvement against
fuzzing, with 85.7% of failures in HumanEval ET eliminated.
SCCG shows stable results across different backend LLMs and datasets, with
28.6%–53.8% decrease in failure numbers. These results indicate that our
repairing method can effectively enhance the robustness of MASs against
semantic-preserving mutations, resulting in fewer failures discovered
during fuzzing.

Across different datasets, MASs exhibit the best robustness improvement on HumanEval ET,
with failure numbers decreasing by 31.2%–85.7%, outperforming other
datasets. Questions in HumanEval ET are well-defined and rarely contain
complex logic, so our repairing method can effectively enhance the coder’s
understanding of the plan by clearly identifying the question’s meaning,
thereby improving MAS robustness.

Our repairing method enhances MAS robustness
against fuzzing, with up to 85.7% failure number reductions.
Repaired MASs exhibit superior robustness on the HumanEval ET dataset.

8. Discussion

Time Cost. Time efficiency is a critical factor in MASs,
as computational overhead directly impacts system scalability and practical deployment (Chen et al., 2024b ; Wu et al., 2023 ) .
To understand the time cost of our repairing method, we
measure the execution time of MASs with and without our repairing method.
Here, we select GPT-3.5 as the backend LLM and conduct experiments on
HumanEval ET, as other settings (e.g., datasets, LLMs) show similar trends.
Experiment results are shown in Table 6 .

Table 6. Comparison of time cost on HumanEval ET with GPT 3.5 as backend LLM.

Our method w/o Multi-prompt w/o Monitor Original

SCCG 13.6s 12.9s 11.3s 10.9s

MetaGPT 18.4s 17.6s 15.3s 14.8s

PairCoder 20.1s 19.0s 17.3s 16.4s

In general, the additional time overhead primarily comes from the
two components of our repairing method: multi-prompt generation and monitor
agent insertion. For multi-prompt generation, since we maintain the same
total number of generation attempts n n , the primary overhead comes only
from generating k k mutated prompts, which incurs little additional
overhead for API calls compared to the main generation process. Besides,
the monitor agent introduces two additional API calls per generation
attempt, taking merely 2.7s–3.7s across different MASs.

We clarify that this overhead is modest in real-world application
scenarios, given that a full MAS execution typically takes more than 30 seconds. On the other hand, the adoption of the monitor
agent brings substantial robustness improvements, as shown in
Sec. 7 , making the cost-benefit trade-off favorable. In
this regard, users of MASs are recommended to adopt our repairing method in
most scenarios, especially for cases with complex requirements where robustness is their primary concern.

Threats to Validity. We identified and mitigated several potential threats to validity in our evaluation.
The first threat is about the representativeness of our experimental setup. To
address this, we evaluated three popular MASs (Dong et al., 2024 ; Zhang et al., 2024a ; Hong et al., 2023 ) with three distinct LLMs (OpenAI, 2022 ; Achiam et al., 2023 ; Zhu et al., 2024 ) from different model families across four diverse datasets (Dong et al., 2025 ; Li et al., 2022 ; Yu et al., 2024b ) .
The second threat is about the reliability of semantic-preserving mutation. To
mitigate this threat, we employed GPT-4o (Achiam et al., 2023 ) to execute four
carefully designed mutation operators. We conducted manual verification to confirm
that the generated questions preserve the core semantics
and thus the robustness issues revealed by these tests are meaningful.
The last threat is subjectivity in manual failure analysis. To ensure reliable
implications from failure cases, we first build a failure taxonomy based on a pilot
study on 5% cases with the two software developers with over five years of
programming experience. They then independently categorize the reasons for each failure for the other 15% cases,
cross-check the annotation, and resolve all disagreements.

9. Related Work

MASs for Code Generation. Recent advancements in
LLMs (Achiam et al., 2023 ; Zhu et al., 2024 ; Bai et al., 2023 ) have exhibited
remarkable capabilities in code generation.
By defining different roles and establishing communication protocols among
multiple LLM agents, researchers have designed various MASs with diverse
architectures (Hong et al., 2023 ; Dong et al., 2024 ; Zhang et al., 2024a ; Huang et al., 2023 ; Islam et al., 2024 ; M. A. Islam, M. E. Ali, and M. R. Parvez, 2025 ) .
For instance, Hong et al. (Hong et al., 2023 ) propose MetaGPT, which
employs five distinct agents to simulate the development workflow of a
software company. Dong et al. (Dong et al., 2024 ) propose the Self-collaboration Code Generation framework,
which includes three different agents responsible for planning, coding, and testing.
To enhance the correctness of generated plans, some
approaches (Zhang et al., 2024a ; Islam et al., 2024 ; M. A. Islam, M. E. Ali, and M. R. Parvez, 2025 ) generate multiple
candidate plans and then use a selection mechanism to identify the
optimal plan with the highest score.
For example, Zhang et al. (Zhang et al., 2024a ) propose a clustering method to select the optimal plan, while
Islam et al. (Islam et al., 2024 ) introduce a dynamic traversal method to assign the confidence of the generated plans.
These approaches improve plan quality
in terms of logical correctness, thereby outperforming previous approaches
that rely on direct plan generation.

However, these methods focus primarily on logical correctness while neglecting the
communication gap between planner and coder, which is first identified in
this paper. In this work, we propose a repairing method to address the robustness issue of MASs by mitigating the gap.

Testing Code Generation Models. Numerous studies have applied testing
methodologies to evaluate code generation LLMs. Wang et
al. (Wang et al., 2023b ) introduce ReCode, a benchmark for robustness
evaluation through systematic perturbation testing, while Mastropaolo et
al. (Mastropaolo et al., 2023 ) conduct empirical studies on GitHub
Copilot’s robustness in real-world scenarios.
Recent advances have proposed diverse methods to evaluate
code generation models under different scenarios, like instruction
concretization (Yan et al., 2025 ) , multi-language robustness
assessment (Rabbi et al., 2025 ) , adversarial
training (Zhang et al., 2024c ) , and equivalence
checking (Wei et al., 2025 ) .
However, none of these works focus on MASs and their robustness
remains under-explored. We conducted the first fuzzing-based testing approach to investigate the robustness of MASs and identified the planner-coder gap as the main cause of robustness issues.

10. Conclusion

This paper presents the first comprehensive study on the robustness of MASs for code generation, revealing that MASs fail to solve problems they initially solved when faced with semantically equivalent mutations. We identify the “planner-coder gap” as a fundamental cause of the robustness issues and propose a novel repairing method incorporating multi-prompt generation and monitor agent insertion. Our findings provide essential insights for developing more reliable MASs and establish a foundation for future research on robustness in multi-agent code generation systems.

11. Data Availability

We release our code and data to facilitate future
research on MAS robustness at https://github.com/anonymous-for-submit/MAS_testing_repairing .

References

- (1)

- ope (2025) 2025. New tools for building agents. https://openai.com/index/new-tools-for-building-agents/ .

- clo (2025) 2025. Vertex AI offers new ways to build and manage multi-agent systems. https://cloud.google.com/blog/products/ai-machine-learning/build-and-manage-multi-system-agents-with-vertex-ai .

- Achiam et al. (2023) Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. 2023. Gpt-4 technical report. arXiv preprint arXiv:2303.08774 (2023).

- Austin et al. (2021) Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, et al. 2021. Program synthesis with large language models. arXiv preprint arXiv:2108.07732 (2021).

- Bai et al. (2023) Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, et al. 2023. Qwen technical report. arXiv preprint arXiv:2309.16609 (2023).

- Böhme et al. (2016) Marcel Böhme, Van-Thuan Pham, and Abhik Roychoudhury. 2016. Coverage-based greybox fuzzing as markov chain. In Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security . 1032–1043.

- Cao et al. (2024) Jialun Cao, Zhiyong Chen, Jiarong Wu, Shing-Chi Cheung, and Chang Xu. 2024. JavaBench: A Benchmark of Object-Oriented Code Generation for Evaluating Large Language Models. In Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering . 870–882.

- Chen et al. (2022) Bei Chen, Fengji Zhang, Anh Nguyen, Daoguang Zan, Zeqi Lin, Jian-Guang Lou, and Weizhu Chen. 2022. Codet: Code generation with generated tests. arXiv preprint arXiv:2207.10397 (2022).

- Chen et al. (2025) Jingyi Chen, Songqiang Chen, Jialun Cao, Jiasi Shen, and Shing-Chi Cheung. 2025. When LLMs Meet API Documentation: Can Retrieval Augmentation Aid Code Generation Just as It Helps Developers? arXiv preprint arXiv:2503.15231 (2025).

- Chen et al. (2024a) Liguo Chen, Qi Guo, Hongrui Jia, Zhengran Zeng, Xin Wang, Yijiang Xu, Jian Wu, Yidong Wang, Qing Gao, Jindong Wang, et al. 2024a. A survey on evaluating large language models in code generation tasks. arXiv preprint arXiv:2408.16498 (2024).

- Chen et al. (2021b) Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde De Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al. 2021b. Evaluating large language models trained on code. arXiv preprint arXiv:2107.03374 (2021).

- Chen et al. (2021a) Songqiang Chen, Shuo Jin, and Xiaoyuan Xie. 2021a. Testing your question answering software via asking recursively. In 2021 36th IEEE/ACM International Conference on Automated Software Engineering (ASE) . IEEE, 104–116.

- Chen et al. (2024b) Weize Chen, Jiarui Yuan, Chen Qian, Cheng Yang, Zhiyuan Liu, and Maosong Sun. 2024b. Optima: Optimizing Effectiveness and Efficiency for LLM-Based Multi-Agent System. arXiv preprint arXiv:2410.08115 (2024).

- Cover and Thomas (2006) Thomas M Cover and Joy A Thomas. 2006. Elements of Information Theory (2nd ed.). John Wiley & Sons.

- Dai et al. (2025) Shih-Chieh Dai, Jun Xu, and Guanhong Tao. 2025. A Comprehensive Study of LLM Secure Code Generation. arXiv preprint arXiv:2503.15554 (2025).

- Dehaerne et al. (2022) Enrique Dehaerne, Bappaditya Dey, Sandip Halder, Stefan De Gendt, and Wannes Meert. 2022. Code generation using machine learning: A systematic review. Ieee Access 10 (2022), 82434–82455.

- Dong et al. (2025) Yihong Dong, Jiazheng Ding, Xue Jiang, Ge Li, Zhuo Li, and Zhi Jin. 2025. Codescore: Evaluating code generation by learning code execution. ACM Transactions on Software Engineering and Methodology 34, 3 (2025), 1–22.

- Dong et al. (2024) Yihong Dong, Xue Jiang, Zhi Jin, and Ge Li. 2024. Self-collaboration code generation via chatgpt. ACM Transactions on Software Engineering and Methodology 33, 7 (2024), 1–38.

- Du et al. (2024) Xueying Du, Mingwei Liu, Kaixin Wang, Hanlin Wang, Junwei Liu, Yixuan Chen, Jiayi Feng, Chaofeng Sha, Xin Peng, and Yiling Lou. 2024. Evaluating large language models in class-level code generation. In Proceedings of the IEEE/ACM 46th International Conference on Software Engineering . 1–13.

- Fakhoury et al. (2024) Sarah Fakhoury, Aaditya Naik, Georgios Sakkas, Saikat Chakraborty, Madan Musuvathi, and Shuvendu Lahiri. 2024. Exploring the effectiveness of llm based test-driven interactive code generation: User study and empirical evaluation. In Proceedings of the 2024 IEEE/ACM 46th International Conference on Software Engineering: Companion Proceedings . 390–391.

- Fioraldi et al. (2022) Andrea Fioraldi, Dominik Christian Maier, Dongjia Zhang, and Davide Balzarotti. 2022. Libafl: A framework to build modular and reusable fuzzers. In Proceedings of the 2022 ACM SIGSAC Conference on Computer and Communications Security . 1051–1065.

- Fried et al. (2023) Daniel Fried, Armen Aghajanyan, Jessy Lin, Sida I. Wang, Eric Wallace, Freda Shi, Ruiqi Zhong, Wen-tau Yih, Luke Zettlemoyer, and Mike Lewis. 2023. InCoder: A Generative Model for Code Infilling and Synthesis. In International Conference on Learning Representations .

- Gao et al. (2024) Xinyu Gao, Yun Xiong, Deze Wang, Zhenhan Guan, Zejian Shi, Haofen Wang, and Shanshan Li. 2024. Preference-Guided Refactored Tuning for Retrieval Augmented Code Generation. In Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering . 65–77.

- Guo et al. (2024) Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Yu Wu, YK Li, et al. 2024. DeepSeek-Coder: When the Large Language Model Meets Programming–The Rise of Code Intelligence. arXiv preprint arXiv:2401.14196 (2024).

- Han et al. (2024) Siyuan Han, Qiujie Zhang, Yunfei Yao, Wei Jin, Zhicheng Xu, and Chaojun He. 2024. LLM Multi-Agent Systems: Challenges and Open Problems. arXiv preprint arXiv:2402.03578 (2024).

- He et al. (2024) Junda He, Christoph Treude, and David Lo. 2024. LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision and the Road Ahead. ACM Transactions on Software Engineering and Methodology (2024).

- Hong et al. (2023) Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, et al. 2023. Metagpt: Meta programming for multi-agent collaborative framework. arXiv preprint arXiv:2308.00352 3, 4 (2023), 6.

- Huang et al. (2023) Dong Huang, Jie M Zhang, Michael Luck, Qingwen Bu, Yuhao Qing, and Heming Cui. 2023. Agentcoder: Multi-agent-based code generation with iterative testing and optimisation. arXiv preprint arXiv:2312.13010 (2023).

- Iakusheva et al. (2023) SF Iakusheva, AS Khritankov, and DI Harbachonak. 2023. Metamorphic testing for generative artificial intelligence systems. System informatics 22 (2023), 37–44.

- Ishibashi and Nishimura (2024) Yoichi Ishibashi and Yoshimasa Nishimura. 2024. Self-organized agents: A llm multi-agent framework toward ultra large-scale code generation and optimization. arXiv preprint arXiv:2404.02183 (2024).

- Islam et al. (2024) Md Ashraful Islam, Mohammed Eunus Ali, and Md Rizwan Parvez. 2024. MapCoder: Multi-Agent Code Generation for Competitive Problem Solving. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) . 4912–4944.

- Ji et al. (2023) Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan Su, Yan Xu, Etsuko Ishii, Ye Jin Bang, Andrea Madotto, and Pascale Fung. 2023. Survey of Hallucination in Natural Language Generation. Comput. Surveys 55, 12, 1–38.

- Jiang et al. (2024) Juyong Jiang, Fan Wang, Jiasi Shen, Sungju Kim, and Sunghun Kim. 2024. A survey on large language models for code generation. arXiv preprint arXiv:2406.00515 (2024).

- Jiang et al. (2023) Shuyang Jiang, Yuhao Wang, and Yu Wang. 2023. Selfevolve: A code evolution framework via large language models. arXiv preprint arXiv:2306.02907 (2023).

- Joel et al. (2024) Sathvik Joel, Jie JW Wu, and Fatemeh H Fard. 2024. A survey on llm-based code generation for low-resource and domain-specific programming languages. arXiv preprint arXiv:2410.03981 (2024).

- Li et al. (2024) Xinyi Li, Sai Wang, Siqi Zeng, Yu Wu, and Yi Yang. 2024. A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges. Vicinagearth 1, 1 (2024), 9.

- Li et al. (2022) Yujia Li, David Choi, Junyoung Chung, Nate Kushman, Julian Schrittwieser, Rémi Leblond, Tom Eccles, James Keeling, Felix Gimeno, Agustin Dal Lago, et al. 2022. Competition-level code generation with alphacode. Science 378, 6624 (2022), 1092–1097.

- Li et al. (2023) Zongjie Li, Chaozheng Wang, Zhibo Liu, Haoxuan Wang, Dong Chen, Shuai Wang, and Cuiyun Gao. 2023. Cctest: Testing and repairing code completion systems. In 2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE) . IEEE, 1238–1250.

- Lin et al. (2024) Feng Lin, Dong Jae Kim, et al. 2024. SOEN-101: Code Generation by Emulating Software Process Models Using Large Language Model Agents. arXiv preprint arXiv:2403.15852 (2024).

- Liu et al. (2024) Junwei Liu, Kaixin Wang, Yixuan Chen, Xin Peng, Zhenpeng Chen, Lingming Zhang, and Yiling Lou. 2024. Large language model-based agents for software engineering: A survey. arXiv preprint arXiv:2409.02977 (2024).

- Liu et al. (2023) Pengfei Liu, Weizhe Yuan, Jinlan Fu, Zhengbao Jiang, Hiroaki Hayashi, and Graham Neubig. 2023. Pre-train, prompt, and predict: A systematic survey of prompting methods in natural language processing. ACM computing surveys 55, 9 (2023), 1–35.

- M. A. Islam, M. E. Ali, and M. R. Parvez (2025) M. A. Islam, M. E. Ali, and M. R. Parvez. 2025. CODESIM: Multi-Agent Code Generation and Problem Solving through Simulation-Driven Planning and Debugging. arXiv preprint arXiv:2502.05664 (2025).

- Mastropaolo et al. (2023) Antonio Mastropaolo, Luca Pascarella, Emanuela Guglielmi, Matteo Ciniselli, Simone Scalabrino, Rocco Oliveto, and Gabriele Bavota. 2023. On the robustness of code generation techniques: An empirical study on github copilot. In 2023 IEEE/ACM 45th International Conference on Software Engineering (ICSE) . IEEE, 2149–2160.

- Mathews and Nagappan (2024) Noble Saji Mathews and Meiyappan Nagappan. 2024. Test-Driven Development and LLM-based Code Generation. In Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering . 1583–1594.

- McHugh (2012) Mary L McHugh. 2012. Interrater reliability: the kappa statistic. Biochemia medica 22, 3 (2012), 276–282.

- Nijkamp et al. (2022) Erik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu, Huan Wang, Yingbo Zhou, Silvio Savarese, and Caiming Xiong. 2022. Codegen: An open large language model for code with multi-turn program synthesis. arXiv preprint arXiv:2203.13474 (2022).

- Ognawala et al. (2018) Saahil Ognawala, Thomas Hutzelmann, Eirini Psallida, and Alexander Pretschner. 2018. Improving function coverage with munch: a hybrid fuzzing and directed symbolic execution approach. In Proceedings of the 33rd Annual ACM Symposium on Applied Computing . 1475–1482.

- OpenAI (2022) OpenAI. 2022. Introducing ChatGPT. https://openai.com/index/chatgpt/ . Accessed: May 30, 2025.

- Pan et al. (2025) Melissa Z Pan, Mert Cemri, Lakshya A Agrawal, Shuyi Yang, Bhavya Chopra, Rishabh Tiwari, Kurt Keutzer, Aditya Parameswaran, Kannan Ramchandran, Dan Klein, et al. 2025. Why do multiagent systems fail?. In ICLR 2025 Workshop on Building Trust in Language Models and Applications .

- Park et al. (2023) Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S Bernstein. 2023. Generative agents: Interactive simulacra of human behavior. In Proceedings of the 36th annual acm symposium on user interface software and technology . 1–22.

- Qian et al. (2023) Chen Qian, Xin Cong, Cheng Yang, Weize Chen, Yusheng Su, Juyuan Xu, Zhiyuan Liu, and Maosong Sun. 2023. Communicative agents for software development. arXiv preprint arXiv:2307.07924 6, 3 (2023).

- Rabbi et al. (2025) Fazle Rabbi, Zushuo Ding, and Jinqiu Yang. 2025. A Multi-Language Perspective on the Robustness of LLM Code Generation. arXiv preprint arXiv:2504.19108 (2025).

- Rehman and Srinivasan (2023) Faqeer Ur Rehman and Madhusudan Srinivasan. 2023. Metamorphic testing for machine learning: Applicability, challenges, and research opportunities. In 2023 IEEE International Conference On Artificial Intelligence Testing (AITest) . IEEE, 34–39.

- Reimers and Gurevych (2019) Nils Reimers and Iryna Gurevych. 2019. Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP) . 3982–3992.

- Shannon (1948) Claude E Shannon. 1948. A Mathematical Theory of Communication. Bell System Technical Journal 27, 3 (1948), 379–423.

- Shin and Nam (2021) Jiho Shin and Jaechang Nam. 2021. A survey of automatic code generation from natural language. Journal of Information Processing Systems 17, 3 (2021), 537–555.

- Tran et al. (2025) Khanh-Tung Tran, Dung Dao, Minh-Duong Nguyen, Quoc-Viet Pham, Barry O’Sullivan, and Hoang D Nguyen. 2025. Multi-Agent Collaboration Mechanisms: A Survey of LLMs. arXiv preprint arXiv:2501.06322 (2025).

- Veggalam et al. (2016) Spandan Veggalam, Sanjay Rawat, Istvan Haller, and Herbert Bos. 2016. Ifuzzer: An evolutionary interpreter fuzzer using genetic programming. In Computer Security–ESORICS 2016: 21st European Symposium on Research in Computer Security, Heraklion, Greece, September 26-30, 2016, Proceedings, Part I 21 . Springer, 581–601.

- Wang et al. (2024b) Chengpeng Wang, Wuqi Zhang, Zian Su, Xiangzhe Xu, Xiaoheng Xie, and Xiangyu Zhang. 2024b. LLMDFA: analyzing dataflow in code with large language models. Advances in Neural Information Processing Systems 37 (2024), 131545–131574.

- Wang et al. (2024a) Chengpeng Wang, Wuqi Zhang, Zian Su, Xiangzhe Xu, and Xiangyu Zhang. 2024a. Sanitizing Large Language Models in Bug Detection with Data-Flow. In Findings of the Association for Computational Linguistics: EMNLP 2024 . 3790–3805.

- Wang et al. (2025) Liwen Wang, Wenxuan Wang, Shuai Wang, Zongjie Li, Zhenlan Ji, Zongyi Lyu, Daoyuan Wu, and Shing-Chi Cheung. 2025. IP Leakage Attacks Targeting LLM-Based Multi-Agent Systems. arXiv preprint arXiv:2505.12442 (2025).

- Wang et al. (2023b) Shiqi Wang, Zheng Li, Haifeng Qian, Chenghao Yang, Zijian Wang, Mingyue Shang, Varun Kumar, Samson Tan, Baishakhi Ray, Parminder Bhatia, et al. 2023b. ReCode: Robustness Evaluation of Code Generation Models. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) . 13818–13843.

- Wang et al. (2023a) Yue Wang, Hung Le, Akhilesh Gotmare, Nghi Bui, Junnan Li, and Steven Hoi. 2023a. CodeT5+: Open Code Large Language Models for Code Understanding and Generation. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing . 1069–1088.

- Wang et al. (2021) Yue Wang, Weishi Wang, Shafiq Joty, and Steven C. H. Hoi. 2021. CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Understanding and Generation. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing . Association for Computational Linguistics, 8696–8708.

- Wei et al. (2025) Anjiang Wei, Jiannan Cao, Ran Li, Hongyu Chen, Yuhui Zhang, Ziheng Wang, Yaofeng Sun, Yuan Liu, Thiago SFX Teixeira, Diyi Yang, et al. 2025. Equibench: Benchmarking code reasoning capabilities of large language models via equivalence checking. arXiv e-prints (2025), arXiv–2502.

- Wu et al. (2023) Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Shaokun Zhang, Erkang Zhu, Beibin Li, Li Jiang, Xiaoyun Zhang, and Chi Wang. 2023. A Survey on Large Language Model-Based Multi-Agent Systems: Common Workflows, Challenges, and Opportunities. arXiv preprint arXiv:2308.11432 (2023).

- Xie et al. (2022) Xiaoyuan Xie, Pengbo Yin, and Songqiang Chen. 2022. Boosting the revealing of detected violations in deep learning testing: A diversity-guided method. In Proceedings of the 37th IEEE/ACM International Conference on Automated Software Engineering . 1–13.

- Xu et al. (2023) Yuzhuang Xu, Shuo Wang, Peng Li, Fuwen Luo, Xiaolong Wang, Weidong Liu, and Yang Liu. 2023. Exploring large language models for communication games: An empirical study on werewolf. arXiv preprint arXiv:2309.04658 (2023).

- Yan et al. (2025) Ming Yan, Junjie Chen, Jie M Zhang, Xuejie Cao, Chen Yang, and Mark Harman. 2025. Robustness evaluation of code generation systems via concretizing instructions. Information and Software Technology 179 (2025), 107645.

- Yu et al. (2024b) Hao Yu, Bo Shen, Dezhi Ran, Jiaxin Zhang, Qi Zhang, Yuchi Ma, Guangtai Liang, Ying Li, Qianxiang Wang, and Tao Xie. 2024b. Codereval: A benchmark of pragmatic code generation with generative pre-trained models. In Proceedings of the 46th IEEE/ACM International Conference on Software Engineering . 1–12.

- Yu et al. (2024a) Jiahao Yu, Xingwei Lin, Zheng Yu, and Xinyu Xing. 2024a. { \{ LLM-Fuzzer } \} : Scaling assessment of large language model jailbreaks. In 33rd USENIX Security Symposium (USENIX Security 24) . 4657–4674.

- Zalewski (2025) Michał Zalewski. 2025. American fuzzy lop. http://lcamtuf.coredump.cx/afl/ . Accessed on May 30,2025.

- Zhang et al. (2024a) Huan Zhang, Wei Cheng, Yuhan Wu, and Wei Hu. 2024a. A Pair Programming Framework for Code Generation via Multi-Plan Exploration and Feedback-Driven Refinement. In Proceedings of the 39th IEEE/ACM International Conference on Automated Software Engineering . 1319–1331.

- Zhang et al. (2024b) Kechi Zhang, Jia Li, Ge Li, Xianjie Shi, and Zhi Jin. 2024b. Codeagent: Enhancing code generation with tool-integrated agent systems for real-world repo-level coding challenges. arXiv preprint arXiv:2401.07339 (2024).

- Zhang et al. (2024c) Yuhao Zhang, Shiqi Wang, Haifeng Qian, Zijian Wang, Mingyue Shang, Linbo Liu, Sanjay Krishna Gouda, Baishakhi Ray, Murali Krishna Ramanathan, Xiaofei Ma, et al. 2024c. CodeFort: Robust Training for Code Generation Models. In Findings of the Association for Computational Linguistics: EMNLP 2024 . 5262–5277.

- Zheng et al. (2024) Dewu Zheng, Yanlin Wang, Ensheng Shi, Ruikai Zhang, Yuchi Ma, Hongyu Zhang, and Zibin Zheng. 2024. Towards more realistic evaluation of LLM-based code generation: an experimental study and beyond. arXiv preprint arXiv:2406.06918 (2024).

- Zhu et al. (2024) Qihao Zhu, Daya Guo, Zhihong Shao, Dejian Yang, Peiyi Wang, Runxin Xu, Y Wu, Yukun Li, Huazuo Gao, Shirong Ma, et al. 2024. Deepseek-coder-v2: Breaking the barrier of closed-source models in code intelligence. arXiv preprint arXiv:2406.11931 (2024).
