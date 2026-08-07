from deepeval import assert_test
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, SingleTurnParams


def test_g_eval_correctness():
    test_case = LLMTestCase(
        input="What if these shoes don't fit?",
        actual_output="We offer a 30-day full refund at no extra cost.",
        expected_output="You're eligible for a free full refund within 30 days of purchase.",
    )
    metric = GEval(
        name="Correctness",
        criteria="Determine if the actual output is correct based on the expected output.",
        evaluation_params=[
            SingleTurnParams.ACTUAL_OUTPUT,
            SingleTurnParams.EXPECTED_OUTPUT,
        ],
        threshold=0.5,
    )
    assert_test(test_case, [metric])
