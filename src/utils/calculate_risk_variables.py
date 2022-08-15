class RiskVariables:
    def turns_args_ineligible(self, insurance_scores, *args):
        for arg in args:
            insurance_scores[arg] = "ineligible"
        return insurance_scores

    def increase_points(self, insurance_scores, points, *args):
        for arg in args:
            if insurance_scores[arg] != "ineligible":
                insurance_scores[arg] += points
        return insurance_scores

    def decrease_points(self, insurance_scores, points, *args):
        for arg in args:
            if insurance_scores[arg] != "ineligible":
                insurance_scores[arg] -= points
