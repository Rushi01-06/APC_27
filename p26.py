from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(self):
        pass

class PDFReport(Report):
    def generate(self):
        return "Generating PDF report layout and compiling to document..."

class ExcelReport(Report):
    def generate(self):
        return "Generating Excel report and populating spreadsheet cells..."

class HTMLReport(Report):
    def generate(self):
        return "Generating HTML report and rendering web markup..."

def process_report(report: Report):
    result = report.generate()
    print(result)

if __name__ == "__main__":
    pdf = PDFReport()
    excel = ExcelReport()
    html = HTMLReport()

    process_report(pdf)
    process_report(excel)
    process_report(html)
