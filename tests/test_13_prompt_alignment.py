from deepeval import assert_test
from deepeval.metrics import PromptAlignmentMetric
from deepeval.test_case import LLMTestCase


def test_prompt_alignment():
    test_case = LLMTestCase(
        input="Answer in one short sentence only: What is your refund window?",
        actual_output="We offer a 30-day full refund.",
    )
    metric = PromptAlignmentMetric(
        prompt_instructions=["Answer in one short sentence only."],
        threshold=0.5,
    )
    assert_test(test_case, [metric])
