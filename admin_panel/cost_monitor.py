class CostMonitor:
    def __init__(self):
        # Placeholder for the data structure storing cost details
        self.costs = []

    def record_cost(self, api_call, cost):
        """
        Record the cost of an individual API call.
        """
        self.costs.append((api_call, cost))

    def get_total_cost(self):
        """
        Calculate and return the total cost incurred by all API calls.
        """
        return sum(cost for _, cost in self.costs)

    def get_average_cost(self):
        """
        Calculate and return the average cost per API call.
        """
        total_calls = len(self.costs)
        if total_calls == 0:
            return 0
        return self.get_total_cost() / total_calls
 
