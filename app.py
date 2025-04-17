import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, jsonify
import asyncio
from agents import Runner, set_default_openai_client, set_default_openai_api, set_tracing_disabled
from planner_agents.understanding_agent import understanding_agent
from planner_agents.resource_agent import resource_agent
from openai import AsyncOpenAI

app = Flask(__name__)
print(os.getenv("OPENAI_API_KEY"))  # Debugging line to check if the API key is loaded

custom_client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://models.inference.ai.azure.com",  # or any custom endpoint
)

set_default_openai_client(client=custom_client)  # Set to True if you want to use the same client for tracing
set_tracing_disabled(True)  # Disable tracing if not needed
set_default_openai_api(api="chat_completions")  # or "responses" based on your needs

@app.route("/analyze", methods=["POST"])
def analyze_project():
    data = request.json
    project_description = data.get("description")

    async def run_agents():
        understanding = await Runner.run(understanding_agent, project_description)
        if understanding is None or understanding.final_output is None:
            raise ValueError("Understanding agent returned no output.")
        resource = await Runner.run(resource_agent, understanding.final_output)
        if resource is None or resource.final_output is None:
            raise ValueError("Resource agent returned no output.")
        return {
            "understanding": understanding.final_output,
            "resources": resource.final_output
        }

    result = asyncio.run(run_agents())
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)