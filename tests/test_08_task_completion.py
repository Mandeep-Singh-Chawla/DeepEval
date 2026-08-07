from deepeval import assert_test
from deepeval.metrics import TaskCompletionMetric
from deepeval.test_case import LLMTestCase


def test_task_completion():
    test_case = LLMTestCase(
        input="Summarize our refund policy in one sentence.",
        actual_output="Customers can get a full refund within 30 days at no extra cost.",
    )
    metric = TaskCompletionMetric(threshold=0.5)
    assert_test(test_case, [metric])
