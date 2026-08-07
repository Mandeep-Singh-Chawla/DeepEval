# DeepEval — Metrics

Test suite to evaluate LLM apps showing DeepEval metrics with sample test cases. Replace `actual_output` with your app’s response to evaluate a real system.

## What this shows

| # | Metric | Script | Required fields |
|---|--------|--------|-----------------|
| 1 | GEval | `tests/test_01_g_eval.py` | fields in `evaluation_params` |
| 2 | AnswerRelevancy | `tests/test_02_answer_relevancy.py` | input, actual_output |
| 3 | Faithfulness | `tests/test_03_faithfulness.py` | input, actual_output, retrieval_context |
| 4 | Hallucination | `tests/test_04_hallucination.py` | input, actual_output, context |
| 5 | ContextualRelevancy | `tests/test_05_contextual_relevancy.py` | input, retrieval_context |
| 6 | ContextualPrecision | `tests/test_06_contextual_precision.py` | input, retrieval_context, expected_output |
| 7 | ContextualRecall | `tests/test_07_contextual_recall.py` | input, retrieval_context, expected_output |
| 8 | TaskCompletion | `tests/test_08_task_completion.py` | input, actual_output |
| 9 | Toxicity | `tests/test_09_toxicity.py` | input, actual_output |
| 10 | Bias | `tests/test_10_bias.py` | input, actual_output |
| 11 | Misuse | `tests/test_11_misuse.py` | input, actual_output (+ domain on metric) |
| 12 | PIILeakage | `tests/test_12_pii_leakage.py` | input, actual_output |
| 13 | PromptAlignment | `tests/test_13_prompt_alignment.py` | input, actual_output (+ prompt_instructions on metric) |
| 14 | RoleViolation | `tests/test_14_role_violation.py` | input, actual_output (+ role on metric) |
| 15 | ToolCorrectness | `tests/test_15_tool_correctness.py` | input, tools_called, expected_tools |

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env and add your API key
```

## Run

```bash
source .venv/bin/activate
deepeval test run tests/
# or one file:
deepeval test run tests/test_04_hallucination.py
```

## Notes

- `actual_output` is hardcoded for demos. In real use, call your LLM app and set that field.
- Hallucination uses `context`. RAG grounding uses Faithfulness + `retrieval_context`.
- Metrics 9–12 and 14 support safety / guardrail-style evaluation of outputs.
- Metric 15 covers agent tool-calling correctness.
- Optional: set `CONFIDENT_API_KEY` to upload runs to Confident AI.
