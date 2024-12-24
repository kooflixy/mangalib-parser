class Level:
    def __init__(self, total_points: int, level: int, max_level_points: int, current_level_points: int, point_percent_progress: int):
        self.total_points = total_points
        self.level = level
        self.max_level_points = max_level_points
        self.current_level_points = current_level_points
        self.point_percent_progress = point_percent_progress