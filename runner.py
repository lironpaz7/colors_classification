from k_means import KMeans


class Runner:
    def __init__(self, k, num_of_iters, points, max_seeds):
        self.k = k
        self.num_of_iters = num_of_iters
        self.points = points
        self.max_seeds = max_seeds

    def run_test(self):
        test = KMeans(self.k, self.num_of_iters)
        total_sse = []
        total_sum = 0
        for seed in range(self.max_seeds):
            test.run(self.points, seed)
            sse = test.compute_sse()
            total_sse.append(sse)
            total_sum += sse
        minimal_sse = min(total_sse)
        mean_sse = total_sum / 10
        maximal_sse = max(total_sse)
        return [f"0-{self.max_seeds - 1}", self.k, self.num_of_iters, minimal_sse, mean_sse, maximal_sse]
