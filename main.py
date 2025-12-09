from agents.detector import DetectorAgent
from agents.analyzer import AnalyzerAgent
from agents.reporter import ReporterAgent

def main():
    print("Hackathon AI Agents – ambiente pronto ✅")

    # Per ora solo istanze vuote, poi aggiungiamo la logica
    detector = DetectorAgent()
    analyzer = AnalyzerAgent()
    reporter = ReporterAgent()

    print("Agenti creati:", detector, analyzer, reporter)

if __name__ == "__main__":
    main()
