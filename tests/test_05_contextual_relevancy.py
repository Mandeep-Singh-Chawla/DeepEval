from deepeval import assert_test
from deepeval.metrics import ContextualRelevancyMetric
from deepeval.test_case import LLMTestCase


def test_contextual_relevancy():
    test_case = LLMTestCase(
        input="What if these shoes don't fit?",
        actual_output="We offer a 30-day full refund at no extra cost.",
        retrieval_context=[
            "All customers are eligible for a 30 day full refund at no extra cost."
        ],
    )
    metric = ContextualRelevancyMetric(threshold=0.5)
    assert_test(test_case, [metric])
