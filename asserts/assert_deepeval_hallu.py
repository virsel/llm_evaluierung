from typing import Dict, Any, Union
from deepeval.test_case import LLMTestCase
from deepeval.metrics import HallucinationMetric
from deepeval.models import GPTModel
from deepeval import assert_test


def get_assert(output: str, options: Dict[str, Any]) -> Union[bool, float, Dict[str, Any]]:
    # Set a threshold for hallucination score (adjust based on your needs)
    HALLUCINATION_THRESHOLD = 0.5

    # Extract required data from options
    prompt = options.get('prompt', "default prompt")
    context = options.get('vars', {}).get('context', "default context")
    fact = options.get('vars', {}).get('fact', "default fact")
    
    try:
        metric = HallucinationMetric(model=GPTModel(model="gpt-3.5-turbo"))
        
        test_case = LLMTestCase(
            input=prompt,               
            actual_output=output,       
            context=[context],    
        )

        # Run the assertion test
        metric.measure(test_case)
    except Exception as e:
        print("Error calculating hallucination score:", e)
        return {
        "pass": False,
        "score": None,
        "reason": e,
    }
    
    return {
        "pass": metric.score <= HALLUCINATION_THRESHOLD,
        "score": metric.score,
        "reason": metric.reason,
    }

# Main entry point
if __name__ == "__main__":
    # Sample data to test the function
    sample_output = "The mitochondrion is the powerhouse of the cell."
    sample_options = {
        "prompt": "What is the function of mitochondria?",
        "vars": {
            "context": "In biology, cells have organelles, each with specific functions.",
            "fact": "Mitochondria produce energy in the form of ATP."
        }
    }

    # Run get_assert with the sample data
    result = get_assert(sample_output, sample_options)

    # Print the result
    print("Result of hallucination check:", result)
