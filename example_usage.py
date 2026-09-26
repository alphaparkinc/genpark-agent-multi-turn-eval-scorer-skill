import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AgentMultiTurnEvalScorerClient

def main():
    client = AgentMultiTurnEvalScorerClient()
    res = client.evaluate_trajectory_run()
    print("=== Agent Multi-Turn Eval Scorer Output ===")
    print(f"Goal: {res['task_goal']}")
    print(f"Steps: {res['total_steps_executed']} (Baseline: {res['optimal_step_baseline']}) | Redundant: {res['redundant_steps_detected']}")
    print(f"Trajectory Score: {res['trajectory_score']}/100 ({res['quality_rating']})")
    print(f"Overhead Ratio: {res['step_overhead_ratio']} | Goal Achieved: {res['autonomous_goal_achieved']}")

if __name__ == '__main__':
    main()
