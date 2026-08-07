from deepeval import assert_test
from deepeval.metrics import ContextualPrecisionMetric
from deepeval.test_case import LLMTestCase


def test_contextual_precision():
    test_case = LLMTestCase(
        input="What if these shoes don't fit?",
        actual_output="We offer a 30-day full refund at no extra cost.",
        expected_output="You're eligible for a free full refund within 30 days of purchase.",
        retrieval_context=[
            "All customers are eligible for a 30 day full refund at no extra cost.",
            "Our store sells running shoes and accessories.",
        ],
    )
    metric = ContextualPrecisionMetric(threshold=0.5)
    assert_test(test_case, [metric])
