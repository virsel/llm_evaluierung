from typing import Dict, TypedDict, Union, Any

def get_assert(output: str, context) -> Union[bool, float, Dict[str, Any]]:
    # print('Prompt:', context['prompt'])
    # print('Vars', context['vars']['topic'])

    # This return is an example GradingResult dict
    return len(output) < 300