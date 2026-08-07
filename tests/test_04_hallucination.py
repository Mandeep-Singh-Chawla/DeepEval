from deepeval import assert_test
from deepeval.metrics import HallucinationMetric
from deepeval.test_case import LLMTestCase


def test_hallucination():
    test_case = LLMTestCase(
        input="What if these shoes don't fit?",
        actual_output="We offer a 30-day full refund at no extra cost.",
        context=[
            "All customers are eligible for a 30 day full refund at no extra cost."
        ],
    )
    metric = HallucinationMetric(threshold=0.5)
    assert_test(test_case, [metric])
