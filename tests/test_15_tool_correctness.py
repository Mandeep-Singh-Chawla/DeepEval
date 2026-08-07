from deepeval import assert_test
from deepeval.metrics import ToolCorrectnessMetric
from deepeval.test_case import LLMTestCase, ToolCall


def test_tool_correctness():
    test_case = LLMTestCase(
        input="Check the refund status for order 12345.",
        actual_output="Your order 12345 is eligible for a full refund.",
        tools_called=[ToolCall(name="get_order_status", input_parameters={"order_id": "12345"})],
        expected_tools=[ToolCall(name="get_order_status", input_parameters={"order_id": "12345"})],
    )
    metric = ToolCorrectnessMetric(threshold=0.5)
    assert_test(test_case, [metric])
