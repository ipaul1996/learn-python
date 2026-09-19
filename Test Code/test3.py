from enum import StrEnum

class SuperTest:
    def __init__(self):
        print("SuperTest init")


class Test(SuperTest):
    def __init__(self, count):
        # super().__init__()
        print("Test init")
        self.count = count

    def __enter__(self):
        print("Test Enter")
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        print("Test Exit")
        return False


with Test(10) as t:
    print(t.count)


class CallEndReason(StrEnum):
    user_hung_up = "user_hung_up"  # on transport event
    call_end_tool = "call_end_tool"
    call_transfer_tool = "call_transfer_tool"
    user_unresponsive = "user_unresponsive"  # due to user idle timeout or _max_waiting_time_in_secs reached
    max_duration_reached = "max_duration_reached"
    disconnected_due_to_failure = "disconnected_due_to_failure"  # We disconnected due to unexpected exception in pipeline
    ddos_protection = "ddos_protection"  # disconnected due to ddos protection
    not_available = "not_available"  # default value for call end reason
    answering_machine_detected = "answering_machine_detected"

    @property
    def display_name(self) -> str:
        """Returns a UI-friendly display name for the enum value."""
        display_names = {
            self.user_hung_up: "User Disconnected",
            self.call_end_tool: "Agent Disconnected",
            self.call_transfer_tool: "Call Transferred",
            self.user_unresponsive: "User Silent",
            self.max_duration_reached: "Max Duration Reached",
            self.disconnected_due_to_failure: "Agent Failure",
            self.ddos_protection: "DDoS Protection",
            self.not_available: "Not Available",
            self.answering_machine_detected: "Answering Machine Detected",
        }
        return display_names.get(self, self.value)
    



x = CallEndReason.call_end_tool

print(x)
print(type (x))
print(x.display_name)