import smolagents

import autoboltagent
import autoboltagent.prompts


def test_guessing_agent():

    # Use the smallest Instruct model available for fast CI feedback
    model = smolagents.TransformersModel(
        model_id="HuggingFaceTB/SmolLM-135M-Instruct",
        max_new_tokens=200,  # Keep generation short for speed
    )

    # Create the GuessingAgent and run it
    response = autoboltagent.GuessingAgent(model).run(
        autoboltagent.prompts.EXAMPLE_TASK_INSTRUCTIONS
    )

    # Make sure the response exists
    assert response is not None


def test_low_fidelity_agent():

    # Use the smallest Instruct model available for fast CI feedback
    model = smolagents.TransformersModel(
        model_id="HuggingFaceTB/SmolLM-135M-Instruct",
        max_new_tokens=200,  # Keep generation short for speed
    )

    # Create the LowFidelityAgent and run it
    response = autoboltagent.LowFidelityAgent(model).run(
        autoboltagent.prompts.EXAMPLE_TASK_INSTRUCTIONS
    )

    # Make sure the response exists
    assert response is not None


def test_high_fidelity_agent():

    # Use the smallest Instruct model available for fast CI feedback
    model = smolagents.TransformersModel(
        model_id="HuggingFaceTB/SmolLM-135M-Instruct",
        max_new_tokens=200,  # Keep generation short for speed
    )

    # Create the HighFidelityAgent and run it
    response = autoboltagent.HighFidelityAgent(model).run(
        autoboltagent.prompts.EXAMPLE_TASK_INSTRUCTIONS
    )

    # Make sure the response exists
    assert response is not None


def test_dual_fidelity_agent():

    # Use the smallest Instruct model available for fast CI feedback
    model = smolagents.TransformersModel(
        model_id="HuggingFaceTB/SmolLM-135M-Instruct",
        max_new_tokens=200,  # Keep generation short for speed
    )

    # Create the DualFidelityAgent and run it
    response = autoboltagent.DualFidelityAgent(model).run(
        autoboltagent.prompts.EXAMPLE_TASK_INSTRUCTIONS
    )

    # Make sure the response exists
    assert response is not None
