import json, sys
from client import AgentMultiTurnEvalScorerClient

def handle_mcp_request(payload):
    method = payload.get("method")
    req_id = payload.get("id", 1)
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "agent-multi-turn-eval-scorer", "version": "1.0.0"}}}
    elif method == "tools/list":
        return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [{"name": "evaluate_trajectory_run", "description": "Scores multi-turn autonomous agent trajectories for efficiency, redundancy, and goal achievement."}]}}
    elif method == "tools/call":
        client = AgentMultiTurnEvalScorerClient()
        res = client.evaluate_trajectory_run()
        return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
    return {"jsonrpc": "2.0", "id": req_id, "result": {"status": "ACTIVE"}}

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps(handle_mcp_request({"method": "tools/list"})))
    else:
        client = AgentMultiTurnEvalScorerClient()
        print(json.dumps(client.evaluate_trajectory_run(), indent=2))
