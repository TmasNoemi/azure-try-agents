class ReporterAgent:
    def __init__(self):
        self.name = "ReporterAgent"

    def run(self, analysis_result: dict):
        # Qui creeremo il report / alert per gli analyst
        return {"alert": False, "message": "stub reporter"}
