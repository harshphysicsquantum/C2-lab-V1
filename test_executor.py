
from executor import execute_task

# Test 1: Supported system_info task
result = execute_task("system_info")
print("Test 1:", result)
assert result == "Simulated system information"

# Test 2: Supported health_check task
result = execute_task("health_check")
print("Test 2:", result)
assert result == "Agent simulation is healthy"

# Test 3: Unsupported task type
result = execute_task("unsupported_task")
print("Test 3:", result)
assert result is None

print("All executor tests passed!")
